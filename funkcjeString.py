marka='Pegout'
ilosc_drzwi=5
pojemnosc=1.3
imie='Ala'
zwierze ='kot'

marte_up=marka.upper()
marka_lo=marka.lower()

print('Samochod ' + marka + ' ma ' +str(ilosc_drzwi) + ' drzwi')
print(marte_up)
print('Pojemnosc po zmianach: ' + str(pojemnosc*2))
print(marka_lo)

print('z minus jeden -' + marka[-1])
print('z 1:-1 -' + marka[1:-1])

print("{0} ma {1}a".format(imie, zwierze))
