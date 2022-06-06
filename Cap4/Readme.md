# Capítulo 4

Busca por endereços IP com portas abertas.

**Caso não tenha sido executado nos capítulos anteriores:**
```
cd ~
git clone https://github.com/norisjunior/Livro-SegIoT.git
```

## Instalar masscan
```
cd ~/Livro-SegIoT/Cap4
sudo apt update
sudo apt install git gcc make libpcap-dev
git clone https://github.com/robertdavidgraham/masscan
cd masscan
make
make install
```

Depois de instalar o masscan, podemos usar o software para fazer uma busca massiva por um escopo de endereços IP e especificar quais portas serão o alvo da tentativa de verificação se estão abertas: (2)

Esse comando procura pelas portas 443 e da porta 20 a 80 nos endereços IP que vão do 192.168.1.1 ao 192.168.1.254:

```
sudo masscan -p443,20-80 192.168.1.0/24
```
