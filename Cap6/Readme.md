# Capítulo 6

Para utilizar o Leshan LWM2M Server, é necessário usar o java.

Para instalar:

```
sudo apt install default-jdk
```

## Utilização do LWM2M
Para iniciar o Leshan LWM2M Server, é necessário abrir um terminal e executar:

```
cd ~/Livro-SegIoT/Cap6
java -jar ./leshan-server-demo.jar
```

Abra um navegador e acesse o endereço: **http://localhost:8080**

Para iniciar o Leshan Client (que simula um dispositivo IoT), execute:
```
cd ~/Livro-SegIoT/Cap6
java -jar ./leshan-client-demo.jar
```

Depois de iniciar o Leshan Client, observe no navegador que é exibido na listagem um novo cliente. Para verificar as opções, clique no nome do cliente no navegador.
