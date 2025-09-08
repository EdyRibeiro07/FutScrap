from bs4 import BeautifulSoup
import copy

def Scrap_IDS(list_doms:list):
    list_ids = []

    for dom in list_doms:
        
        body = dom.find('body')        
        script = body.find('script')
        dom_text = script.text
        text_split = dom_text.split('/futebol/partida-estatisticas/_/jogoId/')        
        count_t =  len(text_split)
              
        for i in range(1, count_t):

            a = text_split[i].find('"')
            id_ = text_split[i][0:a]
            list_ids.append(copy.copy(id_))

    print(list_ids)
    print("*****************************")  
    print("*****************************")  
    print(f"{len(list_ids)} IDS ENCONTRADOS")     
    print("*****************************")      
    print("*****************************")  

    return list_ids