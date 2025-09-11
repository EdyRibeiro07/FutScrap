def Get_Comments(element, team_home, team_visit):    
    home_fouls = []
    visit_fouls = []

    elements = element.find_all('div', class_ = 'MatchCommentary__Comment')

    
    for e in elements:
        
        minute_element = e.find('div', class_ = 'MatchCommentary__Comment__Timestamp')  
        minute_01 = minute_element.text.strip()
        minute_02 = minute_01.replace("'", "")
        minute_03 = minute_02.split("+")
        for m in minute_03:
            a = m
            if m != '-':
                a =+ int(m)
        print(a)



        comment_01 = e.find('div', class_ = 'MatchCommentary__Comment__GameDetails')
        comment_01 = comment_01.text.upper()

        if "FALTA COMETIDA" in comment_01:
            if team_home.upper() in comment_01:
                home_fouls.append(minute_element.text.strip())
            if team_visit.upper() in comment_01:
                visit_fouls.append(minute_element.text.strip())


        print(comment_01.strip())
        print("-----------------------------------")
    
    print(home_fouls, visit_fouls)