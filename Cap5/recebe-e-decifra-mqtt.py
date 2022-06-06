# LivroSegIoT - Cap. 5
# Simula envio criptografado de temperatura (aplicando confidencialidade)

import os
import paho.mqtt.client as mqtt
import time
import random
from Crypto.Cipher import AES
import Crypto.Cipher.AES
import Crypto.Util.Counter
from binascii import hexlify, unhexlify


broker = "broker.emqx.io"
client = mqtt.Client("Cloud001")
sub_topic = "/livrosegiot/Dispositivo001/attrs"
Connected = False
espera = 10

#chave simétrica, deve ser usada no destinatário para decifrar a mensagem
chave = '4c6976726f536567496f5453454e4143'.encode("utf8")


#Decifração
def aes_ctr_decrypt(payload_cifrado, chave):
    IV = unhexlify(payload_cifrado[:32])
    texto_cifrado = unhexlify(payload_cifrado[32:])
    ctr = Crypto.Util.Counter.new(128, initial_value=int.from_bytes(IV, byteorder='big'))
    cipher = AES.new(chave, AES.MODE_CTR, counter=ctr)
    plaintext = cipher.decrypt(texto_cifrado)
    return plaintext


#Conexão com o MQTT Broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        global Connected
        Connected = True
        client.subscribe(sub_topic) #realiza subscribe no tópico especificado
    else:
        print("Falha na conexão com o Broker... ", rc)


# Recebendo mensagem MQTT
def on_message(client, userdata, msg):
    print('\nNUVEM - Mensagem recebida')
    print(" - tópico: ", msg.topic)
    print(" - mensagem: " , msg.payload)

    texto_claro = aes_ctr_decrypt(msg.payload, chave)
    texto_claro = texto_claro.decode("utf-8")
    print('Mensagem recebida: ', texto_claro)



client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883, 60)
client.loop_start()        #start the loop
while Connected != True:    #Wait for connection
    time.sleep(0.1)

##############################################################################
#Envia mensagens continuamente, considerando o tempo que está na variável
#`espera`, que por default é de 10 segundos
try:
    while True:
        print("Aguardando mensagem ...")
        time.sleep(espera)
except KeyboardInterrupt:
    # disconecta quando pressionadas as teclas CTRL+C
    print("Parando o cliente ...")
    client.loop_stop()
    client.disconnect()
