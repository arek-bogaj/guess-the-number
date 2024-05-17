import random

# Import paczek językowych
import en
import pl

# Domyślna paczka językowa
txt = en.txt


min = 1
max = 10
diff_label = ""


# Funkcja odpowiedzialna za poziom trudności
def choose_difficulty():
    print()
    print(txt[1])

    global max

    while True:
        d = input(txt[2])
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
    print(txt[3], min, txt[4], f"{max}.", txt[5])

    # Pętla, sprawdza czy wprowadzono text czy liczbę i czy input zgadza się wygenerowaną liczbą
    while True:
        i = input(": ")
        if i.isdigit():
            i = int(i)
            if i < min or i > max:
                print(txt[6])
            elif i > numer:
                numb_of_attempts += 1
                print(txt[7])
            elif i < numer:
                numb_of_attempts += 1
                print(txt[8])

            # Input zgodny z wygenerowaną liczbą
            else:
                print()
                print(txt[9], f"{numer} :)")
                print(txt[10], numb_of_attempts, txt[11])
                print()

                # Pętla, sprawdza czy wprowadzono poprawne dane
                while True:
                    i = input(txt[12])
                    if i == "t":
                        main()
                    elif i == "n":
                        exit()
                    else:
                        pass

        # Niedozwolony input, cofa na początek pętli
        else:
            print(txt[13])


# Start programu
print(txt[0])
main()