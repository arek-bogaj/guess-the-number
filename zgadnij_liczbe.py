import random
min = 1
max = 100


# Główna funkcja
def main():
    # Generowanie losowej liczby i zerowanie licznika podjętych prób
    numer = random.randrange(min, max+1)
    numb_of_attempts = 1
    print()
    print(f"Mam na myśli pewną liczbę z przedziału: {min} - {max} Spróbuj ją odgadnąć :)")

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
                    i = input("Chcesz zagrać ponownie? (t/n) ")
                    if i == "t":
                        main()
                    elif i == "n":
                        exit()
                    else:
                        print("t - tak | n - nie")

        # Niedozwolony input, cofa na początek pętli
        else:
            print("To nie jest liczba :(")


# Start programu
main()