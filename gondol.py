import random
# random.seed(0)

kor = 13
if kor > 10:
    kor=kor-10


gondolt = random.randint(1,100)
print(gondolt)

# tipp = int(input("kérem a számot"))
'''
ismetles = True
while (ismetles):
    tipp = input("kérem a tipped: ")
    tipp = int(tipp)

    if tipp < gondolt:
        print("Kicsi")
    if gondolt < tipp:
        print("Nagy")
    if gondolt == tipp:
        print("Talált")
        ismetles = False
'''
db=0
tipp = 0
while (tipp != gondolt):
    tipp = int(input("kérem a tipped: "))
    # db ==1
    db = db = 1
    if tipp < gondolt:
        print("Kicsi")
    else:
        if gondolt < tipp:
            print("Nagy")
print(db, "Lépésben talált")
        