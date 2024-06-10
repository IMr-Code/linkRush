
#!/usr/bin/python3
# Desenvolvedor: IMr Code
# Github: https://github.com/IMr-Code
# Esta ferramenta foi desenvolvida para ser usada de forma etica e moral
# Nao me responsabilizo com qualquer atividade negativa que possa ser feita
# Utilizando essa ferramenta

import requests
from bs4 import BeautifulSoup
from os import system

def request(url):
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    response = requests.get(url,verify=False)
    if response.status_code == 200:
        return response.text
    else:
        return False

def scraping(html):
    soup = BeautifulSoup(html,'html.parser')
    print('-'*30)
    link = soup.find_all('a',href=True)
    for link in link:
        print(f"\033[92mLINK ===>\033[0m {link['href']}")
    print('-'*30)
    print('\033[31m=======> LINKS DE CAMINHOS DE IMAGENS <========\033[0m')

    image_links = [img['src'] for img in soup.find_all('img')]

    for link in image_links:
        print(f"\033[92mLink da imagem\033[0m: {link}")
    print('-'*30)

def banner():
    system('clear')
    system("echo '\e[1;31m'")
    print('*'*20)
    os.system("echo linkRUsh | figlet")
    print('*'*20)
    system("echo '\e[0m'")
    print('\033[31mBy: Mr Code\033[0m')
    print('')

def main():
    banner()
    url = input('[+]- Digite a URL do site: ')
    html = request(url)
    if html:
        scraping(html)
    else:
        print('Ocorreu um erro ao efetuar o requests')
main()
