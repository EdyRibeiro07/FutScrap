from bs4 import BeautifulSoup
import copy

def Scrap_IDS(list_doms:list):
    list_ids = []
    list_ = []
    
    for dom in list_doms:
        
        body = dom.find('body')
        tour = body.find('span', class_="mLASH")
        script = body.find('script')
        dom_text = script.text
        text_split = dom_text.split('/futebol/partida-estatisticas/_/jogoId/')        
        count_t =  len(text_split)
        list_.append(copy.copy(tour))
        
        for i in range(1, count_t):

            a = text_split[i].find('"')
            id_ = text_split[i][0:a]
            list_.append(copy.copy(id_))
        list_ids.append(copy.copy(list_))
        list_.clear()

    print(list_ids)
    return list_ids