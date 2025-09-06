import os
import time

#Importações Locais

import createdate
import scrapdom
import findelements
import scrapids

url_id = "https://www.espn.com.br/futebol/comentario/_/jogoId/"
url_date = "https://www.espn.com.br/futebol/resultados/_/data/"


opts = [1, 2]
opt = None

def Options():

    os.system('cls')
    
    print("----------DIGITE A OPÇÃO QUE DESEJA----------")
    print("1 - RASPAGEM DE DADOS / ATUALIZAR A DATABASE")
    print("2 - UTILIAZR O SITEMA DE ESTATISTICAS, CHRATOS")
    
    opt = int(input("::: "))
    
    if opt in opts:
        
        if opt == 1:
            list_date = createdate.Create_Date()
            list_doms = scrapdom.Scrap_DOM(url_date, list_date) 
            list_ids = scrapids.Scrap_IDS(list_doms)
            list_doms = scrapdom.Scrap_DOM(url_id, list_ids)
            findelements.Find_Elements(list_doms)
        else:
            pass

    else:
        print("DIGITE UM ARGUMENTO VÁLIDO !")
        time.sleep(3)
        Options()
        
        
    
    