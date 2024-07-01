import cv2

image=cv2.imread("Buz.jpg")

image[100,100]=[0,0,255]
#seçtiğimiz bir koordinatı kırmızıya boyadık

for i in range(200):
    image[200,i]=[0,0,0]
    for i in range(200):
        image[i,200]=[0,0,0]
#bir döngü ile seçtiğimiz koordinatlar arası bütün pixelleri siyah ile boyadık

cv2.line(image,(0,0),(900,720),(0,0,255),4)
cv2.line(image,(0,720),(900,0),(0,0,255),4)
#belirlediğimiz koordinatlar arasına çizgi çektik
cv2.rectangle(image,(370,290),(550,450),(0,0,255),4)
#seçtiğimiz iki nokta ile bir dörtgen oluşturduk
cv2.circle(image,(650,650),50,(0,0,255),4)
#veridiğimiz bir noktayı midpoint alararak 50 piksel yarıçapında kırmızı bir daire oluşturdu

cv2.imshow("Buz",image)

cv2.waitKey(0)
cv2.destroyAllWindows()