# Capítulo 7

Neste capítulo há um script em python que envia continuamente uma mensagem MQTT para o Broker (broker.emqx.io) - o mesmo usado no capítulo 5.

A intenção é observar o ID do cliente que envia mensagens (esse ID pode ser observado usando o Wireshark e observando o cabeçalho da mensagem MQTT):
```
cd ~/Livro-SegIoT/Cap7
python3 envia-valor.py
```
