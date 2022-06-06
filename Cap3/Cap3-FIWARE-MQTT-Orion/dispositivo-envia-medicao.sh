#!/bin/bash
# Provisiona dispositivo
# apikey: livrosegiot

docker run -it --rm --name mqtt-publisher --network \
  fiware_default efrecon/mqtt-client pub -h mosquitto -m "temp|25,00" \
  -t "/livrosegiot/Dispositivo001/attrs"
