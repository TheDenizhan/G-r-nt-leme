import cv2

image=cv2.imread("Love.jpg")
image2=cv2.imread("photo.jpg")

print(image.shape)
print(image2.shape)
#iki resmin boyutlarını alıyoruz eğer iki resim boyutu eşit değilse birleştirildiğinde hata vericektir

print("image1 pixel değeri",image[150,300])
print("image2 pixel değeri",image2[150,300])
#iki resimden seçtiğimiz kordinatlardaki renk değerlerini yazdırıyoruz

cv2.imshow("image",image)
cv2.imshow("image2",image2)

print(image[150,300]+image2[150,300])
#iki resimden aldığımnız pixel değerlerini topluyoruz

Add=cv2.add(image,image2)
#iki resim boyutları eşit ise toplanır
Add2=cv2.addWeighted(image,0.75,image2,0.25,0)
#cv2.addWeighted(RESİM,ORAN,2.RESİM,ORAN,PARLAKLIK)

cv2.imshow("Add",Add)
cv2.imshow("Add2",Add2)

cv2.waitKey(0)
cv2.destroyAllWindows()