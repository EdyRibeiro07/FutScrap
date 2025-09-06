import requests
from bs4 import BeautifulSoup
import copy



headers = {
'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36"
}


def Scrap_DOM(url_, list_):
    
    list_doms = []
    
    print("**********INICIADO CONEXÃO")
    
    for i in list_:
        
        url = url_ + str(i) 
        
        try:
            
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
            print("Requisição bem-sucedida com sessão!")

            dom = BeautifulSoup(response.text, 'html.parser')
            
            list_doms.append(copy.copy(dom))
            

        except requests.exceptions.RequestException as e:
            
            print(f"Erro ao fazer a requisição: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Código de status: {e.response.status_code}")
                
        print("**********DOM RASPADO COM SUCESSO")         
        
    return list_doms   