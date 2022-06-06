# 허프 변환을 이용한 원 검출 예제

import cv2
import numpy as np

src = cv2.imread("sources/lec14/lec14_dial.jpg")
result = cv2.imread("sources/lec14/lec14_dial.jpg")
gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
# cv2.HOUGH_GRADIENT 방법 사용 시, 블러링 권장
blr = cv2.GaussianBlur(gray, (0, 0), 0.5)

circles = cv2.HoughCircles(blr, cv2.HOUGH_GRADIENT, 1, 50,
                            param1=120, param2=50,
                            minRadius=10, maxRadius=80)

for i in range(circles.shape[1]):
    cx, cy, radius = np.uint16(circles[0][i])
    cv2.circle(result, (cx, cy), radius, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow("src", src)
cv2.imshow("result", result)
cv2.imwrite("results/lec14/circles.jpg", src)
cv2.imwrite("results/lec14/houghCircles.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()