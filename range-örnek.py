sayi = int(input("Sayı Giriniz: "))
asalsayi = True
if sayi == 1:
    asalsayi = False
for i in range(2,sayi):
    if(sayi % i == 0):
        asalsayi = False
        break
if asalsayi:
    print("Bu sayı asaldır")
else:
    print("Bu sayı asal sayı değildir")