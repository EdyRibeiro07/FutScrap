from copy import copy
from bs4 import BeautifulSoup

def Get_Comments(element, team_home, team_visit):    
    fouls = []
    conner = []
    shots_block = []
    lost_opportunuty = []
    kick_saved = []
    offside = []

    home_fouls_first_time = []
    visit_fouls_first_time = []
    home_fouls_second_time = []
    visit_fouls_second_time = []

    home_conner_first_time = []
    visit_conner_first_time = []
    home_conner_second_time = []
    visit_conner_second_time = []

    home_kick_block_first_time = []
    visit_kick_block_first_time = []
    home_kick_block_second_time = []
    visit_kick_block_second_time = []

    home_lost_opportunity_first_time = []
    visit_lost_opportunity_first_time = []
    home_lost_opportunity_second_time = []
    visit_lost_opportunity_second_time = []

    home_kick_saved_first_time = []
    visit_kick_saved_first_time = []
    home_kick_saved_second_time = []
    visit_kick_saved_second_time = []

    home_offside_first_time = []
    visit_offside_first_time = []
    home_offside_second_time = []
    visit_offside_second_time = []  


    elements = element.find_all('div', class_ = 'MatchCommentary__Comment')

    
    
    for e in elements:
        time = 2  ### 1 = 1º tempo /// 2 = 2º tempo
        minute_element = e.find('div', class_ = 'MatchCommentary__Comment__Timestamp')  
        minute_01 = minute_element.text.strip()
        minute_02 = minute_01.replace("'", "")  
        if minute_02 != "-" and minute_02 != "":
            minute_03 = int(eval(minute_02))


        comment_01 = e.find('div', class_ = 'MatchCommentary__Comment__GameDetails')
        comment_01 = comment_01.text.upper()

        if "FALTA COMETIDA" in comment_01:

            if minute_03 < 75 and time == 2:

                if "+" in minute_02 and time == 2:
                    time = 1

                if team_home.upper() in comment_01:

                    home_fouls_first_time.append(minute_03)

                if team_visit.upper() in comment_01:

                    visit_fouls_first_time.append(minute_03)

            if minute_03 > 45 and time == 2: 
                
                if team_home.upper() in comment_01:

                    home_fouls_second_time.append(minute_03)

                if team_visit.upper() in comment_01:

                    visit_fouls_second_time.append(minute_03)

        if "ESCANTEIO" in comment_01:

            if minute_03 < 75 and time == 2:

                if "+" in minute_02 and time == 2:
                    time = 1

                if team_home.upper() in comment_01:

                    home_conner_first_time.append(minute_03)

                if team_visit.upper() in comment_01:

                    visit_conner_first_time.append(minute_03)

            if minute_03 > 45 and time == 2: 
                
                if team_home.upper() in comment_01:

                    home_conner_second_time.append(minute_03)

                if team_visit.upper() in comment_01:

                    visit_conner_second_time.append(minute_03)

        if "FINALIZAÇÃO BLOQUEADA" in comment_01:


            if minute_03 < 75 and time == 2:

                if "+" in minute_02 and time == 2:
                    time = 1

                if team_home.upper() in comment_01:

                    home_kick_block_first_time.append(minute_03)

                if team_visit.upper() in comment_01:

                    visit_kick_block_first_time.append(minute_03)

            if minute_03 > 45 and time == 2: 
                
                if team_home.upper() in comment_01:

                    home_kick_block_second_time.append(minute_03)

                if team_visit.upper() in comment_01:

                    visit_kick_block_second_time.append(minute_03)

        if "OPORTUNIDADE PERDIDA" in comment_01:


            if minute_03 < 75 and time == 2:

                if "+" in minute_02 and time == 2:
                    time = 1

                if team_home.upper() in comment_01:

                    home_lost_opportunity_first_time.append(minute_03)

                if team_visit.upper() in comment_01:

                    visit_lost_opportunity_first_time.append(minute_03)

            if minute_03 > 45 and time == 2: 
                
                if team_home.upper() in comment_01:

                    home_lost_opportunity_second_time.append(minute_03)

                if team_visit.upper() in comment_01:

                    visit_lost_opportunity_second_time.append(minute_03)

        if "FINALIZAÇÃO DEFENDIDA" in comment_01:

            if minute_03 < 75 and time == 2:

                if "+" in minute_02 and time == 2:
                    time = 1

                if team_home.upper() in comment_01:

                    home_kick_saved_first_time.append(minute_03)

                if team_visit.upper() in comment_01:

                    visit_kick_saved_first_time.append(minute_03)

            if minute_03 > 45 and time == 2: 
                
                if team_home.upper() in comment_01:

                    home_kick_saved_second_time.append(minute_03)

                if team_visit.upper() in comment_01:

                    visit_kick_saved_second_time.append(minute_03)

        if "IMPEDIMENTO" in comment_01:

            if minute_03 < 75 and time == 2:

                if "+" in minute_02 and time == 2:
                    time = 1

                if team_home.upper() in comment_01:

                    home_offside_first_time.append(minute_03)

                if team_visit.upper() in comment_01:

                    visit_offside_first_time.append(minute_03)

            if minute_03 > 45 and time == 2: 
                
                if team_home.upper() in comment_01:

                    home_offside_second_time.append(minute_03)

                if team_visit.upper() in comment_01:

                    visit_offside_second_time.append(minute_03)

       
        
        
        
        
        
        
        # APPENDS
    
    
    fouls.append(copy(home_fouls_first_time))
    fouls.append(copy(home_fouls_second_time))
    fouls.append(copy(visit_fouls_first_time))
    fouls.append(copy(visit_fouls_second_time))

    conner.append(copy(home_conner_first_time))
    conner.append(copy(home_conner_second_time))
    conner.append(copy(visit_conner_first_time))
    conner.append(copy(visit_conner_second_time))

    shots_block.append(copy(home_kick_block_first_time))
    shots_block.append(copy(home_kick_block_second_time))
    shots_block.append(copy(visit_kick_block_first_time))
    shots_block.append(copy(visit_kick_block_second_time))

    lost_opportunuty.append(copy(home_lost_opportunity_first_time))
    lost_opportunuty.append(copy(home_lost_opportunity_second_time))
    lost_opportunuty.append(copy(visit_lost_opportunity_first_time))
    lost_opportunuty.append(copy(visit_lost_opportunity_second_time))

    kick_saved.append(copy(home_kick_saved_first_time))
    kick_saved.append(copy(home_kick_saved_second_time))
    kick_saved.append(copy(visit_kick_saved_first_time))
    kick_saved.append(copy(visit_kick_saved_second_time))

    offside.append(copy(home_offside_first_time))
    offside.append(copy(home_offside_second_time))
    offside.append(copy(visit_offside_first_time))  
    offside.append(copy(visit_offside_second_time))

    return fouls, conner, shots_block, lost_opportunuty, kick_saved, offside




        
