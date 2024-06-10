**linkRush**
*Desenvolvedor:* IMr Code

O linkRush é uma ferramenta automatizada para coleta de links de tags a e img de uma página HTML, a ferramenta é simples de se usar e muito significativa para a coleta e analise de links

**Instalação**

A ferramenta foi desenvolvida para funcionar em ambiente Linux. você precisa ter o git para poder clonar o repositorio da ferramenta

apt install git 
ou
pkg install git

Caso não tiver o python3, sera necessário instalar

apt install python3
ou
pkg install python3 -y

agora precisamos instalar alguns pacotes, pode rodar o arquivo requirements.txt ou instalar manualmente.
Passo simples:

pip install -r requeriments.txt

O comando a cima já instala todos os pacotes, mas caso não tenha o PIP instale antes de rodar o comando a  cima.

apt install python3-pip
ou
pkg install pip
ou
pkg install python3-pip

agora vamos instalar os pacotes do python

pip install requests
pip install bs4

pronto já temos os pacotes necessários, vamos clonar a ferramenta

git clone https://github.com/IMr-Code/linkRush.git

Depois de clonar a ferramenta, entre no directorio da ferramenta

cd linkRush

agora basta rodar a ferramenta, e seja feliz

python3 linkRush.py
