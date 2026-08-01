import cv2
keep = cv2.imread("gliter_background.png",1)
cv2.imshow("gliter",keep)
img1 = cv2.resize(keep,(400,500))
cv2.imshow("gliter_resize",img1)
cv2.waitKey(0)

keep = cv2.imread("flowers-background.png",1)
cv2.imshow("flowers_background",keep)
img2 = cv2.resize(keep,(400,500))
cv2.imshow("flowers_resize",img2)
cv2.waitKey(0)

