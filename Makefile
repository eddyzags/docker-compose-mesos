cluster-images:
	@echo "Building images..."
	docker-compose build

cluster-info:
	@echo "Fetching containers informations..."
	docker-compose ps

cluster-up:
	@echo "Running mesos environment..."
	docker-compose up -d
	@echo "Mesos environment is now ready"

cluster-stop:
	@echo "Cleaning mesos environment.."
	docker-compose down -v

cluster-test:
	@echo "Testing mesos environment..."
	tests/services-up.py weavescope 4040 zookeeper 2181 marathon 8080 mesos-mater 5050 mesos-slave-1 2201 mesos-slave-2 2202 mesos-slave-3 2203

deploy-app:
	@echo "Deploying healthy application"
	@curl -X POST --header "Content-Type: application/json" --data @tests/app.json http://localhost:8080/v2/apps

cluster-recreate: stop images up
