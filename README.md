# Mesos compose

Mesos compose projects aims to launch a pod of containers which are Mesos, Marathon, Zookeeper and Weavescope with Docker Compose for testing purposes.

# Versions

- Apache Zookeeper 3.4
- Apache Mesos 1.2.1 (1 master, 3 slaves)
- Marathon 1.4.5
- Weave scope 1.5

![Mesos compose architecture](http://imgur.com/Bci5FtU.jpg)

# Usage

Start the mesos cluster in the background
make cluster-up

Stop the mesos cluster
make cluster-stop

Test the mesos cluster
make cluster-test

Deploy test application
make deploy-app

URLs:
* Mesos Master UI : http://localhost:5050
* Mesos Slaves UI : http://localhost:5051;5052;5053
* Marathon UI : http://localhost:8080
* Weavescope UI : http://localhost:4040
