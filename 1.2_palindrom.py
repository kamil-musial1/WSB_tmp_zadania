#dodatkowo ręczne dodawanie słów do listy - pętla "while True"
lista_slow = []
while True:
    slowo = input('podaj slowo do sprawdzenia ')
    lista_slow.append(slowo)
    kontynuacja = input('czy chcesz dodac kolejne slowo? T/N ')
    if kontynuacja.lower() == 'n':  #czy zakonczyc worowadzanie
        break
    elif kontynuacja.lower() != 't':   #czy rozpoznano wybor "tak"
        print('Nie rozpoznano wyboru, zakladam, ze chcesz wprowadzic kolejne slowo')

for slowo in lista_slow:
    slowo_od_konca = slowo[::-1]
    if slowo == slowo_od_konca:
        print('slowo',slowo,'jest palindromem')
    else:
        print('slowo', slowo, 'NIE jest palindromem')
