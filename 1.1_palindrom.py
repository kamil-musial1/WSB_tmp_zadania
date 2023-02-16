#podejscie pierwsze - ręczne sprawdzanie liter z początku i z końća
import math   #potrzebne, do zaokrąglenia w dół
lista_slow = ['mmmaamm', 'mama', 'axa', 'xanax', 'pies']
for slowo in lista_slow:
    print('\nStart slowo', slowo)
#    liczba_iteracji = math.floor(len(slowo)/2)
#    liczba_iteracji = int(len(slowo)/2)
    liczba_iteracji = len(slowo)//2
    flaga_czy_palindrom = True
    for i in range(liczba_iteracji):
        if slowo[i] != slowo[-1 - i]:
            print('litera', slowo[i], 'się nie zgadza')
            print('slowo',slowo,'nie jest palindromem')
            flaga_czy_palindrom = False
            break
        else:
            print('litera ',slowo[i],'ok')
    if flaga_czy_palindrom:
        print('slowo',slowo,'jest palindromem')

#podejście drugie - odwrócenie listy
lista_slow = ['mama', 'axa', 'xanax', 'pies']
for slowo in lista_slow:
    slowo_od_konca = slowo[::-1]   #https://www.w3schools.com/python/python_howto_reverse_string.asp
    if slowo == slowo_od_konca:
        print('slowo',slowo,'jest palindromem')
    else:
        print('slowo', slowo, 'NIE jest palindromem')
