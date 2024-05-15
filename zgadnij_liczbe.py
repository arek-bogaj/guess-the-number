import random
min = 1
max = 10
diff_label = ""


# Funkcja odpowiedzialna za poziom trudności
def choose_difficulty():
    print()
    print(">>> >>> Wybierz poziom trudności <<< <<<")

    global max

    while True:
        d = input("[ ł - ŁATWY | ś - ŚREDNI | t - TRUDNY ]: ")
        if d == "ł":
            max = 10
            break
        elif d == "ś":
            max = 100
            break
        elif d == "t":
            max = 1000
            break
        else:
            pass


# Główna funkcja
def main():
    # Wybieranie poziomu trudności
    choose_difficulty()

    # Generowanie losowej liczby i zerowanie licznika podjętych prób
    numer = random.randrange(min, max+1)
    numb_of_attempts = 1
    print()
    print(f"Mam na myśli pewną liczbę z przedziału: {min} - {max}. Spróbuj ją odgadnąć :)")

    # Pętla, sprawdza czy wprowadzono text czy liczbę i czy input zgadza się wygenerowaną liczbą
    while True:
        i = input(": ")
        if i.isdigit():
            i = int(i)
            if i < min or i > max:
                print("Liczba spoza przedziału!")
            elif i > numer:
                numb_of_attempts += 1
                print("<<< Za duża! Spóbuj ponownie.")
            elif i < numer:
                numb_of_attempts += 1
                print(">>> Za mała! Spóbuj ponownie.")

            # Input zgodny z wygenerowaną liczbą
            else:
                print()
                print(f"BRAWO! Miałem na myśli liczbę {numer} :)")
                print(f"Udało ci się za {numb_of_attempts} razem.")
                print()

                # Pętla, sprawdza czy wprowadzono poprawne dane
                while True:
                    i = input("Chcesz zagrać ponownie? [ t - TAK | n - NIE ] ")
                    if i == "t":
                        main()
                    elif i == "n":
                        exit()
                    else:
                        pass

        # Niedozwolony input, cofa na początek pętli
        else:
            print("To nie jest liczba :(")


# Start programu
print("---- Z G A D N I J ---- L I C Z B Ę ----")
main()