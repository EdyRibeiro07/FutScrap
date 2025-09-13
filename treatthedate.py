def Treat_The_Date(date_element):

    zero = "0"

    text_01 = date_element.text.strip()
    text_02 = text_01[6:]
    
    if "janeiro" in text_02:
        text_03 = text_02.replace("janeiro", "01")
    elif "fevereiro" in text_02:
        text_03 = text_02.replace("fevereiro", "02")
    elif "março" in text_02:
        text_03 = text_02.replace("março", "03")
    elif "abril" in text_02:
        text_03 = text_02.replace("abril", "04")
    elif "maio" in text_02:
        text_03 = text_02.replace("maio", "05")
    elif "junho" in text_02:
        text_03 = text_02.replace("junho", "06")
    elif "julho" in text_02:
        text_03 = text_02.replace("julho", "07")
    elif "agosto" in text_02:
        text_03 = text_02.replace("agosto", "08")
    elif "setembro" in text_02:
        text_03 = text_02.replace("setembro", "09")
    elif "outubro" in text_02:
        text_03 = text_02.replace("outubro", "10")
    elif "novembro" in text_02:
        text_03 = text_02.replace("novembro", "11")
    elif "dezembro" in text_02:
        text_03 = text_02.replace("dezembro", "12")
    else:
        text_03 = ("MÊS NÃO IDENTIFICADO")


    text_04 = text_03.replace("-", "")
    text_05 = text_04.replace(",", "")
    text_06 = text_05.replace("de", "")
    text_07 = text_06.replace(" ", "")


    count_text_07 = len(text_07.strip())
 
    if count_text_07 <= 7:

        text_08 = zero + text_07.strip()
    else:

        text_08 =  text_07.strip()

    print("DATA TRATADA: ", text_08)

    return text_08