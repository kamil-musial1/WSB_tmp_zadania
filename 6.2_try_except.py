liczba = input('Wprowadz liczbe ')

try:
    liczba = int(liczba)
    print('Wprowadzono poprawną liczbe')
except ValueError:
    try:
        liczba = float(liczba)
        print('Nie udalo sie zapisac liczby jako integer\nzapisue jako float')
    except ValueError:
        print('nie udalo sie zapisac jako int, ani jako float - wpisana \"liczba\" zostaje stringiem')
#        raise NameError('No nie da rady')

print(type(liczba))
print('idziemy dalej')