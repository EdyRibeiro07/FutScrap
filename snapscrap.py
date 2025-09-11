### SALVA O HTML DA PAGINA DE COMENTARIOS EM UM ARQUIVO .MD
### POR ENQUANTO ESSE CÓDIGO SERVE APENAS PARA TER UM ARQUIVO COM O HTML SALVO E 
### NÃO PRECISAR FICAR FAZENDO REQUESTS TODA VEZ QUE EXECUTAR O CÓDIGO

import requests
from bs4 import BeautifulSoup

headers = {
'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36"
}

response = requests.get('https://www.espn.com.br/futebol/comentario/_/jogoId/733439', headers=headers)
dom = BeautifulSoup(response.text, 'html.parser')

with open("html.md", "w") as arquivo:
    arquivo.write(dom.prettify())