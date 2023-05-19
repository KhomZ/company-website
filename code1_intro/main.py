import cv2 as cv
import numpy as np
import time

# img = cv.imread('honkai_field_right.jpg', cv.IMREAD_UNCHANGED)
# pointer_img = cv.imread('goal_right.jpg', cv.IMREAD_UNCHANGED)

img = cv.imread('honkai_field_right.jpg', cv.IMREAD_REDUCED_COLOR_2)
pointer_img = cv.imread('goal_right.jpg', cv.IMREAD_REDUCED_COLOR_2)

# img = cv.imread('honkai_field_left.jpg', cv.IMREAD_UNCHANGED)
# pointer_img = cv.imread('goal_left.jpg', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(img, pointer_img, cv.TM_CCOEFF_NORMED)

# get the best match positions
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)  # 0=blackest value, 1=brightest white

print('Best match top left position: %s' % str(max_loc))
print('Best match confidence: %s' % max_val)

threshold = 0.7
if max_val >= threshold:
    print('found pointer')

    # get the dimensions of the pointer image
    pointer_w = pointer_img.shape[1]
    pointer_h = pointer_img.shape[0]

    top_left = max_loc
    bottom_right = (top_left[0] + pointer_w, top_left[1] + pointer_h)

    cv.rectangle(img, top_left, bottom_right,
                 color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
    
    # cv.imshow('Result', img)
    # cv.waitKey()
    cv.imwrite('result.jpg', img)


else:
    print('Pointer not found')



# debug code
# cv.imshow('Result', result)
# cv.waitKey()