import requests
from bs4 import BeautifulSoup

# Importações Locais



import options

thelist = []
thelist = options.Options()






    
    
   
    
# elementos = dom.find_all('div', class_='MatchCommentary__Comment')


# tempo = 2

# for elemento in elementos:

    

    # minuto_tag = elemento.find(class_ = "MatchCommentary__Comment__Timestamp")
    # evento_base = elemento.find("svg", class_ = "MatchCommentary__Comment__PlayIcon__Icon")
    # narracao_base = elemento.find("div", class_ = "MatchCommentary__Comment__GameDetails")
    # narracao = narracao_base.text if narracao_base else None
    # if minuto_tag and evento_base:
        # minuto_text = minuto_tag.text
        # minuto_sem = minuto_text.replace("'", "")

        # if "+" in minuto_sem:
            # minuto_separado = minuto_sem.split("+")

        # if len(minuto_separado) > 1:
            # minuto_separado[0] =  int(minuto_separado[0])
            # minuto_separado[1] =  int(minuto_separado[1])
        # else:
            # minuto_separado[0] =  int(minuto_separado[0])


        # minuto = minuto_separado[0]+ minuto_separado[1]

        # evento = evento_base.get("aria-label") # Usar .get() é mais seguro, pois retorna None se o atributo não existir
        
        # if evento == "Intervalo":
            # tempo = tempo - 1

        # print(f"Minuto: {minuto} Tempo {tempo}")
        # print(f"Evento: {evento}")
        # print(f"Narração: {narracao}")
    # else:
        # # Opcional: Imprima uma mensagem se algum elemento não for encontrado para depuração
        # if not minuto_tag:
            # print("Aviso: Tag de minuto não encontrada para este elemento.")
        # if not evento_base:
            # print("Aviso: Tag de evento (svg) não encontrada para este elemento.")
