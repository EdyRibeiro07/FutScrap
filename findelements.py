import requests
from bs4 import BeautifulSoup

def Find_Elementos(dom, tag, class_, text ):
	lista_elementos = dom.find_all(tag, class_ = text)
    print("ok")