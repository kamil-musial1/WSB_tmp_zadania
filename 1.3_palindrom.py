#dodatkowo dodawanie razem wielu słów do listy
lista_slow = input('Wprowadx slowa oddzielajac je spacja ').split()
#zadanie domowe - rozwinąć, dodać usuwanie z listy i dodawanie

for slowo in lista_slow:
    slowo_od_konca = slowo[::-1]
    if slowo == slowo_od_konca:
        print('slowo',slowo,'jest palindromem')
    else:
        print('slowo', slowo, 'NIE jest palindromem')
