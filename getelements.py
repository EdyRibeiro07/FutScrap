from bs4 import BeautifulSoup
from copy import copy

# Importações Locais

import treatthedate



def Get_Elements(list_doms:list):

    thelist = []
    list_ = []
   
    
    for dom in list_doms:
        element_tour = dom.find('span', class_ ='XSdof')
        list_teams = dom.find_all('span', class_ = 'NMnSM') 
        info = dom.find('div', class_="ContentList")        
        
        location = info.find("div", class_="Weather__Item--location")
        date_element = info.find("div", class_="GameInfo__Meta") 
        date = treatthedate.Treat_The_Date(date_element)       
        stadium = info.find("div", class_="GameInfo__Location")

        if info.find("div", class_="Attendance__Numbers"):
            public_element = info.find("div", class_="Attendance__Numbers")
            print(public_element)
        else:
            public_element = BeautifulSoup('<div class="Attendance__Numbers">Público<!-- -->: <!-- -->Não Divulgado</div>', 'html.parser')

        public_01 = public_element.get_text(strip=True)
        public_02 = public_01.replace("Público:", "")
        public_03 = public_02.replace(",", "")
        
        
        #APPENDS
        list_.append(copy(date))
        list_.append(copy(location))
        list_.append(copy(stadium.text))
        list_.append(copy(element_tour.text))
        list_.append(copy(list_teams[0].text))
        list_.append(copy(list_teams[1].text))
        list_.append(copy(public_03))
        thelist.append(copy(list_))
        print(f"{date} - {location.text} / {stadium.text} - {element_tour.text} - {list_teams[0].text} VS {list_teams[1].text} - {public_03}")
        list_.clear()
    
    return thelist