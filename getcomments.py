def Get_Comments(element, team_home, team_visit):    
    home_fouls_first_time = []
    visit_fouls_first_time = []

    elements = element.find_all('div', class_ = 'MatchCommentary__Comment')

    
    for e in elements:
        
        minute_element = e.find('div', class_ = 'MatchCommentary__Comment__Timestamp')  
        minute_01 = minute_element.text.strip()
        minute_02 = minute_01.replace("'", "")
        if minute_02 != "-" and minute_02 != "":
            minute_03 = int(eval(minute_02))




        comment_01 = e.find('div', class_ = 'MatchCommentary__Comment__GameDetails')
        comment_01 = comment_01.text.upper()

        if "FALTA COMETIDA" in comment_01:
            if team_home.upper() in comment_01:
                home_fouls_first_time.append(minute_03)
            if team_visit.upper() in comment_01:
                visit_fouls_first_time.append(minute_03)


        print(comment_01.strip())
        print("-----------------------------------")
    
    print(home_fouls_first_time, visit_fouls_first_time)