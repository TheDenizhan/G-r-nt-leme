import cv2
#OpenCV kütüphanesini çağırıyoruz

image=cv2.imread("OpenCV.png")
#cv2.imread("RESİM İSMİ") => fonksiyonu ile resmi okuyoruz

image0=cv2.imread("OpenCV.png",0)
#Eğer sonuna 0 yazılırsa o resmi otomatik gri yapar

cv2.imshow("Resim1",image)
#cv2.imshow("Açılacak pencerenin ismi",göstermek istediğiniz resim)

cv2.imshow("Resim2",image0)
#İkinci tanıdığımız resmi de gösteriyoruz

cv2.imwrite("OpenCV.Gri.png",image0)
#cv2.imwrite("KAYDEDİLECEK İSİM",kaydetmek istediğiniz resim) => resmi kaydediyoruz

cv2.waitKey(0)
#cv2.waitkey(0) => resmin ne kadar süre açık kalacağını seçiyoruz
#0 demek siz herhangi bir tuşa basmadan yada pencereyi kapatmadan kapanmıcak demektir
#İçerisine bir sayı girdiğinizde her yazılan değer milisaniye cinsindendir
#5000 girerseniz 5 saniye açık kalacak demektir

cv2.destroyAllWindows()
#Eğer sizin birden fazla pencereniz var ise hepsini kapatacak demektir

print(image)
print(image0)
#eğer resmi print ile yazdırırsak her bir pixelin aldığı renk değerini ekrana yazacaktır

print(image.size)
#resmin boyutunu ekrana yazdıracaktır

print(image.dtype)
#resmin bir pikselde ne kadar yer kapladığını yazdıracaktır

print(image.shape)
#(GENİŞLİK,YÜKSEKLİK,RENK)değerlerini yazdıracaktır

print(image[(50),(50)])
#belirlenen kordinatlardaki pikselin renk değerini yazdıracaktır
