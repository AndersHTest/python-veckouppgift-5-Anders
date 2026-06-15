from vowels import *
from find_max_value import *
from list import *
from Temperatur import *
from count_words import count_words
from median import find_median
from multiplication import multiplication_table
from balance_list import balance_list

def menu_my_app():
    active = True
    while active:
        print(f"\n1. Summera lista")
        print(f"2. Räkna antal vokaler")
        print(f"3. Hitta största värdet")
        print(f"4. Hitta näst största värdet")
        print(f"5. Temperaturomvandling (C->F)")
        print(f"6. Räkna ord")
        print(f"7. Hitta median eller medelvärde")
        print(f"8. Multiplikationstabell")
        print(f"9. Balansera listor")
        print(f"\n0 - Avsluta\n")

        control = input("\nSelect an option: ")

        if control == "0":
            active = False

        elif control == "1":
            x = [1, 2, 3, 4, 5]
            y = []

            print(f"Listan {x} summeras till {sum_list(x)}.")
            print(f"Listan {y} summeras till {sum_list(y)}.")

        elif control == "2":

            input_vowel_count = input(f"Skriv ett ord eller en mening: ")
            print(f"Det finns {count_vowels(input_vowel_count)} vokal(er) i strängen: \"{input_vowel_count}\".\n")

        elif control == "3":
            test_find_1 = [1, 2, 3, 4, 5, 9]
            print(f"Det största talet är {find_max(test_find_1)} i listan {test_find_1}.\n ")
            print(f"{find_max([])}")

        elif control == "4":
            test_find_1 = [1, 2, 3, 4, 5, 9]
            test_find_2 = []
            print(f"\nI listan {test_find_1} är det näst största talet '{find_2nd_max(test_find_1)}'.\n ")
            print(f"I listan {test_find_2} är det näst största talet '{find_max(test_find_2)}'.\n ")

        elif control == "5":
            x = float(input("Skriv en temperatur i grader Celsius för att konvertera till Fahrenheit: "))
            print(c_to_f(x))

        elif control == "6":
            sentence = input("Räkna antalet ord i en mening: ")
            print(f"Antalet ord är: {count_words(sentence)}.")

        elif control == "7":
            print(f"Ojämn lista. Vi kollar det mellersta talet i listan [1, 2, 3, 4, 5]. Svar: {find_median([1, 2, 3, 4, 5])}")
            print(f"Jämn lista. Vi kollar medelvärdet på de två mellersta (i sorterad lista) talen i listan [4, 5, 6, 7, 3, 2]. Svar: {find_median([4, 5, 6, 7, 3, 2])}")

        elif control == "8":
            print(multiplication_table(int(input("Skriv in ett heltal för vilken tabell du vill räkna på: ")), (int(input("Skriv in ett heltal för hur långt vi ska räkna: ")))))

        elif control == "9":
            x_list = [1, 2, 3, 4, 5]
            y_list = [4, 5, 6, 7, 3, 2]

            r_list = [1, 2, 3, 4]
            s_list = [4, 5, 6, 7, 3, 2]

            print(f"1. Vi skickar listorna [1, 2, 3, 4, 5] och [4, 5, 6, 7, 3, 2]. Förväntat resultat är; ingen åtgärd. Resultat: {balance_list(x_list, y_list)}")
            print(f"2. Vi skickar listorna [1, 2, 3, 4] och [4, 5, 6, 7, 3, 2]. Förväntat resultat är att listorna har balanserats. Resultat: {balance_list(x_list, y_list)}")
