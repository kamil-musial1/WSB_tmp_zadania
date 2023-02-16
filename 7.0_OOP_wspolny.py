class BMW:
    def __init__(self, kolor, kierunek, predkosc):
        self.kolor = kolor
        self.przebieg = 0
        self.bagaznik = []
        self.predkosc = predkosc
        self.kierunek = kierunek

    def __str__(self):
        if self.przebieg > 0 :
            return f'Auto BMW ma kolor {self.kolor} i ma przebieg {self.przebieg}'
        else:
            return f'Takie se auto'

    def przyspiesz(self, ile):
        self.predkosc += ile

    def hamuj(self):
        print('Hamuje')
        self.predkosc = 0

    def skrec(self, strona):
        if strona == 'prawo':
            if self.kierunek == 'N':
                self.kierunek = 'E'
            elif self.kierunek == 'E':
                self.kierunek = 'S'
            elif self.kierunek == 'S':
                self.kierunek = 'W'
            elif self.kierunek == 'W':
                self.kierunek = 'N'
        elif strona == 'lewo':
            if self.kierunek == 'N':
                self.kierunek = 'W'
            elif self.kierunek == 'W':
                self.kierunek = 'S'
            elif self.kierunek == 'S':
                self.kierunek = 'E'
            elif self.kierunek == 'E':
                self.kierunek = 'N'
        print(f'skrecam w {strona} i jade w kierunku {self.kierunek}')

    def dodaj(self, a, b):
        return a + b

    def dodaj_przebieg(self, dodatkowy_przebieg):
        if dodatkowy_przebieg >= 0:
            self.przebieg += dodatkowy_przebieg
        else:
            print('niedozwolona akcja')


moje_auto = BMW('czarny', 'N', 300)
auto_sasiada = BMW('czerwone', 'W', 10)

print(moje_auto)
print(f'kolor mojego auta to {moje_auto.kolor}')
print(f'kolor auta somsiada to {auto_sasiada.kolor}')
moje_auto.kolor = 'czerwony'
print(f'kolor mojego auta to {moje_auto.kolor}')
print(f'kolor auta somsiada to {auto_sasiada.kolor}')

moje_auto.bagaznik.append('wiertarka')
moje_auto.bagaznik.append('telefon')
print(moje_auto.bagaznik)
print(auto_sasiada.bagaznik)
#moje_auto.przebieg = 10
print(moje_auto.przebieg)
print(auto_sasiada.przebieg)

moje_auto.hamuj()
auto_sasiada.skrec('prawo')
print(moje_auto.dodaj(4, 5))
print(type(moje_auto))
moje_auto.dodaj_przebieg(20)
moje_auto.dodaj_przebieg(20)
moje_auto.dodaj_przebieg(-20)
print(moje_auto.przebieg)
print(auto_sasiada.przebieg)

moje_auto.skrec('prawo')
moje_auto.skrec('prawo')
moje_auto.skrec('prawo')
moje_auto.skrec('prawo')