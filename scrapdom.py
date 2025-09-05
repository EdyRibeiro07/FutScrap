import requests
from bs4 import BeautifulSoup

headers = {
'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36"
}

def Scrap_DOM(id_):
	url = "https://www.espn.com.br/futebol/comentario/_/jogoId/" + str(id_)
   

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        print("Requisição bem-sucedida com sessão!")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Código de status: {e.response.status_code}")

        dom = BeautifulSoup(response.text, 'html.parser')

    return dom