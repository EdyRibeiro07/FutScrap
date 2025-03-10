import requests
from bs4 import BeautifulSoup

start_id_game = 704538
end_id_game = start_id_game + 11

base_dados = []
lista_eventos = []

evento = None
equipe = None
monento = None


for i in range(start_id_game, end_id_game):
    url = 'https://www.espn.com.br/futebol/comentario/_/jogoId/' + str(i)
    
    tempo = "2ºT"

    #Simulador de requisição do Navegador
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)

    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Parse do conteúdo da página
        html = BeautifulSoup(response.text, 'html.parser')        
     
        divs_comentario = html.find_all('div', class_="MatchCommentary__Comment")
        
        equipes = html.find_all('h2', class_="ScoreCell__TeamName ScoreCell__TeamName--displayName db")
        equipes[0] = equipes[0].text
        equipes[1] = equipes[1].text
        
        for div in divs_comentario:
            for sub_div in div:       
                
                if sub_div.get('class') == ['MatchCommentary__Comment__Timestamp']:
                    span = sub_div.find('span')
                    if span:                        
                        momento = span.text                          
                
                        
                if sub_div.get('class') == ['MatchCommentary__Comment__GameDetails']:
                    span = sub_div.find('span')
                    texto = span.text
                    if equipes:    
                        if str(f"({equipes[0]})") in texto:
                            equipe = equipes[0]                            
                        if str(f"({equipes[1]})") in texto:
                            equipe = equipes[1]
                    if span:                        
                        if "Falta cometida" in span.text:
                            evento = "Falta"
                        if "sofre uma falta" in span.text or "Fim do primeiro tempo" in span.text or "Fim do jogo" in span.text or "Início do primeiro tempo" in span.text or "Escalações" in span.text or "Partida interrompida" in span.text or "Partida recomeça" in span.text:
                            evento = None
                            momento = None
                            equipe = None
                        if "Substituição" in span.text:
                            evento = "Substituição"
                        if "Finalização bloqueada" in span.text:
                            evento = "Finalização bloqueada"
                        if "Impedimento" in span.text:
                            evento = "Impedimento"
                        if "Gol" in span.text:
                            evento = "Gol"
                        if "Fim do primeiro tempo" in span.text:
                            tempo = "1ºT"
                        if "Oportunidade perdida" in span.text:
                            evento = "Finalização pra Fora"
               
            if evento != None:          
                print(f"{tempo} / {momento} / {equipe} / {evento}")     
                print("********************************************")
                        
                        
                       

   
    else:
        print('Erro ao acessar a página:', response.status_code)
