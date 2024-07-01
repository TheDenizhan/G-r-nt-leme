import cv2

image1=cv2.imread("Bitwise1.png")
image2=cv2.imread("bitwise2.png")

bit_and=cv2.bitwise_and(image1,image2)
#İki görüntüye and işlemi yapar:ikisi 1 ise 1 döner yoksa her koşul 0
bit_or=cv2.bitwise_or(image1,image2)
#iki görüntüye or işlemi yapar:işlemde 1 varsa 1 dir yoksa 0
bit_not=cv2.bitwise_not(image1)
#görüntüye not işlemi yapar:1 i 0 ,0 ı 1 yapar
bit_xor=cv2.bitwise_xor(image1,image2)
#iki görüntüye xor işlemi yapar:0,0ve 1,1 0dır, 0,1 ve 1,0 1 dir

cv2.imshow("image1",image1)
cv2.imshow("image2",image2)
cv2.imshow("bitAnd",bit_and)
cv2.imshow("bitOr",bit_or)
cv2.imshow("bitNot",bit_not)
cv2.imshow("bitXor",bit_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()