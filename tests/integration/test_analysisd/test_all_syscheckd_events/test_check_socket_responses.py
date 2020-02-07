# Copyright (C) 2015-2020, Wazuh Inc.
# Created by Wazuh, Inc. <info@wazuh.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import os

import pytest
import yaml

from wazuh_testing import global_parameters
from wazuh_testing.analysis import callback_analysisd_message
from wazuh_testing.tools import WAZUH_PATH, LOG_FILE_PATH, WAZUH_LOGS_PATH
from wazuh_testing.tools.monitoring import FileMonitor

pytestmark = [pytest.mark.linux, pytest.mark.win32, pytest.mark.tier(level=2)]

# variables

test_data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
alerts_json = os.path.join(WAZUH_LOGS_PATH, 'alerts', 'alerts.json')
messages_path = os.path.join(test_data_path, 'syscheck_events.yaml')
wazuh_alerts_monitor = FileMonitor(alerts_json)

wdb_path = os.path.join(os.path.join(WAZUH_PATH, 'queue', 'db', 'wdb'))
analysis_path = os.path.join(os.path.join(WAZUH_PATH, 'queue', 'ossec', 'queue'))
monitored_sockets, receiver_sockets = None, None  # These variables will be set in the fixture create_unix_sockets
monitored_sockets_params = [(wdb_path, 'TCP')]
# monitored_sockets_params = []
receiver_sockets_params = [(analysis_path, 'UDP')]
used_daemons = ['ossec-analysisd']

with open(messages_path) as f:
    test_cases = yaml.safe_load(f)

# Syscheck variables
wazuh_log_monitor = FileMonitor(LOG_FILE_PATH)
n_directories = 0
directories_list = list()
testdir = 'testdir'


@pytest.mark.parametrize('test_case',
                         [test_case['test_case'] for test_case in test_cases],
                         ids=[test_case['name'] for test_case in test_cases])
def test_validate_socket_responses(configure_environment_standalone_daemons, create_unix_sockets,
                                   wait_for_analysisd_startup, test_case: list):
    """
    """
    for stage in test_case:
        expected = callback_analysisd_message(stage['output'])
        receiver_sockets[0].send([stage['input']])
        response = monitored_sockets[0].start(timeout=global_parameters.default_timeout,
                                              callback=callback_analysisd_message).result()
        assert response == expected, 'Failed test case stage {}: {}'.format(test_case.index(stage) + 1, stage['stage'])
