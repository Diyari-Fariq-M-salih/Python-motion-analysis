import cv2
import numpy as np
import os

img_dir = "Road/"   # <-- change this to your folder

# --- LOAD ALL IMAGES ---
images = []
for i in range(200):
    filename = f"{i:04d}.pgm"
    path = os.path.join(img_dir, filename)
    frame = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if frame is None:
        print("Missing:", path)
        continue
    images.append(frame.astype(np.float32))

# --- COMPUTE AVERAGE BACKGROUND ---
background = np.mean(images, axis=0).astype(np.float32)

cv2.imshow("Background (Average)", background / 255)
cv2.waitKey(0)
