# mqtt-fastapi-wrapper

A simple Fastapi wrapper for MQTT


## Prerequisites

-   Docker; if you don't have it yet, follow the [installation instructions];
-   Docker Compose; refer to the official documentation for the [installation guide].


## Getting Up and Running Locally with Docker

* Configure `Eclipse Mosquitto` message broker by editing `mosquitto.conf` file, e.g.:

      # Plain MQTT protocol
      persistence false
      allow_anonymous true
      connection_messages true
      log_type all
      listener 1883

* Open a terminal at the project root and run the following for local development:

  - Build the Stack:

          $ docker-compose build

  - Run the Stack (use `-d` to run in the detached mode):

          $ docker-compose up

  - Run the stack in Debugging mode (with *ipdb* support):

          $ docker-compose run --rm --service-ports backend

By default, service will be available on the following routes:

    http://0.0.0.0/docs
    http://0.0.0.0/redoc
    http://0.0.0.0/api/v1/openapi.json

  [installation instructions]: https://docs.docker.com/install/#supported-platforms
  [installation guide]: https://docs.docker.com/compose/install/
