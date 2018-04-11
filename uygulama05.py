import random
import sys
file = open('kelimelistesi.txt', "r")
sozluk = file.read().split()
file.close()

sozlukboyutu = len(sozluk)
kelime = sozluk[random.randint(0, sozlukboyutu)]

uzunluk=len(kelime)
bil=[]
dizi=dict()

f = ['' for x in range(uzunluk)]

def displayword(characterlist):

    for i in characterlist:
        if i == '':
            print ("-"),
        else:
            print(i)

def varyok(harf, sayac):
    if(harf in kelime):
        print("harf mevcut")
        characterpos=[pos for pos, char in enumerate (kelime) if char==harf]

        for x in characterpos:
            dizi[x] = harf
            f[x] = harf
        #print(f)
        displayword(f)


        if(sorted(f)==sorted(kelime)):
            print("Tebrikler ")
            sys.exit()
        else:
            a=input("\nYeni bir harf giriniz: ")
            varyok(a, sayac)
            print("\n")
    else:
        if(sayac==0):
            print("\n"+str(f)+"\n7 canın kaldı")
            sayac=sayac+1
            a=input("Yeni bir harf giriniz:\n\n")
            varyok(a, sayac)
        if(sayac==1):
            print(f)
            print(" 6 canın kaldı")
            sayac=sayac+1
            a=input("Yeni bir harf giriniz:\n")
            varyok(a, sayac)
        if(sayac==2):
            print(f)
            print("5 canın kaldı")
            sayac=sayac+1
            a=input("Yeni bir harf giriniz:\n")
            varyok(a, sayac)
        if(sayac==3):
            print(f)
            print("4 canın kaldı")
            sayac=sayac+1
            a=input("Yeni bir harf giriniz:\n")
            varyok(a, sayac)
        if(sayac==4):
            print(f)
            print(" 3 canın kaldı")
            sayac=sayac+1
            a=input("Yeni bir harf giriniz:\n")
            varyok(a, sayac)
        if(sayac==5):
            print(f)
            print("2 canın kaldı")
            sayac=sayac+1
            a=input("Yeni bir harf giriniz:\n")
            varyok(a, sayac)
        if(sayac==6):
            print(f)
            print(" 1 canın kaldı")
            sayac=sayac+1
            a=input("Yeni bir harf giriniz:\n")
            varyok(a, sayac)
        if(sayac>6):
            print(f)
            print("Oyunu kaybettiniz. Doğru cevap: " + kelime)
            sys.exit()


print("Adam asmaca oyununa hosgeldiniz.");
print(f);
harf=input("\nBir harf giriniz: ")
varyok(harf, 0)
