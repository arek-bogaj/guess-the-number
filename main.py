import random

# Import paczek językowych
import en
import pl


min = 1
max = 10
txt = ""
diff_label = ""


# Funkcja odpowiedzialna za wybór języka i wyświetlenie tytułu
def start():
    global txt
    while True:
        i = input("[ en - ENGLISH | pl - POLSKI ]: ")
        if i == "en":
            txt = en.txt
            break
        elif i == "pl":
            txt = pl.txt
            break
        else:
            pass

    # Tytuł
    print()
    print(txt[0])


# Funkcja odpowiedzialna za poziom trudności
def choose_difficulty():
    print()
    print(txt[1])

    global max

    while True:
        d = input(txt[2])
        if txt == pl.txt and d == "ł" or txt == en.txt and d == "e":
            max = 10
            break
        elif txt == pl.txt and d == "ś" or txt == en.txt and d == "m":
            max = 100
            break
        elif txt == pl.txt and d == "t" or txt == en.txt and d == "h":
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
start()
main()