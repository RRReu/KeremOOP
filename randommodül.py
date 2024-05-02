import random

sayilar = []

for i in range(5):
    sayi = random.randrange(0, 6)
    
    while sayi in sayilar:
        sayi = random.randrange(0, 6)
        if sayi not in sayilar:
            break



    sayilar.append(sayi)

print(sayilar)
