sayilar = [1,2,3,4,5]
x = input("Sayı gir")
if x.isdigit() == False:
    raise TypeError("Sayı gir")
x = int(x)
if x not in sayilar:
    raise ValueError(f"{x}sayı listede yok")
print(f"{x} sayısı listede var")