

"""import os

import cv2
from PIL import Image

a = 1
for i in range(0, 89):
    img = cv2.imread('unicorn_imgs/' + 'frame' + str(i) + '.jpg', 2)
    ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite('binary_uni/' + str(a) + '.jpg', bw_img)
    a += 1
"""