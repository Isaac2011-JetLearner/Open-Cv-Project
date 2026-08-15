import cv2
pika_img = cv2.imread("pika.png",1)
cv2.imshow("pika",pika_img)

#convertion to a grayscale image
gray_pika = cv2.cvtColor(pika_img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray pikachu", gray_pika)

#convertion to a hsv image
# h = hue, hue is the colour, S = saturation, saturation is the intensity of the colour and v = value, value is the brightness of the image
hsv_pika = cv2.cvtColor(pika_img,cv2.COLOR_BGR2HSV)
cv2.imshow("hsv_pikachu",hsv_pika)
cv2.waitKey(0)


