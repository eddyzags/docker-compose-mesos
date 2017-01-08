images:
	@echo "Building images..."
	docker-compose build

info:
	docker-compose ps

cluster-run:
	@echo Running mesos environment...
	docker-compose up -d
	tests/services-up.py weavescope 4040 zookeeper 2181 marathon 8080 mesos-mater 5050 mesos-slave-1 2201 mesos-slave-2 2202 mesos-slave-3 2203
	@echo Mesos environment is now ready

cluster-clean:
	@echo Cleaning mesos environment..
	docker-compose down -v
