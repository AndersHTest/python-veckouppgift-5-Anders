from vowels import *

def menu_my_app():
    active = True
    while active:
        print(f"\n1. Räkna antal vokaler ")
        print(f"2.")
        print(f"3.")
        print(f"4.")
        print(f"5.")
        print(f"\n0 - Avsluta\n")

        control = input("\nSelect an option: ")

        if control == "0":
            active = False

        elif control == "1":

            input_vowel_count = input(f"Skriv ett ord eller en mening: ")
            print(f"Det finns {count_vowels(input_vowel_count)} vokal(er) i strängen: \"{input_vowel_count}\".\n")
