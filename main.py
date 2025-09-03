from selenium import webdriver
from selenium.webdriver.common.by import By
import copy

lista_id_jogos = []
lista_elementos = []
lista_links =[]


def Create_Driver(data_start, data_end):

    data_start = data_start
    data_end = data_end

    driver = webdriver.Chrome()

    for data in range(data_start, (data_end + 1)):

        print(data)

        driver.get(f"https://www.espn.com.br/futebol/resultados/_/data/{str(data)}")

        Get_Links(driver)

    driver.quit()
    

def Get_Links(driver):

    driver = driver

    lista_elementos = driver.find_elements(By.LINK_TEXT, "Resumo")

    for i in lista_elementos:
        lista_links.append(i.get_attribute("href"))
    for i in lista_links:
        link_quebrado = i.split('/')   
        print(f"Link Quebrado {link_quebrado}")
        lista_id_jogos.append(link_quebrado[-2])
    
    print(lista_id_jogos)
    

def Get_Comentarios():

    driver = webdriver.Chrome()

    for i in lista_id_jogos:
        driver.get(f"https://www.espn.com.br/futebol/comentario/_/jogoId/{str(i)}")
    driver.quit()




print("Abaixo Informe o Peródo de Raspagem. Modelo da Data: 20250831 ")
print("O Período Deve ser Dentro do Intervalo de um Mesmo Mês ")

data_start = int(input("Digite a Data Inícial do Período: "))
data_end = int(input("Digite a Data Final do Período: "))

Create_Driver(data_start, data_end)
Get_Comentarios()