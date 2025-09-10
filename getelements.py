from bs4 import BeautifulSoup
from copy import copy

# Importações Locais

import treatthedate
import getcomments


def Get_Elements(list_doms:list):

    thelist = []
    list_ = []
   
    
    for dom in list_doms:
        element_tour = dom.find('span', class_ ='XSdof')
        list_teams = dom.find_all('span', class_ = 'NMnSM') 
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

        for element in comments_elements:
            comment = getcomments.Get_Comments(element)
            print(comment)
        
        
        #APPENDS
        list_.append(copy(date))
        list_.append(copy(city))
        list_.append(copy(country))
        list_.append(copy(stadium.text))
        list_.append(copy(element_tour.text))
        list_.append(copy(list_teams[0].text))
        list_.append(copy(list_teams[1].text))
        list_.append(copy(public_03))
        thelist.append(copy(list_))

        print(f"{date} - {city}, {country} / {stadium.text} - {element_tour.text} - {list_teams[0].text} VS {list_teams[1].text} - {public_03}")
        
        list_.clear()
    
    return thelist