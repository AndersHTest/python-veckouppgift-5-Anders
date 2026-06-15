def balance_list(list_1, list_2):

    #Räkna ut längden på listorna för att se om de behöver balanseras
    length_1 = len(list_1)
    length_2 = len(list_2)

    #Balansera listorna om lista_1 är minst 2 element större än lista_2.
    if length_1 - length_2 >= 2:
        while len(list_1) - len(list_2) >= 2:
            list_2.append(list_1.pop())
        return list_1, list_2

    #Balansera listorna om lista_2 är minst 2 element större än lista_1.
    elif length_2 - length_1 >= 2:
        while len(list_2) - len(list_1) >= 2:
            list_1.append(list_2.pop())
        return list_1, list_2

    #Om antalet element i listorna är mindre än två ifrån varandra så gör vi ingen balansering.
    else:
        return list_1, list_2