def Get_Comments(element):    

    minute_01 = element.find('div', class_ = 'MatchCommentary__Comment__Timestamp')   
    event_01 = element.find('svg', class_ = 'MatchCommentary__Comment__PlayIcon__Icon icon__svg')
    print(event_01)
    if event_01['aria-label']:
        event_02 = event_01['aria-label']
    else:
        event_02 = None

    comment_01 = element.find('div', class_ = 'MatchCommentary__Comment__GameDetails')

    print(minute_01)
    print(event_02)
    print(comment_01)
    
    