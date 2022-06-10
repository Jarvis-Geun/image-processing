import cv2

src = cv2.imread("sources/lec16/lec16_circuit.bmp", cv2.IMREAD_GRAYSCALE)

# se : structuringe element
se = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
dst1 = cv2.erode(src, se)
dst2 = cv2.dilate(src, None)

cv2.imshow("src", src)
cv2.imshow("erosion", dst1)
cv2.imshow("dilation", dst2)

cv2.imwrite("results/lec16/circuit_src.jpg", src)
cv2.imwrite("results/lec16/circuit_erosion.jpg", dst1)
cv2.imwrite("results/lec16/circuit_dilation.jpg", dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()