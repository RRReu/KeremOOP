class Araba:
    def __init__(self,marka,renk,yil):
        self.marka = marka
        self.renk = renk
        self.yil = yil
    def modelBilgisi(self):
        return f"Bu araç {self.yil} model olup, {self.renk} bir {self.marka}dır"

araba1 = Araba("mercedes","sarı","1976")
print(araba1.modelBilgisi())
araba2 = Araba("volvo","mor","2000")
print(araba2.modelBilgisi())
araba3 = Araba("bmw","siyah","2024")
print(araba3.modelBilgisi())

for i in range(3):
    print(i)