import cv2

capture = cv2.VideoCapture(0)

if capture.isOpened() == False:
    raise Exception("카메라 연결 x")

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    cv2.imshow("해윙", frame)
    
capture.release()