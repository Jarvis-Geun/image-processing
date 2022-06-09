import cv2

src = cv2.imread("sources/lec15/lec15_cells.png", cv2.IMREAD_GRAYSCALE)

def on_threshold(pos):
    _, dst = cv2.threshold(src, pos, 255, cv2.THRESH_BINARY)
    cv2.imshow("dst", dst)

cv2.imshow("src", src)
cv2.namedWindow("dst")
cv2.createTrackbar("Threshold", "dst", 0, 255, on_threshold)
cv2.setTrackbarPos("Threshold", "dst", 128)

cv2.waitKey(0)
cv2.destroyAllWindows()