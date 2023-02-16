class BMW:
    kolor = 'czerwony'
    bagaznik = []
    def hamuj(self):
        print('Tak hamuje')
        self.skrec('lewo')

    def skrec(self, strona):
        print(f'skrec w {strona}')

    def dodaj(self, a, b):
        return a + b

moje_auto = BMW()
auto_sasiada = BMW()
moje_auto.hamuj()
moje_auto.skrec('lewo')
print(moje_auto)
print(moje_auto.dodaj(5, 8))
moje_auto.kolor = 'bialy'
print(moje_auto.kolor)
print(auto_sasiada.kolor)
moje_auto.bagaznik.append('wiertarka')
moje_auto.bagaznik.append('telefon')
print(moje_auto.bagaznik)
print(auto_sasiada.bagaznik)