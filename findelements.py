import requests
from bs4 import BeautifulSoup

def Find_Elements(dom, tag, att, text ):
	if att == "class":
        lista_elementos = dom.find_all(tag, class_ = text)
        print("ok")