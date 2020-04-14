import os
import csv
import operator
import samochod


def wyswietlanie():  # funkcja wyswietlajaca wszystkie pozycje
    with open('samochody.csv', 'r') as csv_plik:
        csv_odczyt = csv.reader(csv_plik)

        for linia in csv_odczyt:
            print(linia)


def dodaj():  # funkcja dodajaca nowa pozycje w katalogu
    with open('samochody.csv', 'a', newline='') as csv_plik:
        zapis = csv.writer(csv_plik)
        ilosc_samochodow = 12
        print("Podaj kolejno: marke samochodu, model, typ szkrzyni biegow, rocznik, pojemnosc silnika i przebieg")
        zapis.writerow([ilosc_samochodow+1, input(), input(),
                        input(), int(input()), int(input()), int(input())])
        print("Dodano samochod")
        ilosc_samochodow+1


def wyswietl_pojedynczo():  # funkcja wyswietlajaca pojedyncza pozycje z katalogu
    with open('samochody.csv', 'r') as plik:
        csv1 = csv.reader(plik)
        wybor = int(input("Podaj numer auta do wyswietlenia"))
        for i in range(wybor):
            next(csv1)
        row = next(csv1)
        print(row)


def usun():  # funkcja usuwajaca wybrana pozycje
    with open('samochody.csv', 'rt') as inp, open('samochody_dwa.csv', 'wt', newline='') as out:
        writer = csv.writer(out)
        usun_linie = input("Podaj numer samochodu, ktory chcesz usunac")
        for row in csv.reader(inp):
            if row[0] != usun_linie:
                writer.writerow(row)
    os.remove('samochody.csv')
    os.rename('samochody_dwa.csv', 'samochody.csv')


def wyswietl_szczegolowo():  # funkcja wyswietlajaca pozycje spelniajace wybrany warunek
    with open('samochody.csv', 'r') as plik:
        rok = input("Podaj od jakiego rocznika wyswietlac auta")
        for linia in csv.reader(plik):
            if linia[4] > rok:
                print(linia)


def sortuj():  # funkcja sortujaca i wyswietlajaca pozycje wedlug rocznika
    with open('samochody.csv', 'r') as plik:
        csv1 = csv.reader(plik)
        sort = sorted(csv1, key=operator.itemgetter(4))
        for linia in sort:
            print(linia)
