samochody=['syrena','polonez', 'fiat', 'kia']
ilosc=[3,5,2,4]

print(samochody[0])
print(samochody[1])
print(samochody[2])

for idx in range(len(samochody)):
    print("idx " + str(idx) + " : " + samochody[idx])

for idx in range(len(samochody)):
    print("idx: " + str(idx) +  " : " + samochody[idx])
    print(samochody[idx] + ' ma ilosc drzwi ' + str(ilosc[idx]))

print(samochody[-1])
# print(samochody[1,-1])
print(samochody[1:])
# print(samochody[10])
