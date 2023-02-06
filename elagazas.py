szam=int(input("Kérek egy természetes számot"))
# print(szam % 2)
if szam % 2 == 0:
    print("A " +str(szam)+" páros")
    print("A", szam, "páros")
else:
    print("A "+str(szam)+" páratlan")


szam=int(input("Kérek egy természetes számot"))
if szam % 2 == 0:
    print("A ",szam, "kettővel osztható")
elif szam % 3 == 0:
    print("A ",szam, "hárommal osztható")


if szam % 2 == 0 and szam % 3 ==0:
    print("A ",szam, "osztható 6-al")

import random

veletlen_szam = random.randint(1,10)
print(veletlen_szam)