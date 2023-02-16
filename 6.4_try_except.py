def can_be_int(liczba):
    try:
        liczba = int(liczba)
        return True
    except ValueError:
        return False


def try_to_int(liczba):
    try:
        liczba_int = int(liczba)
        return liczba_int
    except ValueError:
        return liczba
    #nie wiemy, czy zwrocono int, czy bazową zmienną


def can_be_float(liczba):
    try:
        liczba = float(liczba)
        return True
    except ValueError:
        return False


while True:
    wyplata = input('Wprowadz wyplate ')
    liczba_dzieci = input('Wprowadz liczbe dzieci ')
    if can_be_float(wyplata) and can_be_int(liczba_dzieci):
        print('Dane poprawne, dzialamy dalej')
        wyplata = float(wyplata)
        liczba_dzieci = int(liczba_dzieci)
        break
    else:
        print('Dane niepoprawne, jeszcze raz ')
print('dalsza czesc programu')
#czy jest blad
#kasa_na_dziecko = wyplata / liczba_dzieci

try:
    kasa_na_dziecko = wyplata / liczba_dzieci
except ZeroDivisionError:
    print('cala kasa dla ciebie - use condoms')
