samochody=['syrena','polonez', 'fiat', 'kia']
ilosc=[3,5,2,4]
file=open("testfile.txt", "w")

file.write("Hello word!")
for idx in range(len(samochody)):
    file.write("idx: " + str(idx) +  " : " + samochody[idx])
    file.write(samochody[idx] + ' ma ilosc drzwi ' + str(ilosc[idx]))
file.close()

ff=open("testfile.txt", "r")
print(ff.read())
