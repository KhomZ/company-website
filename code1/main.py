import cv2 as cv2
import numpy as np

img = cv.imread('honkai_field_right.jpg', cv.IMREAD_UNCHANGED)
pointer_img = cv.imread('honkai_goal_right.jpg', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(img, pointer_img, cv.TM_CCOEFF_NORMED)

cv.imshow('Result', result)