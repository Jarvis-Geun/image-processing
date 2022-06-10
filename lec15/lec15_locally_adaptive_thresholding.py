import cv2

src = cv2.imread("sources/lec15/lec15_sudoku.jpg", cv2.IMREAD_GRAYSCALE)

def on_trackbar(pos):
    bsize = pos
    if bsize % 2 == 0:
        bsize = bsize - 1
    if bsize < 3:
        bsize = 3
    
    dst = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY, bsize, 5)
    cv2.imshow("dst", dst)
    cv2.imwrite("results/lec15/sudoku_dst.jpg", dst)

cv2.imshow("src", src)
cv2.namedWindow("dst")
cv2.createTrackbar("Block Size", "dst", 0, 200, on_trackbar)
cv2.setTrackbarPos("Block Size", "dst", 11)
cv2.imwrite("results/lec15/sudoku_src.jpg", src)
cv2.waitKey(0)
cv2.destroyAllWindows()