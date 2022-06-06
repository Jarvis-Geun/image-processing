import cv2
import numpy as np

path = "sources/lec14/lec14_iris.jpg"
src = cv2.imread(path)
# src = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blr = cv2.GaussianBlur(gray, (0, 0), 0.5)

circles = cv2.HoughCircles(blr, cv2.HOUGH_GRADIENT, 1, 50,
                            param1=120, param2=50,
                            minRadius=10, maxRadius=65)

for i in range(circles.shape[1]):
    cx, cy, radius = np.uint16(circles[0][i])
    # 원 그리기 (초록색)
    cv2.circle(src, (cx, cy), radius, (0, 255, 0), 2, cv2.LINE_AA)
    # 중심점 그리기 (빨간색)
    cv2.circle(src, (cx, cy), 5, (0, 0, 255), -1, cv2.LINE_AA)

cv2.imshow("src", src)
cv2.imwrite("results/lec14/iris.png", src)
cv2.waitKey(0)