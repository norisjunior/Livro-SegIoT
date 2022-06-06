# Envia valor simulado de temperatura

import os
import paho.mqtt.client as mqtt
import time
import random

broker = "broker.emqx.io"
client = mqtt.Client("Dispositivo001")
sub_topic = "/livrosegiot/Dispositivo001/cmd"
pub_topic = "/livrosegiot/Dispositivo001/attrs"
Connected = False
espera = 10

#Conexão com o MQTT Broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        global Connected                #Use global variable
        Connected = True                #Signal connection

        # Subscribing in on_connect() - if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(sub_topic)
    else:
        print("Falha na conexão com o Broker... ", rc)

# Recebendo mensagem MQTT
def on_message(client, userdata, msg):
    print('\nMensagem recebida')
    print(" - tópico: ", msg.topic)
    print(" - mensagem: " , msg.payload)



# Publicando
def on_publish():
    valor_temp = round(random.randint(1,30) + random.random(), 2)
    payload = "temp|" + str(valor_temp)
    client.publish(pub_topic, payload)




client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883, 60)
client.loop_start()        #start the loop
while Connected != True:    #Wait for connection
    time.sleep(0.1)

################################################################
#After started, run forever sending measurements until CTRL+C
try:
    while True:
        #Continuously send temperature data
        on_publish()
        time.sleep(espera)
except KeyboardInterrupt:
    # disconnect
    print("Parando o cliente ...")
    client.loop_stop()
    client.disconnect()
