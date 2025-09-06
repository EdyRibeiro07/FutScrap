import requests
from bs4 import BeautifulSoup


def Find_Elements(list_doms:list):
    
    for dom in list_doms:
        list_elements = dom.find_all('span', class_ = 'NMnSM') 
        print(f"{list_elements[0].text} VS {list_elements[1].text}")

    