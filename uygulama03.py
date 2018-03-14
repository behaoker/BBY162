çeviriler={"Elma": "Apple", "Karpuz": "Watermelon", "Kavun": "Melon"}
Seçenekler="""
1: Anahtarları Gösterir.
2: Değerleri Gösterir.
3: Çıkış.
"""
while True:
    print(Seçenekler)
    işlem= input("Yapılacak İşlem:")
    if işlem=="1":
        print(çeviriler.keys())

    elif işlem=="2":
        print(çeviriler.values())

    elif işlem=="3":
        print("Program Sonlandırılıyor!..")
        break

    else:
        print("HATA!")