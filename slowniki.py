# samolot={'name': 'boeing', 'przebieg':1000, 'type':'pasazerski'}

def print_dict(d):
    for key in samolot:
        print("{0}:{1}".format(key, d[key]))

def calucate_vat(netto):
    vat=float(netto*23)/100
    return vat

def main():
    print "Tutaj program"

# for key in samolot:
#     print('{0}:{1}'.format(key, samolot[key]))
#
# for key, value in samolot.iteritems():
#     print('{0}:{1}'.format(key, value))
#
if  __name__ =='__main__':
    samolot={'name': 'boeing', 'przebieg':1000, 'type':'pasazerski'}
    print_dict(samolot)

if __name__=='__main__':
    vat=calucate_vat(1000)
    print("{0}".format(vat))

if __name__=="__main__":
    main()
