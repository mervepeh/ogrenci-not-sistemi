def ortalamanot_Hesapla(satir):
    
  satir=satir[:-1]
  liste=satir.split(":")
  ogrenci_adi=liste[0]
  yazili=liste[1].split(",")

  yazili1=int(yazili[0])
  yazili2=int(yazili[1])
  yazili3=int(yazili[2])


  ortalamanot=(yazili1+yazili2+yazili3)/3

  if ortalamanot>=90 and ortalamanot<=100:
        harfnotu = "AA Gecti"
  elif ortalamanot>=85 and ortalamanot<=89:
        harfnotu = "BA Gecti"
  elif ortalamanot>=80 and ortalamanot<=84:
        harfnotu = "BB Gecti"
  elif ortalamanot>=75 and ortalamanot<=79:
        harfnotu = "CB Gecti"
  elif ortalamanot>=70 and ortalamanot<=74:
        harfnotu = "CC Gecti"
  elif ortalamanot>=65 and ortalamanot<=69:
        harfnotu = "DC Kosullu Gecti"
  elif ortalamanot>=60 and ortalamanot<=64:
        harfnotu = "DD Kosullu Gecti"
  elif ortalamanot>=50 and ortalamanot<=59:
        harfnotu = "FD Kaldi"
  else:
        harfnotu = "FF Kaldi"

  return ogrenci_adi+ ":" + harfnotu + "\n"
def ortalamanot_oku(): 
  with open("ogrenci_yazilinot.txt","r",encoding="utf-8") as file: 
    for satir in file: 
        print(ortalamanot_Hesapla(satir))

def yazili_Girisi(): 
  adi=input("Ogrencinin adi:") 
  soyadi=input("Ogrencinin soyadi:") 
  yazili1=input("Ogrenci 1.yazili:") 
  yazili2=input("Ogrenci 2.yazili:")
  yazili3=input("Ogrenci 3.yazili:")


  with open("ogrenci_yazilinot.txt","a",encoding="utf-8") as file:
    file.write(adi+" "+soyadi+":"+yazili1+","+yazili2+","+yazili3+"\n")

def yazili_Kaydet(): 

  with open("ogrenci_yazilinot.txt","r",encoding="utf-8") as file: 
    liste=[] 
    for i in file: 
      liste.append(ortalamanot_Hesapla(i))

  with open("harf_notlari.txt","r",encoding="utf-8") as file: 
    liste=[] 
    for i in file: 
      liste.append(ortalamanot_Hesapla(i))


print(" OGRENCİ NOT KAYIT SISTEMINE HOS GELDINIZ ") 


while True: 
  secim=input("1- Ogrenci Girisi\n2- Notları Gör\n3- Notları Kaydet\n4- Çıkış Yap\n\n")

  if int(secim)==1:
    yazili_Girisi()

  elif int(secim)==2:
    ortalamanot_oku()


  elif int(secim)==3:
    yazili_Kaydet()
    print("YAZILI KAYDEDILDI")


  else:
    print("SISTEM SONLANDIRILDI")
    break