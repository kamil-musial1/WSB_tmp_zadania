def czyszczenie(tekst):
    czysty_tekst = tekst.lower().replace(',','').replace('.','').replace("'",'').replace('(','').replace(')','')
    return czysty_tekst


def ile_slow(tekst):
    podzielony_tekst = tekst.split()
    return len(set(podzielony_tekst))


with open ("3_my_file.txt", 'r') as plik:        #otwieramy plik
    cala_tresc = plik.read()                     #czytamy cały plik, zapisujemy jako string do zmiennej cala_tresc

print('caly plik jest ',type(cala_tresc),'a w nim\n',cala_tresc,'\n')

print('Czyscimy tekst')
cala_tresc = czyszczenie(cala_tresc)

print('liczba unikalnych slow wynosi',ile_slow(cala_tresc))

#print(ile_slow(czyszczenie(cala_tresc)))  #wszystko razem