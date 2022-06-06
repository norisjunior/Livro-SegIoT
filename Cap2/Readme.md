# Capítulo 2

## Instalando o Docker:
```
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release python3 python-is-python3
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

## Instalando o docker-compose:
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

## Orquestrando os conteineres e o Orion Context Broker:
*Adaptado de: https://github.com/FIWARE/tutorials.Getting-Started*

```
cd ~
git clone https://github.com/norisjunior/Livro-SegIoT.git
cd Livro-SegIoT/Cap2/Cap2-FIWARE-Orion/
sudo docker-compose -p fiware up -d
```
