haslo=input() #'secret'

print('dlugosc hasla: ' + str(len(haslo)))

if len(haslo)==0:
    print('nie podano hasla')
elif len(haslo)==1 or len(haslo)==2:
    print("za ktotkie haslo")
else:
    gwiazdka=(len(haslo) - 2)*'*'
    haslo=haslo.replace(haslo[1:-1], gwiazdka)

    print("gwiazdki " + gwiazdka)
    print('co wyszlo ' + haslo)
