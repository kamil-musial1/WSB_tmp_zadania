# while True:
#     x = input("Wprowadz liczbe calkowita ")
#     try:
#         x = int(x)
#         break
#     except ValueError:
#         print("ups, to nie jest liczba, jeszcze raz")
# print('idziemy dalej')

# while True:
#     try:
#         x = int(input("Wprowadz liczbe calkowita "))
#         break
#     except ValueError:
#         print("ups, to nie jest liczba, jeszcze raz")
# print('idziemy dalej')

licznik = 0
while True:
    try:
        x = int(input("Wprowadz liczbe calkowita "))
        break
    except ValueError:
        print("ups, to nie jest liczba, jeszcze raz")
        licznik += 1
        if licznik == 3:
            print('3 nieudane proby ')
            break
print('idziemy dalej')