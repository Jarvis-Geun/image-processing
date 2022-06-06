# 확률적 허프 변환을 이용한 직선 검출 예제

import cv2
import numpy as np

src = cv2.imread('sources/lec14/lec14_building.jpg', cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(src, 50, 150)
lines = cv2.HoughLinesP(edges, 1.0, np.pi / 180., 160,
                        minLineLength=50, maxLineGap=5)

# edges를 bgr 형태로 바꿔주지 않으면 line을 그려도 흑백으로 출력됨
dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

if lines is not None:
    for i in range(lines.shape[0]):
        pt1 = (lines[i][0][0], lines[i][0][1])  # 시작점 좌표
        pt2 = (lines[i][0][2], lines[i][0][3])  # 끝점 좌표
        cv2.line(dst, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imwrite("results/lec14/houghP_src.jpg", src)
cv2.imwrite("results/lec14/houghP_dst.jpg", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()