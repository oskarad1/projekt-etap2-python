import os
import csv


class samochod:
    def __init__(self, marka, model, skrzynia, rocznik, pojemnosc, przebieg):  # konstruktor
        self.marka = marka
        self.model = model
        self.skrzynia = skrzynia
        self.rocznik = rocznik
        self.pojemnosc = pojemnosc
        self.przebieg = przebieg


def wczytywanie(self, plik):
    self.marka = plik.readline()
    self.marka = self.marka.rstrip("\n")
    self.model = plik.readline()
    self.model = self.model.rstrip("\n")
    self.skrzynia = plik.readline()
    self.skrzynia = self.skrzynia.rstrip("\n")
    self.przebieg = int(plik.readline())
    self.rocznik = int(plik.readline())
    self.pojemnosc = int(plik.readline())
