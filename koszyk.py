import pprint

def zapiszKoszyk(d):
    file=open("koszyk.csv", 'w')
    for poz in d:
        linia=""
        for key in ['name', 'cena', 'vat_procent', 'jednostka', 'ilosc']:
            linia+="{0},".format(poz[key])
        file.write(linia + '\n')
    file.close()

def odczyt():
    koszyk2=[]
    plik=open("koszyk.csv", "r")
    calosc=plik.read()
    linie=calosc.split('\n')
    for l in linie:
        produkt={}
        if len(l)>0:
            pola = l.split(',')
            produkt["nazwa"]=pola[0]
            produkt['cena']=pola[1]
            produkt['vat']=pola[2]
            produkt['jednostka']=pola[3]
            produkt['ilosc']=pola[4]
            koszyk2.append(produkt)
    print(koszyk2)
    plik.close()


def main():
    koszyk=[{'name': 'mlekowita', 'cena': 2.25,  'vat_procent': 23 , 'jednostka': 'sztuka', 'ilosc': 5},
    {'name': 'mleko', 'cena': 2.24,  'vat_procent':23 , 'jednostka':'sztuka' , 'ilosc': 4},
    {'name': 'goplana', 'cena': 2.45,  'vat_procent':23 , 'jednostka': 'sztuka', 'ilosc': 2},
    {'name': 'wedel', 'cena': 2.55,  'vat_procent':23 , 'jednostka':'sztuka' , 'ilosc': 1}]
    zapiszKoszyk(koszyk)
    odczyt()
    # pprint.pprint(koszyk)


if __name__=='__main__':
    main()
