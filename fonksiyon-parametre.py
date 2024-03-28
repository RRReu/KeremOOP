x = int(input("Bir tam sayı giriniz: "))
while x < 0:
    x = int(input("Girilen sayı sıfırdan büyük olmalıdır. Yeniden deneyiniz."))
def faktoriyel(b):
        i = 1
        a = 1
        while i <= b:
            a *= i 
            i += 1
        return a
sonuc = faktoriyel(x)
y = x*3.1415/180
sonuc3 = ((1)-((y**2)/faktoriyel(2)) + ((y**4)/faktoriyel(4)) - (((y**6)/faktoriyel(6))))
print(sonuc3)



     



