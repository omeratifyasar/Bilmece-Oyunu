import secrets


isim = input("İsminizi giriniz: ")
print("Merhaba " + isim + " Hadi Başlayalım ! ")

gizli_kelime1 = "biber"
gizli_kelime2 = "sadakat"
gizli_kelime3 = "muhtar"
gizli_kelime4 = "salıncak"
gizli_kelime5 = "kartopu"

print("\n\n")
secenek = input("Lütfen 1' den 5 kadar bir sayı girin !: ")
tahmin_kelimesi = ""

can = 10


if secenek == "1":
    print("--- Yeşil acı veya Tatlı bir bitki ---")
    while can > 0:

        karakter_bitis = 0

        for karakter in gizli_kelime1:

            if karakter in tahmin_kelimesi:

                print(karakter)
            else:
                print("-")
                karakter_bitis += 1

        if karakter_bitis == 0:
            print("Tebrikler Oyunu Kazandınız !!")	
            break


        tahmin = input("Lütfen Tahmininizi Giriniz:  ")
        tahmin_kelimesi += tahmin

        if tahmin not in gizli_kelime1:
            can -= 1
            print("Yanlış ! ")
            print(f"{can} Canınız Kaldı")

            if can == 0:
                print("Malesef Oyunu Kaybettiniz :(")

if secenek == "2":
    print("--- Güven Kelimesinin Eş anlamlısı ---")
    while can > 0:

        karakter_bitis = 0

        for karakter in gizli_kelime2:

            if karakter in tahmin_kelimesi:

                print(karakter)
            else:
                print("-")
                karakter_bitis += 1

        if karakter_bitis == 0:
            print("Tebrikler Oyunu Kazandınız !!")	
            break


        tahmin = input("Lütfen Tahmininizi Giriniz:  ")
        tahmin_kelimesi += tahmin

        if tahmin not in gizli_kelime2:
            can -= 1
            print("Yanlış ! ")
            print(f"{can} Canınız Kaldı")

            if can == 0:
                print("Malesef Oyunu Kaybettiniz :(")          

if secenek == "3":
    print("--- Bir yerleşim yerinden Sorumlu kişi ---")
    while can > 0:

        karakter_bitis = 0

        for karakter in gizli_kelime3:

            if karakter in tahmin_kelimesi:

                print(karakter)
            else:
                print("-")
                karakter_bitis += 1

        if karakter_bitis == 0:
            print("Tebrikler Oyunu Kazandınız !!")	
            break


        tahmin = input("Lütfen Tahmininizi Giriniz:  ")
        tahmin_kelimesi += tahmin

        if tahmin not in gizli_kelime3:
            can -= 1
            print("Yanlış ! ")
            print(f"{can} Canınız Kaldı")

            if can == 0:
                print("Malesef Oyunu Kaybettiniz :(")                      
                
if secenek == "4":
    print("--- Çocuk parklarında olan en eğlenceli alet ! ---")
    while can > 0:

        karakter_bitis = 0

        for karakter in gizli_kelime4:

            if karakter in tahmin_kelimesi:

                print(karakter)
            else:
                print("-")
                karakter_bitis += 1

        if karakter_bitis == 0:
            print("Tebrikler Oyunu Kazandınız !!")	
            break


        tahmin = input("Lütfen Tahmininizi Giriniz:  ")
        tahmin_kelimesi += tahmin

        if tahmin not in gizli_kelime4:
            can -= 1
            print("Yanlış ! ")
            print(f"{can} Canınız Kaldı")

            if can == 0:
                print("Malesef Oyunu Kaybettiniz :(")                
                
if secenek == "5":
    print("--- Kar yağınca oynanan oyun ! ---")
    while can > 0:

        karakter_bitis = 0

        for karakter in gizli_kelime5:

            if karakter in tahmin_kelimesi:

                print(karakter)
            else:
                print("-")
                karakter_bitis += 1

        if karakter_bitis == 0:
            print("Tebrikler Oyunu Kazandınız !!")	
            break


        tahmin = input("Lütfen Tahmininizi Giriniz:  ")
        tahmin_kelimesi += tahmin

        if tahmin not in gizli_kelime5:
            can -= 1
            print("Yanlış ! ")
            print(f"{can} Canınız Kaldı")

            if can == 0:
                print("Malesef Oyunu Kaybettiniz :(")                
