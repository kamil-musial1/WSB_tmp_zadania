# załóżmy, że pesel ma 4 cyfry
# stwórzmy zbiór NFZ – ludzie, w bazie pacjentów NFZ
# stwórzmy zbiór chorzy_rok – ludzie chorzy w ostatnim roku
# stwórzmy zbiór chorzy_miesiac – ludzie chorzy w ostatnim miesiącu
# stwórzmy zbiór krzyki – wszystkich ludzi mieszkających na krzykach
# stwórzmy zbiór centrum – wszystkich ludzi mieszkających

NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

# sprawdźmy, ile osób, które chorowały w ostatnim roku na krzykach
print('Chorzy w ostatnim roku na krzykach ',chorzy_rok.intersection(krzyki))
print('ilość: ',len(chorzy_rok.intersection(krzyki)))

# sprawdźmy ile osób z Krzyków chorowało w ostatnim roku
print('\nChorzy w ostatnim roku na krzykach ',krzyki.intersection(chorzy_rok))
print('Ilość ',len(krzyki.intersection(chorzy_rok)))

# sprawdźmy, ile osób chorowało w ostatnim miesiącu w centrum
print('\nChorzy w ostatnim miesiącu w centrum ',centrum.intersection(chorzy_miesiac))
print('Ilość ',len(centrum.intersection(chorzy_miesiac)))

# sprawdźmy, ile mieszka w sumie w centrum i na krzykach
print ('\nMIeszkańcy centrum i Krzyków ',centrum.union(krzyki))
print ('Ilość ',len(centrum.union(krzyki)))
#print(len(krzyki) + len(centrum))

# sprawdźmy poprawność danych:
# każdy, kto chorował w ostatnim miesiącu, jednocześnie chorował w ostatnim roku


# nikt nie powinien mieszkać jendocześnie w centrum i na krzykach – jeśli tak, trzeba usunąć
# każdy: chory, zdrowy, z krzyków i z centrum, powinien być w bazie NFZ.
#Jeśli nie ma, trzeba dopisać



# sprawdźmy poprawność danych:
print ('\nPoprawność danych')

# każdy, kto chorował w ostatnim miesiącu, jednocześnie chorował w ostatnim roku
print ('\nLudzie chorujący w ostatnim miesiącu i NIE chorujący w ostatnim roku ')
print(chorzy_miesiac.difference(chorzy_rok))
if len(chorzy_miesiac.difference(chorzy_rok)) == 0:
    print ('ok')

# nikt nie powinien mieszkać jendocześnie w centrum i na krzykach – jeśli tak, trzeba usunąć
print('Osoby mieszkjaące jednocześnie w centrum i na krzykach ',krzyki.intersection(centrum))
print('Ilość: ',len(krzyki.intersection(centrum)))
if len(krzyki.intersection(centrum)) != 0:
    x = input('Usuwam. Usunąć ludzi z Krzyków (K), czy z Centrum (C) ?   ')
    duplikaty = krzyki.intersection(centrum)
    if x == 'K':
        for i in krzyki.intersection(centrum):
            krzyki.remove(i)
    elif x == 'C':
        for i in duplikaty:
            centrum.remove(i)
        # centrum = centrum.difference(krzyki.intersection(centrum))
        # centrum = centrum.difference(krzyki)

print ('Usunięte, sprawdzam: Liczba osób mieszkających jednocześnie w centrum i na krzykach ',len(krzyki.intersection(centrum)))
if len(krzyki.intersection(centrum)) == 0:
    print ('ok')
else:
    print ('Ups, nie udało się usunać')

# każdy: chory, zdrowy, z krzyków i z centrum, powinien być w bazie NFZ. Jeśli nie ma, trzeba dopisać
poza_NFZ = (centrum.union(krzyki.union(chorzy_miesiac.union(chorzy_rok)))).difference(NFZ)
print (f'\nLudzie poza NFZ {poza_NFZ}, liczba tych osób {len(poza_NFZ)}\ndodaje do bazy NFZ')
NFZ = NFZ.union(poza_NFZ)
print ('Sprawdzam ',(centrum.union(krzyki.union(chorzy_miesiac.union(chorzy_rok)))).difference(NFZ))
if len((centrum.union(krzyki.union(chorzy_miesiac.union(chorzy_rok)))).difference(NFZ)) == 0:
    print ('ok')
else:
    print ('Ups, nie udało się dodać do bazy. Wciąż mamy ',len(centrum.union(krzyki.union(chorzy_miesiac.union(chorzy_rok)))),' ludzi poza bazą NFZ')

# pesele żeńskie mają ostatnią cyfrę parzystą, męskie – nieparzystą.
# zróbmy nowe zbiory, osobne dla mężczyzn i kobiet (w NFZ)

print ('\nDzielę zbiór NFZ na panów i panie')
NFZ_men = set()
NFZ_women = set()
for i in NFZ:
    if i%2 == 0:
        NFZ_women.add(i)
    else:
        NFZ_men.add(i)
print ('Sprawdzam\nPanie to ',NFZ_women,' a Panowie to ',NFZ_men)

#wypiszmy kobiety z krzyków, które były chore w ostatnim roku
#domowe   ##wypiszmy mężczyzn z centrum, którzy NIE byli chorzy w ostatnim roku
a = krzyki.intersection(chorzy_rok) # ludzie chorzy w ostatnim roku na krzykach, cześć wpsólna chorych w ostatnim roku i mieszkańców Krzyki
b = a.intersection(NFZ_women) # część wspólna kobiet i chorych w ostatnim roku na krzykach
print ('\nkobiety chore w ostatnim roku na krzykach:   ',b)

#napiszmy program przyjmujący PESEL i zwracający wszystkie dostępne informacje o tym peselu
print()
pesel = int(input('Wpisz PESEL:    '))
if pesel not in NFZ:
    print ('Brak osoby w bazie NFZ')
else:
    if pesel in NFZ:
        print('Osoba jest w bazie NFZ ')
    if pesel in NFZ_men:
        print('Osoba jest mężczyzną ')
    else:
        print('Osoba jest kobietą ')
    if pesel in krzyki:
        print('Osoba mieszka na krzykach')
    else:
        print('Osoba mieszka w centrum')
    if pesel in chorzy_rok:
        print('Osoba była chora w tym roku')
    if pesel in chorzy_miesiac:
        print('A nawet w tym miesiącu ')

#zabezpieczmy program
#wszystkie dane, które wprowadzamy muszą być poprawne
#sprawdźmy, czy wszystkie pesele w zbiorach są poprawne (4ro cyfrowe liczby)

