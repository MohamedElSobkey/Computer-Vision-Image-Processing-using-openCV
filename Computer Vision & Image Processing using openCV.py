import cv2

print(cv2.__version__)

img= cv2.imread("./apple.jpg",0) # 0 for grayscale
                                 # 1 for color
                                 # -1 for alpha channel "unchangeable"
                                 
print(img)                                 

cv2.imshow("First Image" , img)                                 
k = cv2.waitKey(0)

if k == 27 :
     cv2.destroyAllwindows()
elif k == ord('S') :
       cv2.imwrite('Sec Image.jpg', img )
       cv2.destroyAllwindows()