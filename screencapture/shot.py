import dxcam
import cv2
import time
from PIL import Image

camera = dxcam.create()
# camera.grab()

# frame = camera.grab()
# Image.fromarray(frame).show()

left, top = (1280 - 640) // 2, (1024 - 640) // 2
right, bottom = left + 640, top + 640
# mon = {'top': 100, 'left':200, 'width':1280, 'height':1024}


region = (left, top, right, bottom)
# region = int(mon)
frame = camera.grab(region=region)  # numpy.ndarray of size (640x640x3) -> (HXWXC)

Image.fromarray(frame).show()









# camera.start(region=(left, top, right, bottom))
# camera.is_capturing   # true
# # .....do something
# camera.stop()
# camera.is_capturing  # false


# # consume the screen Capture data
# camera.start()
# for i in range(1000):
#     image = camera.get_latest_frame()
# camera.stop()

# video_mode = True

# cam1 = dxcam.create(device_idx=0, output_idx=0)
# cam2 = dxcam.create(device_idx=0, output_idx=1)
# cam3 = dxcam.create(device_idx=1, output_idx=1)


# del cam1
# del cam2
# del cam3

# img1 = cam1.grab()
# img2 = cam2.grab()
# img3 = cam3.grab()

# info = dxcam.device_info()
# print(info)

# # specifying output format
# dxcam.create(output_idx=0, output_color="BGRA")

# # video buffer
# camera = dxcam.create(max_buffer_len=512)
# camera.start(target_fps=120)

# target_fps = 120
# camera = dxcam.create(output_idx=0, output_color="BGR")
# camera.start(target_fps=target_fps, video_mode=True)
# writer = cv2.VideoWriter(
#     "video.mp4", cv2.VideoWriter_fourcc(*"mp4v"), target_fps, (1920, 1080)
# )
# for i in range(600):
#     writer.write(camera.get_latest_frame())
# camera.stop()
# writer.release()

# camera1 = dxcam.create(output_idx=0, output_color="BGR")
# camera2 = dxcam.create(output_idx=0)  # Not allowed, camera1 will be returned
# camera1 is camera2  # True
# del camera1
# del camera2
# camera2 = dxcam.create(output_idx=0)  # Allowed

# start_time, fps = time.perf_counter(), 0
# cam = dxcam.create()
# start = time.perf_counter()
# while fps < 1000:
#     frame = cam.grab()
#     if frame is not None:  # New frame
#         fps += 1
# end_time = time.perf_counter() - start_time
# print(f"{title}: {fps/end_time}")

# camera = dxcam.create(output_idx=0)
# camera.start(target_fps=60)
# for i in range(1000):
#     image = camera.get_latest_frame()
# camera.stop()