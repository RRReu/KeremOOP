# __ kullanıldığında private olur erişilmez get ve set methodları erişim için gereklidir.
# _ kullandıldığında protected olur sınıf ve alt sınıflar içind erişilebilir ve değişebilir.

class Person:
    __name = "john"

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

p = Person()
print(p.get_name()) # John yazdırır.
p.set_name("Mike") # Adı Mike olarak değiştirir.
print(p.get_name()) # Mike yazdırır.