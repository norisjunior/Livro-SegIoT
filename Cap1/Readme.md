# Capítulo 1

## Instalar docker-ce
```
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release python3 python-is-python3
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

##### Verificando a instalação ocorreu com sucesso:
```
sudo docker run hello-world
```

## Instalar docker-compose
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```


## Usar o FIWARE com microsserviços
```
cd ~
git clone https://github.com/FIWARE/tutorials.Getting-Started.git
cd tutorials.Getting-Started
git checkout NGSI-v2
sudo docker-compose -p fiware up -d
```

##### Verificando se o Orion inicializou
```
curl -X GET 'http://localhost:1026/version'
```


## Criar a entidade sensor de temperatura na floresta amazônica (simulando o envio de informação por um dispositivo)
```
curl -iX POST \
  'http://localhost:1026/v2/entities' \
  -H 'Content-Type: application/json' \
  -d '
{
    "id": "temperature_amazon_rainforest_3303",
    "type": "LM35",
    "temperature": {
        "type": "Float",
        "value": "26.8",
        "metadata": {
            "Unit": {
                "value": "Celsius",
                "type": "String"
            }
        }
    },
    "location": {
        "type": "geo:point",
        "value": "-3.464619, -62.214979"
    },
    "temperature_precision": {
        "type": "Float",
        "value": "0.01"
    },
    "name": {
        "type": "Text",
        "value": "Temperatura Floresta Amazonica"
    }
}'
```


## Recuperar a informação (ação executada por uma aplicação usando a API fornecida pela plataforma FIWARE)
```
curl -X GET http://localhost:1026/v2/entities/temperature_amazon_rainforest_3303?type=LM35&options=keyValues | python -m json.tool
```
