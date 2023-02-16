# przepis = {'mleko' : 2, 'ser' : 1.3, 'maslo' : 1.2, 'maka' : 3.4, 'jajko' : 6}
# for i in przepis.keys():
#     print(i)
#     print(przepis[i])

przepis = {'mleko' : 2, 'ser' : 1.3, 'maslo' : 1.2, 'maka' : 3.4, 'jajko' : 6}
zapas = {'mleko' : 5.2, 'ser' : 3.6, 'maslo' : 3.4, 'maka' : 12, 'jajko' : 16, 'woda' : 44, 'proszek' :  11}

liczba_ciast = float('inf')
for i in przepis.keys():
    x = zapas[i] / przepis[i]    #5.2 / 2
    if x < liczba_ciast:
        liczba_ciast = x
print('liczba ciast = ',int(liczba_ciast))

# ratio = {}   #tworzymy pusty słownik
# for i in przepis.keys():      #petla po kluczach słownika
#     ratio[i] = (zapas[i] / przepis[i])     #zapisujemy w słowniku ile ciast można zrobić z każdego produktu
#
# min_key = (min(ratio, key=ratio.get))    #to trudne, łapiemy ten produkt, z którego będzie najmniej ciast
# print(min_key, int(ratio[min_key]))      #wypisujemy produkt, z ktorego będzie najmniej ciast oraz liczbę tych ciast