# függvényekről
def teszt(nev):
    print("Szia "+nev+"!")

teszt("Pista")
teszt("Zoli")
teszt("Karcsi")
teszt("Ági")
# print("nev")
def negyzet(x):
    n=x*x
 #  print(n)
    return n

negyzet(3)
print(negyzet(3))

harom=negyzet(3)
negy=negyzet(4)
ot=negyzet(5)
print((harom+negy)/ot)

for i in range(1,101):
    print(i)
    x=negyzet(i)
    print(i,x)
print(x)

def kiIr(lista):
    for x in lista:
        print(x,end=",")
    print()

print(12*"-")
l = list()
l = [1,12,2,3]
print(l[3])
print(12*"-")

def kiIr2(lista):
    for i in range(len( lista)):
        print(lista[i])



en_listam=(1,2,3,4,2,1)
print(type(en_listam))
print(en_listam)

kiIr(en_listam)
kiIr2(en_listam)

en_listam=[1,2,3,4,2,1]
print(type(en_listam))
print(en_listam)

kiIr(en_listam)
kiIr2(en_listam)

en_listam={1,2,3,4,2,1}
print(type(en_listam))
print(en_listam)

kiIr(en_listam)
# kiIr2(en_listam)