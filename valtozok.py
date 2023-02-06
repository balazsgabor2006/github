from builtins import print
from pickle import FALSE, TRUE


szam=12
print(szam)
szam=szam+6
print(szam)
szam=szam*szam
print(szam)
szam=szam+1
print(szam)
szam +=1 # szam++
print(szam)

szam +=10
print(szam)

szam -=1 #szam--
print(szam)

szam *=10
print(szam, type(szam))
szam /=10
print(szam, type(szam))

szam="szam"
print(szam, type(szam))

szam=TRUE
print(szam, type(szam))

szam=FALSE
print(szam, type(szam))

szam=True
print(szam, type(szam))

szam=False
print(szam, type(szam))

print(1 == 1)
print(1 == 2)

szam=True
print(szam == TRUE)
print(szam == True)

szam=(1,2,3)
print(szam, type(szam))

lista=[1,2,3]
print(lista, type(lista))

halmaz={1,2,3}
print(halmaz, type(halmaz))

a,b = 1,2
print(a)
print(b)

# a,b=12
a,b=12,44
print("a =",a,"b =",b)
print("a =",a,"b =",b,sep="")
print("a=",a,"b=",b,sep="")

szoveg="Szia"
nev="Pista"
koszones= szoveg+" "+nev
print(koszones)

koszones= szoveg+" "+nev+"!"
print(koszones)

print('-'*13)
koszones= szoveg+" "+nev+"!"*3
print(koszones)
print('-'*13)

koszones=(szoveg+" ")*5+nev+"!"*3
print(koszones)

szam=12

# print(szoveg+szam)
print(szoveg*szam)
# print(szoveg/szam)
# print(szoveg-szam)
# print(szoveg*koszones)

szam=1.0
print(szoveg*szam)
print(szam*szoveg)

szam=float(input)("Kérek egy számot")
szerencseszam=