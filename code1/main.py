import cv2 as cv
import numpy as np

img = cv.imread('honkai_field_right.jpg', cv.IMREAD_UNCHANGED)
pointer_img = cv.imread('goal_right.jpg', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(img, pointer_img, cv.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print('Best match top left position: %s' % str(max_loc))
print('Best match confidence: %s' % max_val)

# threshold = 0.8
# if 


# cv.imshow('Result', result)
# cv.waitKey()