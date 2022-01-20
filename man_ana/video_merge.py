import cv2
import numpy as np
from itertools import count


vid_bg = 'bg.mp4'
vid_fg = 'ManAna.mp4'
cap_bg = cv2.VideoCapture(vid_bg)
cap_fg = cv2.VideoCapture(vid_fg)
w, h = 3840, 2160
fps = 60
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

writer = cv2.VideoWriter("man_ana_final.mp4", fourcc, fps, (w, h))


def get_weight_matrix(frame):
    mid_point = h // 2
    col = np.absolute(np.array(range(h)) - mid_point)
    weight_matrix = np.zeros((h, w), dtype=float)
    for c in range(w):
        weight_matrix[:, c] = col[:]
    weight_matrix = weight_matrix / mid_point
    weight_matrix = cv2.merge((weight_matrix, weight_matrix, weight_matrix))
    return 1 - weight_matrix


last_frame_bg = None
last_frame_fg = None
for i in count():
    ret1, frame_bg = cap_bg.read()
    ret2, frame_fg = cap_fg.read()

    if not ret1 and not ret2:
        break

    if frame_bg is None:
        frame_bg = last_frame_bg
    else:
        last_frame_bg = frame_bg

    if frame_fg is None:
        frame_fg = last_frame_fg
    else:
        last_frame_fg = frame_fg

    try:
        frame_fg = frame_fg * weight_matrix
    except NameError:
        weight_matrix = get_weight_matrix(frame_bg.copy())
        frame_fg = frame_fg * weight_matrix
    finally:
        frame_fg = frame_fg.astype(np.uint8)
        frame = np.maximum(frame_fg, frame_bg)

    writer.write(frame.copy())


cap_bg.release()
cap_fg.release()
writer.release()
