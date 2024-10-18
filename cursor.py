import cv2 as cv
import numpy as np

# Создаем пустое изображение
img = np.zeros((400, 400, 3), dtype=np.uint8)

# Повернутый прямоугольник
rect1 = ((200, 200), (150, 100), 0) 
rect = ((200, 200), (150, 100), 30)  # Центр, размеры, угол поворота

# Получаем 4 вершины
box = cv.boxPoints(rect)
box = np.int0(box)
box1= cv.boxPoints(rect1)
box1 = np.int0(box1)

# Рисуем точки на каждой вершине
# cv.drawContours(img, [box], 0, (0, 255, 0), 2)
# for point in box:
#     cv.circle(img, tuple(point), 5, (0, 0, 255), -1)
cv.drawContours(img, [box1], 0, (0, 255, 0), 2)
for point1 in box1:
    cv.circle(img, tuple(point1), 5, (0, 0, 255), -1)
# Показываем изображение
cv.imshow("Rotated Rect Points", img)
cv.waitKey(0)
cv.destroyAllWindows()