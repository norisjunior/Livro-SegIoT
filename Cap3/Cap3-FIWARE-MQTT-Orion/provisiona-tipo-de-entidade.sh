#!/bin/bash
# Provisiona dispositivo
# apikey: livrosegiot


curl -iX POST \
  'http://localhost:4041/iot/services' \
  -H 'Content-Type: application/json' \
  -H 'fiware-service: openiot' \
  -H 'fiware-servicepath: /' \
  -d '{
 "services": [
   {
     "apikey":      "livrosegiot",
     "cbroker":     "http://orion:1026",
     "entity_type": "Dispositivo",
     "resource":    "/iot/d"
   }
 ]
}'
