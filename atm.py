print("Kod Kardeşim ATM Uygulaması")
bakiye = 0
print("""[1] Bakiye Sorgula
[2] Para Yatır
[3] Para Çek
[Q] Çıkış Yap""")
while True:
    print("---")
    islem = input("İşlem seçiniz : ")
    if islem == "1":
        print("Hesabınızda bulunan toplam bakiye : {} TL".format(bakiye))
    elif islem == "2":
        yatirilanmiktar = int(input("Yatırmak istediğiniz tutar : "))
        bakiye += yatirilanmiktar
        print("İşlem başarılı. Hesabınızdaki toplam para : {} TL".format(bakiye))
    elif islem == "3":
        cekilecekmiktar = int(input("Çekmek istediğiniz tutar : "))
        if cekilecekmiktar > bakiye:
            print("Yetersiz bakiye!")
        else:
            bakiye -= cekilecekmiktar
            print("İşlem başarılı. Hesabınızdaki kalan para : {} TL".format(bakiye))
    elif islem == "Q" or islem == "q":
        print("Çıkış yapılıyor.")
        break
    else:
        print("Hatalı seçim. Lütfen yeniden deneyin")
