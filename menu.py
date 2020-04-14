import csv
import os
import samochod
import funkcje

print("Katalog samochodow \n MENU GLOWNE: \n ------------------------------------------------------ \n 1. Wprowadz nowy samochod do katalogu. \n 2. Wyswietl liste wszystkich samochodow w katalogu. \n 3. Wyswietl liste samochodow od wybranego rocznika. \n 4. Wyswietl dane jednego samochodu. \n 5. Posortuj samochody wedlug rocznika produkcji. \n 6. Usun samochod z katalogu. \n 7. Wyjdz z programu.")


def menu():
    wybor = input()

    if wybor == "1":
        funkcje.dodaj()
        menu()

    elif wybor == "2":
        funkcje.wyswietlanie()
        menu()

    elif wybor == "3":
        funkcje.wyswietl_szczegolowo()
        menu()

    elif wybor == "4":
        funkcje.wyswietl_pojedynczo()
        menu()

    elif wybor == "5":
        funkcje.sortuj()
        menu()

    elif wybor == "6":
        funkcje.usun()
        menu()

    elif wybor == "7":
        os.system("CLS")

    else:
        print("Nie ma takiej opcji w menu.")
        menu()


menu()
