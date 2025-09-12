#ATENÇÃO AO PARAMENTRO DA FUNÇÃO QUE PARA FINS DE TESTES FOI ALTERADO
#TAMBEM FOI ALTERADO O ITEN DE INTERAÇÃO DO PRIMEIRO FOR DA FUNÇÃO


from bs4 import BeautifulSoup
from copy import copy

# Importações Locais

import treatthedate
import getcomments

list_temp = []

with open("html.md", "r") as arquivo_01:
    arquivo_02 =arquivo_01.read()
    arquivo_03 = BeautifulSoup(arquivo_02, "html.parser")
    list_temp.append(arquivo_03)



def Get_Elements(a): ### em produção o paramentro correto é "list_doms:list"

    
    thelist = []
    list_ = []
   
    
    for dom in a: ### em produção o paramentro correto é "list_doms"
        element_tour = dom.find('span', class_ ='XSdof')
        list_teams = dom.find_all('span', class_ = 'NMnSM') 
        team_home = list_teams[0].text.strip()
        team_visit = list_teams[1].text.strip()
        info = dom.find('div', class_="ContentList") 
        comments_elements = dom.find_all('div', class_ = 'MatchCommentary__Comment')       
        
        location_element = info.find("div", class_="Weather__Item--location")
        location_text = location_element.get_text(strip=True)
        city, country = [t.strip() for t in location_text.split(",")]

        date_element = info.find("div", class_="GameInfo__Meta") 
        date = treatthedate.Treat_The_Date(date_element)       
        stadium = info.find("div", class_="GameInfo__Location")

        if info.find("div", class_="Attendance__Numbers"):
            public_element = info.find("div", class_="Attendance__Numbers")

        else:
            public_element = BeautifulSoup('<div class="Attendance__Numbers">Público<!-- -->: <!-- -->Não Divulgado</div>', 'html.parser')

        public_01 = public_element.get_text(strip=True)
        public_02 = public_01.replace("Público:", "")
        public_03 = public_02.replace(",", "")

        #SCRAP COMENTS:::

        for element in list_temp: # PARÂMETRO ORIGINAL DO FOR 'comments_elements'
            comment = getcomments.Get_Comments(element, team_home, team_visit) 
            print(comment)
 
        
        
        #APPENDS
        list_.append(copy(date.strip()))
        list_.append(copy(city.strip()))
        list_.append(copy(country.strip()))
        list_.append(copy(stadium.text.strip()))
        list_.append(copy(element_tour.text.strip()))
        list_.append(copy(team_home))
        list_.append(copy(team_visit))
        list_.append(copy(public_03.strip()))
        thelist.append(copy(list_))

        for i in thelist:
            print("")
            print(i)
        
        list_.clear()
    
    return thelist