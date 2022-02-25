isim = input("İsminizi giriniz: ")
print("Merhaba " + isim + " Hadi Başlayalım ! ")

gizli_kelime = "biber"

tahmin_kelimesi = ""

can = 10

while can > 0:

	karakter_bitis = 0

	for karakter in gizli_kelime:

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

	if tahmin not in gizli_kelime:
		can -= 1
		print("Yanlış ! ")
		print(f"{can} Canınız Kaldı")

		if can == 0:
			print("Malesef Oyunu Kaybettiniz :(")