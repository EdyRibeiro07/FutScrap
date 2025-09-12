from copy import copy
from bs4 import BeautifulSoup

import dict_main

def Get_Comments(element, team_home, team_visit):    

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

            if minute_03 < 90 and time == 2 and "+" in minute_02:         
                 
    
                time = 1

                if team_home.upper() in comment_01:

                    home_offside_first_time.append(minute_03)

                if team_visit.upper() in comment_01:

                    visit_offside_first_time.append(minute_03)

            if minute_03 < 90 and time == 1 and "+" in minute_02:         
                 

                if team_home.upper() in comment_01:

                    home_offside_first_time.append(minute_03)

                if team_visit.upper() in comment_01:

                    visit_offside_first_time.append(minute_03)

            if minute_03 > 45 and time == 2: 
                
                if team_home.upper() in comment_01:

                    home_offside_second_time.append(minute_03)

                if team_visit.upper() in comment_01:

                    visit_offside_second_time.append(minute_03)

            if minute_03 <= 45 and time == 1: 
                
                if team_home.upper() in comment_01:

                    home_offside_first_time.append(minute_03)

                if team_visit.upper() in comment_01:

                    visit_offside_first_time.append(minute_03)

       
        
        
        
        
        
        
        # APPENDS


    dict_main.the_dict["fouls_home_first_time"].append(copy(home_fouls_first_time))
    dict_main.the_dict["fouls_home_second_time"].append(copy(home_fouls_second_time))
    dict_main.the_dict["fouls_visit_first_time"].append(copy(visit_fouls_first_time))
    dict_main.the_dict["fouls_visit_second_time"].append(copy(visit_fouls_second_time))

    dict_main.the_dict["conner_home_first_time"].append(copy(home_conner_first_time))
    dict_main.the_dict["conner_home_second_time"].append(copy(home_conner_second_time))
    dict_main.the_dict["conner_visit_first_time"].append(copy(visit_conner_first_time))
    dict_main.the_dict["conner_visit_second_time"].append(copy(visit_conner_second_time))

    dict_main.the_dict["shots_block_home_first_time"].append(copy(home_kick_block_first_time))
    dict_main.the_dict["shots_block_home_second_time"].append(copy(home_kick_block_second_time))
    dict_main.the_dict["shots_block_visit_first_time"].append(copy(visit_kick_block_first_time))
    dict_main.the_dict["shots_block_visit_second_time"].append(copy(visit_kick_block_second_time))

    dict_main.the_dict["lost_opportunity_home_first_time"].append(copy(home_lost_opportunity_first_time))
    dict_main.the_dict["lost_opportunity_home_second_time"].append(copy(home_lost_opportunity_second_time))
    dict_main.the_dict["lost_opportunity_visit_first_time"].append(copy(visit_lost_opportunity_first_time))
    dict_main.the_dict["lost_opportunity_visit_second_time"].append(copy(visit_lost_opportunity_second_time))

    dict_main.the_dict["kick_saved_home_first_time"].append(copy(home_kick_saved_first_time))
    dict_main.the_dict["kick_saved_home_second_time"].append(copy(home_kick_saved_second_time))
    dict_main.the_dict["kick_saved_visit_first_time"].append(copy(visit_kick_saved_first_time))
    dict_main.the_dict["kick_saved_visit_second_time"].append(copy(visit_kick_saved_second_time))

    dict_main.the_dict["offside_home_first_time"].append(copy(home_offside_first_time))
    dict_main.the_dict["offside_home_second_time"].append(copy(home_offside_second_time))
    dict_main.the_dict["offside_visit_first_time"].append(copy(visit_offside_first_time))
    dict_main.the_dict["offside_visit_second_time"].append(copy(visit_offside_second_time))


    home_fouls_first_time.clear()
    visit_fouls_first_time.clear()
    home_fouls_second_time.clear()
    visit_fouls_second_time.clear()         
    home_conner_first_time.clear()
    visit_conner_first_time.clear()
    home_conner_second_time.clear()
    visit_conner_second_time.clear()
    home_kick_block_first_time.clear()
    visit_kick_block_first_time.clear()
    home_kick_block_second_time.clear()
    visit_kick_block_second_time.clear()
    home_lost_opportunity_first_time.clear()
    visit_lost_opportunity_first_time.clear()
    home_lost_opportunity_second_time.clear()           
    visit_lost_opportunity_second_time.clear()
    home_kick_saved_first_time.clear()
    visit_kick_saved_first_time.clear()
    home_kick_saved_second_time.clear()
    visit_kick_saved_second_time.clear()
    home_offside_first_time.clear()
    visit_offside_first_time.clear()        
    home_offside_second_time.clear()
    visit_offside_second_time.clear()

