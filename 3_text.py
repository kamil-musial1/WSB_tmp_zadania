with open ("3_my_file.txt", 'r') as plik_txt:
    cala_tresc = plik_txt.read()
print(cala_tresc)
cala_tresc = cala_tresc.split()
print(cala_tresc)
for i in range(len(cala_tresc)):
    cala_tresc[i] = cala_tresc[i].lower().replace(',','').replace('.','').replace("'",'').replace('(','').replace(')','')
print(cala_tresc)

print(len(set(cala_tresc)))