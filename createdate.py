list_date = []

def Create_Date():
    
    start = int(input("Digite a data de início: "))
    end = int(input("Digite a data de final: "))
    
    for i in range(start, end + 1):
        list_date.append(i)
    
    print("**********LISTA DE DATAS CRIADAS")
    return list_date