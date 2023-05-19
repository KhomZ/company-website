# from mss import mss
import dxcam
import cv2
from PIL import Image
import numpy as np
from time import time

mon = {'top': 100, 'left':200, 'width':1280, 'height':1024}

# sct = mss()
sct = dxcam.create()

while 1:
    begin_time = time()
    sct_img = sct.grab(mon)
    img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
    img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    cv2.imshow('test', np.array(img_bgr))
    print('This frame takes {} seconds.'.format(time()-begin_time))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break


# 1280x1024 widthxheight


# from mss import mss
# import cv2
# from PIL import Image
# import numpy as np
# from time import time

# mon = {'top': 100, 'left':200, 'width':1600, 'height':1024}

# sct = mss()

# while 1:
#     begin_time = time()
#     sct_img = sct.grab(mon)
#     img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
#     img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
#     cv2.imshow('test', np.array(img_bgr))
#     print('This frame takes {} seconds.'.format(time()-begin_time))
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break