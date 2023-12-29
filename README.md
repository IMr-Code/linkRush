**W E B -GEL I N K**
*Desenvolvedor: * Mr Code

O WEB-GELINK é uma ferramenta automatizada para coleta de links de tags a e img de uma página HTML, a ferramenta é simples de se usar e muito significativa para a coleta e analise de links

**Instalação**

A ferramenta foi desenvolvida para funcionar em ambiente Linux. você precisa ter o git para poder clonar o repositorio da ferramenta

apt install git 
ou
pkg install git

Caso não tiver o python3, sera necessário instalar

apt install python3
ou
pkg install python3 -y

agora precisamos instalar alguns pacotes, caso não tenha o pip nstale com esse comando:

apt install python3-pip
ou
pkg install pip
ou
pkg install python3-pip

agora vamos instalar os pacotes do python

pip install requests
pip install bs4

pronto já temos os pacotes necessários, vamos clonar a ferramenta

git clone https://github.com/CalebMarcelino/web-gelink.git

Depois de clonar a ferramenta, entre no directorio da ferramenta

cd web-getlink

agora basta rodar a ferramenta, e seja feliz

python3 web-gelink.py
