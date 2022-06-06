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
client = mqtt.Client("Dispositivo001")
sub_topic = "/livrosegiot/Dispositivo001/cmd"
pub_topic = "/livrosegiot/Dispositivo001/attrs"
Connected = False
espera = 10

#chave simétrica, deve ser usada no destinatário para decifrar a mensagem
chave = '4c6976726f536567496f5453454e4143'.encode("utf8")



#Cifração
def aes_ctr_encrypt(payload, chave):
    #payload = mensagem
    IV = os.urandom(16)
    ctr = Crypto.Util.Counter.new(128, initial_value=int(hexlify(IV), 16))
    cipher = AES.new(chave,AES.MODE_CTR,counter=ctr)
    ciphertext = cipher.encrypt(payload)
    return IV, ciphertext

#Decifração
def aes_ctr_decrypt(payload_cifrado, chave):
    #payload_cifrado = texto_cifrado
    IV = payload_cifrado[:16]
    texto_cifrado = payload_cifrado[16:]
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
    print('\nDISPOSITIVO IOT - Mensagem recebida')
    print(" - tópico: ", msg.topic)
    print(" - mensagem: " , msg.payload)


# Publicando
def on_publish():
    valor_temp = round(random.randint(1,30) + random.random(), 2)
    mensagem = "temp|" + str(valor_temp)
    mensagem = str.encode(mensagem)
    init_v, texto_cifrado = aes_ctr_encrypt(mensagem, chave)
    texto_cifrado = hexlify(init_v).decode('utf-8') + hexlify(texto_cifrado).decode('utf-8')
    texto_cifrado = unhexlify(texto_cifrado)
    print('     - IV:', hexlify(init_v).decode('utf-8'))
    print('     - Texto cifrado: ', hexlify(texto_cifrado).decode('utf-8'))

    #teste
    #texto_claro = aes_ctr_decrypt(texto_cifrado, chave)
    #texto_claro = texto_claro.decode("utf-8")
    #print('Mensagem recebida: ', texto_claro)

    client.publish(pub_topic, hexlify(texto_cifrado).decode('utf-8'))


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
        on_publish()
        time.sleep(espera)
except KeyboardInterrupt:
    # disconecta quando pressionadas as teclas CTRL+C
    print("Parando o cliente ...")
    client.loop_stop()
    client.disconnect()
