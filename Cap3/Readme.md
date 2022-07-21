# Capítulo 3

## Orquestrando os conteineres com o Orion Context Broker e o FIWARE MQTT IoT Agent:
*Adaptado de: https://github.com/FIWARE/tutorials.IoT-over-MQTT*

**Caso não tenha sido executado no capítulo anterior:**
```
cd ~
git clone https://github.com/norisjunior/Livro-SegIoT.git
```

## Inicializando a plataforma
```
cd ~/Livro-SegIoT/Cap3/Cap3-FIWARE-MQTT-Orion
sudo ./services create
sudo ./services start
```

##### Conferindo se o IoT Agent para MQTT está em funcionamento:
```
curl -X GET 'http://localhost:4041/iot/about' | python -m json.tool
```

## Provisionando tipo de entidade
```
sudo ./provisiona-tipo-de-entidade.sh
```

## Provisionando sensor de temperatura no Dispositivo001
```
sudo ./provisiona-sensor-temperatura.sh
```


### Verifica que não há medições enviadas (valor do atributo temperatura está vazio):
```
curl -X GET \
  'http://localhost:1026/v2/entities/Dispositivo001?type=Notebook' \
  -H 'fiware-service: openiot' \
  -H 'fiware-servicepath: /' | python -m json.tool
```

## Dispositivo simulado envia medição de temperatura:
```
sudo ./dispositivo-envia-medicao.sh
```

### Verifica há uma nova medição de temperatura (valor 25,00):
```
curl -X GET \
  'http://localhost:1026/v2/entities/Dispositivo001?type=Notebook' \
  -H 'fiware-service: openiot' \
  -H 'fiware-servicepath: /' | python -m json.tool
```
