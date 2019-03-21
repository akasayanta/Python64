
#SORU 1
h=5
a=6
def dik_ucgen():
    alan=a*h/2
    return alan
def kare():
    alan=a*a
    return alan
def dortgen():
    alan =a*h
    return alan



print("Hangisi ile işlem yapmak isrtersiniz?")
print("Dik üçgen(u)")
print("Kare(k)")
print("Dikdörtgen(d)")
islem=input()

if (islem=="u" or islem=="U"):
    print("Üçgenin alanı=",dik_ucgen())
elif(islem=="k" or islem=="K"):
    print("Karenin alanı =",kare())
elif(islem=="D" or islem=="d"):
    print("Dikdörtgenin alanı =",dortgen())
else:
    print("Liste dışı bir karaktere bastınız")
# ------------------------------------------------------


#soru 2
def isim(ad,sad):
    name=ad+" "+sad
    return name

ad=input("İsminiz = ")
sad=input("Soy isminiz = ")
print(isim(ad,sad))

# ------------------------------------------------------


#soru 3
toplam=0
adet=0
kucuk_adet=0
devam=1
while(devam):
    sayi=int(input("Sayı giriniz ="))
    adet = adet+1
    if(sayi>50):
       toplam = toplam+sayi
    elif(sayi<50):
        kucuk_adet=kucuk_adet+1
    else:
        print("Girdiğiniz",adet,"sayının 50'den büyük olanların toplamı=",toplam)
        print("Girdiğiniz",adet,"sayının",kucuk_adet,"tanesi 50'den küçüktür")
        devam=0
# ------------------------------------------------------


#soru 4
def fak(sayi):
    if (sayi==0):
        return 1
    else:

        return sayi*fak(sayi-1)

sayi=int(input("Hangi sayının faktöriyeli lazım ?"))

print(sayi,"sayısının faktöriyeli =",fak(sayi))


#-------------------------------------------------------------
#soru 5
import random

sayi=random.randint(0,100)
print(sayi)
deneme=0
bulma=1
print("Bir sayı tuttum.Bakalım kaç denemede bulabileceksin?")
while(bulma):
    dene=int(input("Bir sayı yaz"))
    deneme=deneme+1
    if dene==sayi:
        print("Tebrikler...Sayıyı",deneme,". denemenizde buldunuz")
        bulma=0
    else:
        print("Malesef bulamadın.Tekrar dene.")