#Dictionary Oluştur

hafta = {
        "1":"Pazartesi",
        "2":"Salı",
        "3":"Çarşamba",
        "4":"Perşembe",
        "5":"Cuma",
        "6":"Cumartesi",
        "7":"Pazar"
}

x= input("Bir sayı giriniz")
gun = hafta[x]
print(f"Haftanın {x}. günü, {gun}")



hafta.pop("2") # Girilen değeri temizleme
print(hafta.items())
hafta.clear() # Temizleme
print(hafta.items())
hafta.update({"8":"özgü"}) # Ekleme
print(hafta.items())
