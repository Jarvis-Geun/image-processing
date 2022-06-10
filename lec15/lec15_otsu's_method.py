import cv2

src = cv2.imread("sources/lec15/lec15_rice.png", cv2.IMREAD_GRAYSCALE)

th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print("otsu's threshold:", th)  # 131

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imwrite("results/lec15/otsu's_method_src.jpg", src)
cv2.imwrite("results/lec15/otsu's_method_dst.jpg", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()