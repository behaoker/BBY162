#saniyeyi dakika, saat, gün, ay ve yıla çevirme.
saniye = float(input("saniyeyi giriniz.:"))
print(saniye)
dakika = (saniye / 60)
print(dakika)
saat = (dakika / 60)
print(saat)
gün = (saat / 24)
print(gün)
ay = (gün / 30)
print(ay)
yıl = (ay / 12)
print(yıl)

print(int(yıl) , "Yıl" , " " , int(ay) ,"Ay" , " " , int(gün) ,"Gün" , " " , int(saat) , "Saat" , " " , int(dakika)  ,"Dakika", " " , int(saniye) , "Saniye")
