# mqtt-fastapi-wrapper

A simple Fastapi wrapper for MQTT


## Prerequisites

`Docker` (`Docker Compose`) has to be installed and properly configured.


## Quick start

* Configure `Eclipse Mosquitto` message broker by editing `mosquitto.conf` file, e.g.:

      # Plain MQTT protocol
      persistence false
      allow_anonymous true
      connection_messages true
      log_type all
      listener 1883

* Run `docker-compose`(use `-d` for detached mode):

      $ docker-compose up [-d]

For the list of available docs/routes and resources see:

    http://0.0.0.0/docs
    http://0.0.0.0/redoc
    http://0.0.0.0/api/v1/openapi.json
