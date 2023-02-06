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







