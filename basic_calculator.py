print("HESAP MAKİNESİ")

sayi1 = float(input("İlk sayı: "))
islem = input("İşlem seç (+, -, *, /): ")
sayi2 = float(input("İkinci sayı: "))

if islem == "+":
    sonuc = sayi1 + sayi2
elif islem == "-":
    sonuc = sayi1 - sayi2
elif islem == "*":
    sonuc = sayi1 * sayi2
elif islem == "/":
    if sayi2 != 0:
        sonuc = sayi1 / sayi2
    else:
        sonuc = "Hata !!!Sıfıra bölünemez."
else:
    sonuc = "Geçersiz "

print("Sonuç:", sonuc)