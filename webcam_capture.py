# webcam_capture.py

import cv2

# def capture_webcam_image(camera_index=0):
#     try:
#         cap = cv2.VideoCapture(camera_index)
#
#         # Check if the camera is opened successfully
#         if not cap.isOpened():
#             raise cv2.error("Error: Could not open the webcam.")
#
#         ret, frame = cap.read()
#         cap.release()
#         return frame
#     except cv2.error as e:
#         print(e)
#         return None

# webcam_capture.py


def capture_webcam_image(camera_index=0):
    try:
        cap = cv2.VideoCapture(camera_index)

        # Check if the camera is opened successfully
        if not cap.isOpened():
            raise cv2.error("Error: Could not open the webcam.")

        ret, frame = cap.read()
        cap.release()
        return frame
    except cv2.error as e:
        if "Camera index out of range" in str(e):
            print("Warning: No webcam found. Running without webcam.")
        else:
            print(e)
        return None
