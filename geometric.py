import numpy as np
import cv2
my_img = np.zeros((400, 400, 3), dtype = "uint8")
# creating for line
cv2.line(my_img, (200, 10), (170, 40), (0, 0, 255), 10)
cv2.line(my_img, (200, 10), (230, 40), (0, 0, 255), 10)
cv2.line(my_img, (170, 40), (230, 40), (0, 0, 255), 10)

cv2.line(my_img, (180, 40), (130, 100), (0, 0, 255), 10)

cv2.line(my_img, (110, 80), (80, 110), (0, 0, 255), 10)
cv2.line(my_img, (110, 80), (140, 110), (0, 0, 255), 10)
cv2.line(my_img, (80, 110), (140, 110), (0, 0, 255), 10)

cv2.line(my_img, (130, 100), (230, 100), (0, 0, 255), 10)

cv2.line(my_img, (260, 80), (230, 110), (0, 0, 255), 10)
cv2.line(my_img, (260, 80), (290, 110), (0, 0, 255), 10)
cv2.line(my_img, (230, 110), (290, 110), (0, 0, 255), 10)

cv2.line(my_img, (210, 40), (250, 90), (0, 0, 255), 10)

cv2.imshow('Window', my_img)
cv2.waitKey(0)
cv2.destroyAllWindows()