from selenium import webdriver
from selenium.webdriver.common.by import By
import copy
import varlis


lista_id_jogos = []
lista_elementos = []
lista_elementos_comemtarios = []
lista_links =[]
lista_iddata = []
n = 0

def Create_Driver(data_start, data_end):

    data_start = data_start
    data_end = data_end

    driver = webdriver.Chrome()

    for data in range(data_start, (data_end + 1)):

        print(f"Coferindo os jogos do dia {data}")               

        driver.get(f"https://www.espn.com.br/futebol/resultados/_/data/{str(data)}")    

        lista_elementos = driver.find_elements(By.LINK_TEXT, "Resumo")

        print("------------------------------------------------------")
        print(f"Quantidade de elementos em lista_elementos{len(lista_elementos)}")
        for elemento in lista_elementos:
            print(f"--Capturando os links dos jogos do dia {data}")
            lista_links.append(elemento.get_attribute("href"))       
                
        print("------------------------------------------------------") 
        print(f"Quantidade de links em lista_links{len(lista_links)}")
        for link in lista_links:
            print(f"----Corrigindo links dos jogos")
            link_quebrado = link.split('/')   
            lista_iddata.append(link_quebrado[-2])
            lista_iddata.append(data)
            print(f"---- Salvando na Lista de IDs a ID {lista_iddata[0]}")
            print(f"---- Salvando na Lista de IDs a Data {lista_iddata[1]}")
            lista_id_jogos.append(copy.copy(lista_iddata))      
            
            lista_iddata.clear()
        
        lista_elementos.clear()
        lista_links.clear()
        
            
           
    print(lista_id_jogos)    
    
    driver.quit()
    
    
    
def Get_Comentarios():
    
    global lista_elementos_comemtarios
    driver = webdriver.Chrome()

    for i in lista_id_jogos:
        driver.get(f"https://www.espn.com.br/futebol/comentario/_/jogoId/{str(i[0])}")
        elementos_comentarios = driver.find_elements(By.CLASS_NAME, "Table__TR--sm")
        lista_elementos_comemtarios.append(copy.copy(elementos_comentarios))
        elementos_comentarios.clear()
    driver.quit()
    




print("Abaixo Informe o Peródo de Raspagem. Modelo da Data: 20250831 ")
print("O Período Deve ser Dentro do Intervalo de um Mesmo Mês ")

data_start = int(input("Digite a Data Inícial do Período: "))
data_end = int(input("Digite a Data Final do Período: "))

Create_Driver(data_start, data_end)
Get_Comentarios()