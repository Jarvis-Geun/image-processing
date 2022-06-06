# 차선 검출
# Canny edge detection 및 Hough transform을 이용한 차선 검출 알고리즘 구현

import cv2
import numpy as np

src = cv2.imread("sources/lec14/lec14_lanes.jpg")
dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(dst, 50, 150)
lines = cv2.HoughLinesP(edges, 1.0, np.pi / 180., 70,
                        minLineLength=80, maxLineGap=7)

if lines is not None:
    for i in range(lines.shape[0]):
        pt1 = (lines[i][0][0], lines[i][0][1])
        pt2 = (lines[i][0][2], lines[i][0][3])
        cv2.line(src, pt1, pt2, (255, 0, 0), 2, cv2.LINE_AA)

cv2.imshow("src", src)
cv2.imwrite("results/lec14/lanes_src.jpg", src)
cv2.waitKey(0)
cv2.destroyAllWindows()