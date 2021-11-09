# mqtt-fastapi-wrapper

## Quick start

Create `mosquitto.conf` with the following content:

    ➜  /tmp cat mosquitto.conf 
    persistence false
    allow_anonymous true
    connection_messages true
    log_type all
    listener 1883


Run MQTT broker using Docker

    docker run --rm --name mosquitto -p 1883:1883 --rm -v `pwd`/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto

Run `uvicorn`:

    uvicorn main:app --port 8888 --reload --log-level debug

See a list of available routes `http://localhost:8888/docs`
