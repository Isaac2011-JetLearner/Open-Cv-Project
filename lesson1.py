import cv2
store = cv2.imread("kobe.jpg",cv2.IMREAD_COLOR)#  the imread_color integer value is 1
cv2.imshow("Kobe",store)
cv2.waitKey(0)

store = cv2.imread("kobe.jpg",cv2.IMREAD_GRAYSCALE)# the imread_grayscale integer value is 0
cv2.imshow("Kobe",store)
cv2.waitKey(0)
cv2.imwrite("kobe_2.jpg",store)


store = cv2.imread("kobe.jpg",cv2.IMREAD_UNCHANGED)# the imread_unchanged integer value is -1
cv2.imshow("Kobe",store)
cv2.waitKey(0)

# You can print the image in diffrent colour formats

store =cv2.imread("kobe.jpg",cv2.IMREAD_COLOR)
print(store)
b,g,r = cv2.split(store)
cv2.imshow("Blue saturation image",b)
cv2.imshow("Green saturation image",g)
cv2.imshow("Red saturation image",r)
cv2.waitKey(0)


print(b,g,r)


