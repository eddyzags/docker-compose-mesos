# Mesos compose

Mesos compose projects aims to launch a pod of containers which are Mesos, Marathon, Zookeeper and Weavescope with Docker Compose for testing purposes.

# Versions

- Apache Zookeeper 3.4
- Apache Mesos 1.2.1 (1 master, 3 slaves)
- Marathon 1.4.5
- Weave scope 1.5

![Mesos compose architecture](http://imgur.com/Bci5FtU.jpg)

# Usage

```shell
make cluster-up
```
Start the cluster in background


```shell
make cluster-stop
```
Stop the cluster


```shell
make cluster-test
```
Start a python scripts to check the service availability


```shell
make deploy-app
```
Deploy simple web service in the cluster through Marathon

URLs:
* Mesos Master UI : http://localhost:5050
* Mesos Slaves: http://localhost:5051;5052;5053
* Marathon UI : http://localhost:8080
* Weavescope UI : http://localhost:4040
