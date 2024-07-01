import cv2

image=cv2.imread("Cat.png")
cv2.imshow("orjinal",image)
image2=cv2.imread("Cat.png")
image3=cv2.imread("Cat.png")
image4=cv2.imread("Cat.png")

image2[:,:,0]=180
#0 sarı 255 mavi olmak üzere bütün resmi o efekti uygular

image3[:,:,1]=0
#0 pembe 255 yeşil olmak üzere bütün resme o efekti uygular

image4[:,:,2]=0
#0 açık mavi 255 kırmızı olmak üzere bütün resme o efekti uygular

image[50:150,150:250,1]=0
#(50,150)noktasından(150,250) noktasına kadar o efekti uygular

kesit=image[50:150,150:250]
#(50,150)noktasından (150:250) noktasına olan kısmı alır
cv2.imshow("Part",kesit)
#kesilen alınan kesiti yazdırır

image[200:300,200:300]=kesit
#aldığımız kesiti (200,300) noktasıyla(200,300) noktasına yapıştırır

cv2.imshow("Result",image)
cv2.imshow("Blue",image2)
cv2.imshow("Green",image3)
cv2.imshow("Red",image4)

cv2.waitKey(0)
cv2.destroyAllWindows()