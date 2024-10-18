# import pyautogui
# import time
# print("Press CTRL-C to quit")

# '''
# Для постоянного вывода текущих координат из mouse.position() можно использовать бесконечный цикл. А для кода завершающего программу нужно будет перехватить исключение KeyboardInterrupt, которое возникает всякий раз, когда пользователь нажимает CTRL-C.
# Если этого не сделать то try/exept отобразит уродливую строку сообщения об ошибке.
# И чтобы обработать цикл заключим его в  оператор try '''

# try:
#     while True:
#       # получение текущих координат
#       x, y = pyautogui.position()
#       # метод str(x) превращает число в строку а rjust(4) сдвигает его на четыре позиции вправо
#       positionStr = 'X:'+ str(x).rjust(4) +'  Y:'+ str(y).rjust(4)
#       # end предотвращает добавление символа новой строки,  без  этого старые координаты удалить не получится
#       print(positionStr, end = '')
     
#       # escape-символ \ b стирает конец строки и чтобы удалить всю строку умножаем его на длину строки
#       print('\b'*len(positionStr), end = '', flush = True)
     
#       # для предотвращения мигания при выполнении цикла используем засыпание
#       time.sleep(0.01)



# # Когда пользователь нажимает CTRL-C, выполнение программы переходит к разделу except и # Done будет напечатан с новой строки

# except KeyboardInterrupt:
#     print('\nDone')
# import cv2 as cv
# import numpy as np

# # Создаем пустое изображение
# img = np.zeros((400, 400, 3), dtype=np.uint8)

# # Повернутый прямоугольник
# rect1 = ((200, 200), (150, 100), 0) 
# rect = ((200, 200), (150, 100), 30)  # Центр, размеры, угол поворота

# # Получаем 4 вершины
# box = cv.boxPoints(rect)
# box = np.int0(box)
# box1= cv.boxPoints(rect1)
# box1 = np.int0(box1)

# # Рисуем точки на каждой вершине
# # for point in box:
# #     cv.circle(img, tuple(point), 5, (0, 0, 255), -1)
# cv.drawContours(img, [box1], 0, (0, 255, 0), 2)
# for point1 in box1:
#     cv.circle(img, tuple(point1), 5, (0, 0, 255), -1)
# # Показываем изображение
# cv.imshow("Rotated Rect Points", img)
# cv.waitKey(0)
# cv.destroyAllWindows()
# import cv2
# import numpy as np
# import math
# import cos
# # Читаем изображение
# image = cv2.imread('image.png')
# image2 = cv2.imread('image2.png')
# # Преобразуем изображение в HSV
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# hsv2 = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)
# # Задаем диапазон для красного цвета (в HSV)
# lower_red = np.array([0, 50, 50])     # нижняя граница красного цвета
# upper_red = np.array([10, 255, 255])  # верхняя граница красного цвета
# mask1 = cv2.inRange(hsv, lower_red, upper_red)
# mask3 = cv2.inRange(hsv2, lower_red, upper_red)

# lower_red = np.array([170, 50, 50])   # нижняя граница для более "темного" красного
# upper_red = np.array([180, 255, 255]) # верхняя граница для более "темного" красного
# mask2 = cv2.inRange(hsv, lower_red, upper_red)
# mask4 = cv2.inRange(hsv2, lower_red, upper_red)
# # Комбинируем маски
# mask = mask1 + mask2
# mask02 = mask3+mask4

# # Применяем морфологическую операцию, чтобы улучшить результат (например, закрытие маленьких дыр)
# mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
# mask02 = cv2.morphologyEx(mask02, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
# # Находим контуры на маске
# contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# contours2, _ = cv2.findContours(mask02, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# # Обрабатываем каждый контур
# for contour, contour2 in zip(contours, contours2):
#     # Вычисляем минимальный ограничивающий прямоугольник для каждого контура
#     x, y, w, h = cv2.boundingRect(contour)
#     x1, y1, w1, h1 = cv2.boundingRect(contour2)
#     # Находим центр контуров
#     center_x = x + w // 2
#     center_y = y + h // 2
#     center_x1 = x1 + w1 //2
#     center_y1 = y1 + h1 //2
#     vec_len = np.sqrt(math.pow((center_x - center_x1),2) + math.pow((center_y - center_y1),2))
     
#     cosA = cos.cosAlpha(vec_len) 
#     # Выводим координаты центра
#     print(f"Координаты красной точки: x = {center_x}, y = {center_y}")
#     print(f"Координаты красной точки: x = {center_x1}, y = {center_y1}")
#     print(f"Координаты красной точки вектора: {vec_len}")
#     print(f"Угол поворота: {cosA}")

#     # Отмечаем центр на изображении для проверки
#     cv2.circle(image, (center_x, center_y), 5, (255, 0, 0), -1)  # Синие круги
#     cv2.circle(image, (center_x1, center_y1), 5, (0, 0, 255), -1)  # Синие круги
# # Показываем изображение с отмеченными центрами точек
# cv2.imshow("Detected Points", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2
import numpy as np
import math
import cos
import time
# Открываем видео
video = cv2.VideoCapture(0)
arr = []  
# Задаем диапазон для красного цвета (в HSV)
# measured_once = False

lower_red = np.array([0, 150, 150])     # нижняя граница яркого красного
upper_red = np.array([10, 255, 255])    # верхняя граница яркого красного
lower_red2 = np.array([350, 150, 150])   # нижняя граница темного красного
upper_red2 = np.array([360, 255, 255])   # верхняя граница темного красного
# lower_purple = np.array([125, 100, 100])  # нижняя граница для фиолетового
# upper_purple = np.array([145, 255, 255])  # верхняя граница для яркого фиолетового

# # Нижняя и верхняя границы для более темного фиолетового цвета в HSV
# lower_purple2 = np.array([146, 100, 100])  # нижняя граница для темного фиолетового
# upper_purple2 = np.array([160, 255, 255])  # верхняя граница для темного фиолетового
while True:
    ret, frame = video.read()
    if not ret:
        break  # Выход, если видео завершилось
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1+mask2

    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # # Обрабатываем каждый контур
    for contour in contours:
        # Находим минимальный ограничивающий прямоугольник
        x, y, w, h = cv2.boundingRect(contour)
        # box = cv2.boxPoints(contour)
        # box = np.int0(box)
        # # Находим центр контура
        center_x = x + w // 2
        center_y = y + h // 2
        # arr.append((center_x, center_y))

        # # Если есть предыдущие координаты, считаем расстояние
        # if len(arr) > 1:
        #     vec_len = np.sqrt((arr[-1][0] - arr[-2][0])**2 + (arr[-1][1] - arr[-2][1])**2)
        #     cosAlp = cos.cosAlpha(vec_len)
        #     print(f"Угол отклонения: {cosAlp}")
        #     print(f"Длина вектора между точками: {vec_len}")
            
        # Отмечаем центр на кадре
        lenght = cv2.arcLength(contour, True)
        print(contour)
        print(lenght)

        cv2.drawContours(frame, [contour], 0, (0, 0, 255), 2)
        cv2.approxPolyDP(contour, 0.01*lenght, True)
        cv2.circle(frame, (center_x, center_y), 5, (255, 0, 0), -1)  # Синие круги
    result = cv2.bitwise_and(frame, frame, mask = mask)

    # Преобразуем кадр в HSV
    # Показываем кадр с отмеченными точками
    cv2.imshow("Bitwise", result)
    cv2.imshow("Tracking", frame)

    # Прерываем цикл при нажатии клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# Освобождаем ресурсы
video.release()
cv2.destroyAllWindows()
# import cv2
# import numpy as np
# import time
# import cos
# import asyncio
# # Определение диапазона красного цвета в HSV
# lower_red = np.array([0, 150, 150])     # нижняя граница яркого красного
# upper_red = np.array([10, 255, 255])    # верхняя граница яркого красного
# lower_red2 = np.array([350, 150, 150])   # нижняя граница темного красного
# upper_red2 = np.array([360, 255, 255])   # верхняя граница темного красного
# arr = []
# # Захват видео с камеры
# cap = cv2.VideoCapture(0)

# async def process_video():
#     cap = cv2.VideoCapture(0)

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Преобразование изображения из BGR в HSV
#         hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#         # Маска для первого диапазона красного
#         mask1 = cv2.inRange(hsv, lower_red, upper_red)

#         # Маска для второго диапазона красного
#         mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

#         # Объединяем маски
#         mask = mask1 + mask2

#         # Применяем маску на изображение
#         contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Обрабатываем каждый контур
#         for contour in contours:
#         # Находим минимальный ограничивающий прямоугольник
#             x, y, w, h = cv2.boundingRect(contour)

#         # Находим центр контура
#             center_x = x + w // 2
#             center_y = y + h // 2
#             arr.append((center_x, center_y))
#             cv2.circle(frame, (center_x, center_y), 5, (255, 0, 0), -1)
#         # Отображаем оригинальное изображение и результат
#         cv2.imshow("Original", frame)
#         # Асинхронная пауза на 1 секунду
#         await asyncio.sleep(1)

#         # Нажмите 'q' для выхода
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# # Основная функция
# async def main():
#     await process_video()

# # Запуск программы
# asyncio.run(main())