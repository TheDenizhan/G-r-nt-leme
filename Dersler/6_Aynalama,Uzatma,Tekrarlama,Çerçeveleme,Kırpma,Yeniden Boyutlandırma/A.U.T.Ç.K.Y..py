import cv2

image=cv2.imread("Tree.jpg")
Mirror=cv2.copyMakeBorder(image,200,200,200,200,cv2.BORDER_REFLECT)
#cv2.copyMakeBorder(RESİM,ÜST,ALT,SOL,SAĞ,YAPILACAK İŞLEM)
Replic=cv2.copyMakeBorder(image,200,200,200,200,cv2.BORDER_REPLICATE)
#cv2.copyMakeBorder(RESİM,ÜST,ALT,SOL,SAĞ,YAPILACAK İŞLEM)
Wrap=cv2.copyMakeBorder(image,200,200,200,200,cv2.BORDER_WRAP)
#cv2.copyMakeBorder(RESİM,ÜST,ALT,SOL,SAĞ,YAPILACAK İŞLEM)
Border=cv2.copyMakeBorder(image,50,50,50,50,cv2.BORDER_CONSTANT,value=(0,0,0))
#cv2.copyMakeBorder(RESİM,ÜST,ALT,SOL,SAĞ,YAPILACAK İŞLEM,BGR RENK DEĞERİ)
print("Normal boyut",Mirror.shape)
imgresize=cv2.resize(Mirror,(400,400))
#cv2.resize(RESİM,(X,Y)resmin dönüştürmek istediğiniz boyutu yazıyoruz
print("Yeniden işlenmiş boyut",imgresize.shape)

imgCropped=Mirror[100:600,300:600]
#belirlediğimiz alanı kesiyoruz

cv2.imshow("Mirror",Mirror)
cv2.imshow("Replic",Replic)
cv2.imshow("Wrap",Wrap)
cv2.imshow("Border",Border)
cv2.imshow("YeniBoyut",imgresize)
cv2.imshow("Cropped",imgCropped)

cv2.waitKey(0)
cv2.destroyAllWindows()