from bs4 import BeautifulSoup
from copy import copy

# Importações Locais
#Teste Git





def Get_Elements(list_doms:list):

    thelist = []
    list_ = []
    
    for dom in list_doms:
        element_tour = dom.find('span', class_ ='XSdof')
        list_teams = dom.find_all('span', class_ = 'NMnSM') 
        info = dom.find('div', class_="ContentList")        
        
        location = info.find("div", class_="Weather__Item--location")
        date = info.find("div", class_="GameInfo__Meta")        
        stadium = info.find("div", class_="GameInfo__Location")
        public_element = info.find("div", class_="Attendance__Numbers")
        public03 = public_element.get_text(strip=True)
        public02 = public03.replace("Público:", "")
        public = public02.replace(",", "")
        
        
        #APPENDS
        list_.append(copy(date.text))
        list_.append(copy(location))
        list_.append(copy(stadium.text))
        list_.append(copy(element_tour.text))
        list_.append(copy(list_teams[0].text))
        list_.append(copy(list_teams[1].text))
        list_.append(copy(public))
        thelist.append(copy(list_))
        print(f"{date.text} - {location.text} / {stadium.text} - {element_tour.text} - {list_teams[0].text} VS {list_teams[1].text} - {public}")
        list_.clear()
    
    return thelist