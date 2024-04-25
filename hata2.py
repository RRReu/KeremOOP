urunler = {"urunAdi":"MSI", "fiyat":10000}
def getir (urun,key):
    try:
        return urun[key]
    except KeyError:
        return "bulunamadı"
a = getir(urunler, "fiyat")
b = getir(urunler, "urunAdi")
c = getir(urunler, "model")

print(f"{b} rünü model no: {c} fiyatı : {a}")
