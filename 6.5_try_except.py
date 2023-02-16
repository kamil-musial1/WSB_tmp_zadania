while True:
    liczba_dzieci = input('Wprowadz liczbe dzieci ')
    try:
        liczba_dzieci = int(liczba_dzieci)
        break
    except:
        print('zla liczba dzieci, jeszcze raz')

while True:
    wyplata = input('Wprowadz wyplate ')
    try:
        wyplata = float(wyplata)
        break
    except:
        print('zla wyplata, jeszcze raz')

print('Dane poprawne, dzialamy dalej')
print('dalsza czesc programu')
#czy jest blad
#kasa_na_dziecko = wyplata / liczba_dzieci

try:
    kasa_na_dziecko = wyplata / liczba_dzieci
    print('kasa na dzieco',kasa_na_dziecko)
except ZeroDivisionError:
    print('cala kasa dla ciebie - use condoms')
