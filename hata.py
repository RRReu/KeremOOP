try:
    x= int(input("Bir sayı gir"))
    y= int(input("İkinci sayıyı gir"))
    print(x/y)
except ZeroDivisionError as errorLog:
    print("0 Girme")
except ValueError:
    print("Sayı gir")