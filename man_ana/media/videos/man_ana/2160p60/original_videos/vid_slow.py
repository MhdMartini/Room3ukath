import cv2

vid_name = 'production ID_4999943.mp4'
cap = cv2.VideoCapture(vid_name)
w, h = 3840, 2160
fps = 60
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

writer = cv2.VideoWriter(f"slow_{vid_name}", fourcc, fps, (w, h))


idx = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    idx += 1
    num_frames = 1 if idx < 100 else 8
    for _ in range(num_frames):
        writer.write(frame.copy())

cap.release()
writer.release()
