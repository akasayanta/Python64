'''
 #1.soru
sayi=input("Bir sayı giriniz =")
print(sayi)
#-----------------------------------------------------------
#2.soru
isim=input("Adınızı yazınız =")
print(isim)
#-----------------------------------------------------------
#3.soru
say1=int(input("1. sayıyı giriniz ="))
say2=int(input("2. sayıyı giriniz ="))
toplam=say1+say2
fark=say1-say2
carp=say1*say2
bol=say1//say2
print("Bu Sayıların Toplamı = ",toplam)
print("Bu Sayıların Farkı = ",fark)
print("Bu Sayıların Çarpımıı = ",carp)
print("Bu Sayıların Bölümü = ",bol)
print("Bu sayıların ortalaması =",toplam//2)
#-----------------------------------------------------------
#5.soru
kontrol=1
while(kontrol):
    vize = int(input("VİZE NOTUNU GİRİNİZ = "))
    if (vize>100 or vize<0):
        print("Vize notunu yanlış girdiniz.Lütfen tekrar giriniz.")
    else:
        break
while(kontrol):
    final=int(input("FİNAL NOTUNU GİRİNİZ ="))
    if(final>100 or final<0):
        print("Final Notunu yanlış girdiniz.Lütfen tekrar giriniz.")
    else:
        break
ortalama=vize*30/100+final*70/100
print("Not ortalamanız =",ortalama)
#-----------------------------------------------------------
#6.Soru
boy=float(input("Boyuuzu nedir ? "))
kilo=float(input("Kilonuz nedir ? "))
index=kilo//(boy**2)
print("Vücut kitle index değeriniz = ",index)
#-----------------------------------------------------------
#7.Soru
say1=int(input("1. sayı = "))
say2=int(input("2. sayı ="))
print("Birinci sayı = ",say1)
print("İkinci sayı = ",say2)
yedek=say1
say1=say2
say2=yedek
print("Birinci Sayı = ",say1)
print("İkinci sayı = ",say2)
#-----------------------------------------------------------
#8.Soru
taban=int(input("Üçgenin taban uzunluğu kaç cm ?"))
yuksek=int(input("üçgenin yüksekliği kaç cm ?"))
alan=taban*yuksek/2
print("üçgenin alanı = ",alan)
#-----------------------------------------------------------
#9.Soru
r=int(input("Direnç değeri kaç ohm ?"))
V=int(input("Gerilim kaç volt ?"))
I=V/r
print("Akım = ",I,"amper")
#-----------------------------------------------------------
#10.Soru
ad=input("Adınız =")
yas=int(input("Yaşınız ="))
print(ad*yas)
#-----------------------------------------------------------
#11.Soru
say = [0,1,2,3,4,5,6,7,8,9]
toplam=0
ort=0
for i in range(10):
    print(i+1,". Sayıyı Giriniz = ")
    sayi=input()
for x in range(10):
    toplam=toplam+int(say[x])
ort=toplam/10
print("Sayıların toplamı = ",toplam)
print("Sayıların ortaaması = ",ort)
#-----------------------------------------------------------
#12.Soru
toplam=0
say=int(input("Bir sayı giriniz = "))
if (say>=0 and say<=100):
    toplam=toplam+say
    while (say >= 0 and say <= 100):
        say = int(input("Bir sayı giriniz = "))
        if(say>0 or say<100):
            toplam = toplam + say
        else:
            break
    toplam=toplam-say
else:
    print("0-100 arasında sayı girmediğiniz için program sonlandı")
print("Sayıların toplamı =",toplam)
'''
#-----------------------------------------------------------
#13.Soru
turSayGel=0
turSayGit=0
sor="E"
katilan=0
print("Turnuvaya katılabilmeniz için soruları yanıtlamalısınız")
while(sor=="e" or sor=="E"):
    sayac = 0
    yanit1=input("Soru1 (E/H) =")
    if (yanit1=="e" or yanit1=="E"):
        sayac=sayac+1
    yanit2=input("Soru1 (E/H) =")
    if (yanit2=="e" or yanit2=="E"):
        sayac=sayac+1
    yanit3=input("Soru1 (E/H) =")
    if (yanit3=="e" or yanit3=="E"):
        sayac=sayac+1
    yanit4=input("Soru1 (E/H) =")
    if (yanit4=="e" or yanit4=="E"):
        sayac=sayac+1
    yanit5=input("Soru1 (E/H) =")
    if (yanit5=="e" or yanit5=="E"):
        sayac=sayac+1
    katilan=katilan+1
    if (sayac >= 3):
        print("Turnuvaya kazanmaya hak kazandınız")
        turSayGel = turSayGel + 1
    else:
        print("Turnuvaya katılamazsınız")
    if (turSayGel==50):
        print("Birinci grup oluşturuldu ")
    elif(turSayGel==100):
        print("İkinci grup oluşturuldu")
        break
    else:
        print("Henüz grup oluşturacak kadar katılımcı yok")

    sor = input("Turnuvaya katılmak isteyen başka birisi var mı")

print("Turnuvaya katılmak için toplam",katilan,"kişi başvurmasına rağmen")
print(turSayGel,"kişi turnuvaya katılabilecektir.")