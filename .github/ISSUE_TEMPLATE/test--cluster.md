---
name: 'Test: Cluster'
about: Test suite for cluster.
title: ''
labels: ''
assignees: ''

---

# Cluster test

| Version | Revision | Branch |
| --- | --- | --- |
| x.y.z | rev | branch |

## Installation

- [ ] Installation by default: Run `/var/ossec/bin/wazuh-clusterd -f`
- [ ] Installation by default: Run `/var/ossec/bin/wazuh-clusterd -f`
- [ ] Installation by default - centos6: Run `/var/ossec/bin/wazuh-clusterd -f`

## Configuration

- [ ] Configure cluster: No key.
- [ ] Configure cluster: Wrong key.
- [ ] Configure cluster: Wrong node type.
- [ ] Configure cluster: Wrong master node IP.

## Cluster

- [ ] Start the master before/after the workers.
- [ ] Change path to opt in master and var in workers.
- [ ] Synchronization process when one of the workers is down.
- [ ] Stop master and start it after some time.
- [ ] Disconnect worker node internet connection and check it disconnects after 2 minutes. Check the master node removes that node. Connect the node to the internet again and check itreconnects to the master node without restarting.
- [ ] Disconnect worker and reconnect it again to the internet in less than 2 minutes. Check it keeps working as usual.
- [ ] File level tests: Run automatic tests and review KO files.

## Cluster control
- [ ] Master
    - [ ] check `cluster_control -l`
    - [ ] check `cluster_control -a`
    - [ ] check `cluster_control -i`
- [ ] Worker
    - [ ] check `cluster_control -l`
    - [ ] check `cluster_control -a`
    - [ ] check `cluster_control -i`

## Agents

- [ ] Register an agent in master and point it to a worker.
The *client.keys* must be propagated and the agent must be reporting. Then, if the agents are listed in the master, it must be Active.
- [ ] `cluster-control -a` must show the agents information and the manager.
- [ ] Connect the previous agent to a different worker and review logs/alerts. It must be transparent for the user.
- [ ] Remove an agent in master. It must be removed in all the workers.

## Groups

- [ ] Create a new group.
- [ ] Create a file in a group.
- [ ] Modify a file in a group.
- [ ] Remove a file in a group.
- [ ] Remove group.
- [ ] Re-create a removed group.
- [ ] Assign agent to a group.
- [ ] Unassign agent group.
    - [ ] Assign a group in a worker using md5. Then, check if it is propagated to the master.

## Ruleset

- [ ] Modify a file in the rules/decoders/lists directory.
- [ ] Add a file in the rules/decoders/lists directory.
- [ ] Remove a file in the rules/decoders/lists directory.

## Performance

- [ ] 1 master, 10 workers, 100k agent-info and agent-groups.
