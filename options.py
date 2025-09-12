import os
import subprocess
import time

#Importações Locais

import createdate
import scrapdom
import getelements
import scrapids


opts = ["1", "2"]
opt = None

def Options():
    
    url_id = "https://www.espn.com.br/futebol/comentario/_/jogoId/"
    url_date = "https://www.espn.com.br/futebol/resultados/_/data/"

    os.system('cls')
    subprocess.run('clear')
    
    print("----------DIGITE A OPÇÃO QUE DESEJA----------")
    print("[1] - RASPAGEM DE DADOS / ATUALIZAR A DATABASE")
    print("[2] - UTILIAZR O SITEMA DE ESTATISTICAS, CHRATOS")
    
    opt = str(input("::: "))    
            
        
    if opt == "1":
        os.system('cls')
        subprocess.run('clear')
        list_date = createdate.Create_Date()
        list_doms = scrapdom.Scrap_DOM(url_date, list_date, 1) 
        list_ids = scrapids.Scrap_IDS(list_doms)
        list_doms = scrapdom.Scrap_DOM(url_id, list_ids, 2)       

        getelements.Get_Elements(list_doms) 
        print("DIGITE UM ARGUMENTO VÁLIDO !")
        time.sleep(3)
        Options()

 
    
    