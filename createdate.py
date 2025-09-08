list_date = []

def Create_Date():
    
    start = int(input("DIGITE A DATA DE INÍCIO: "))
    end = int(input("DIGITE A DATA FINAL: "))
    
    for i in range(start, end+1):
        list_date.append(i)
    
    print("*****LISTA DE DATAS CRIADAS*****")
    return list_date