import requests
from bs4 import BeautifulSoup
import copy



headers = {
'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36"
}


def Scrap_DOM(url_, list_, stage_):    

    count = 1
    
    list_doms = []
    
    print("**********INICIADO CONEXÃO")
    
    for i in list_:
        
        url = url_ + str(i) 
        
        try:

            if stage_ == 1:

                print("RASPAGEM DE PÁGINAS DE DATAS")
                response = requests.get(url, timeout=20, headers=headers)
                print(f"{count} REQUISIÇÃO BEM SUCEDIDA!")
                response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
                dom = BeautifulSoup(response.text, 'html.parser')
                list_doms.append(copy.copy(dom))
                print("**DOM RASPADO COM SUCESSO**")

            if stage_ == 2:

                print("RASPAGEM DE PÁGINAS DE COMENTÁRIOS")
                element_tour = None

                while element_tour == None:

                    response = requests.get(url, timeout=20, headers=headers)
                    response.raise_for_status()  # Verifica se a requisição foi bem-sucedida 
                    dom = BeautifulSoup(response.text, 'html.parser')
                    element_tour = dom.find('span', class_ ='XSdof')

                print(f"{count} REQUISIÇÃO BEM SUCEDIDA!")
                list_doms.append(copy.copy(dom))
                print("**********DOM RASPADO COM SUCESSO")

        except requests.exceptions.RequestException as e:
            
            print(f"ERRO AO FAZER REQUISIÇÃO: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Código de status: {e.response.status_code}")
                
        
        print("---------------------------------")
        count = count + 1         
        
    return list_doms   