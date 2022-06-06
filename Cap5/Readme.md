# Capítulo 5

Neste capítulo há dois scripts para demonstrar como uma mensagem MQTT pode ser cifrada na origem e decifrada no destino, tendo um intermediário no caminho: o MQTT Broker.

Nesse exemplo, é necessário abrir três terminais:

- Terminal 1: para mostrar as mensagens que passam pelo Broker (no caso define-se um Broker publicamente disponível na Internet: broker.emqx.io, na porta 1883)
- Terminal 2: para executar o script ***recebe-e-decifra-mqtt.py***
- Terminal 3: para executar o script ***cifra-e-envia-mqtt.py***

Para isso, é necessário instalar os softwares python3 e mosquitto-clients, e os pacotes paho-mqtt e pycryptodome, usando os seguintes comandos:
```
sudo apt install python3 mosquitto-clients
pip install paho-mqtt pycryptodome
```


Depois, abra um terminal para observar as mensagens que trafegam no Broker (***ATENÇÃO: nunca faça subscribe no tópico '#', pois o volume de mensagens é imenso***)



##### Terminal 1:
```
cd ~/Livro-SegIoT/Cap5/
mosquitto_sub -t "/livrosegiot/#"
```

##### Terminal 2 (que receberá a mensagem):
```
cd ~/Livro-SegIoT/Cap5/
python3 recebe-e-decifra-mqtt.py
```

##### Terminal 3 (que enviará a mensagem):
```
cd ~/Livro-SegIoT/Cap5/
python3 cifra-e-envia-mqtt.py
```
