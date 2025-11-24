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

# ------------------------------------------------------------
# STEP 1 — AVERAGE BACKGROUND
# ------------------------------------------------------------
background_avg = np.mean(images, axis=0).astype(np.float32)

# Show the average background
cv2.imshow("Background (Average)", background_avg / 255)
cv2.waitKey(500)

# ------------------------------------------------------------
# STEP 2 — EXPONENTIAL BACKGROUND
# ------------------------------------------------------------
k = 0.95       # update rate (change to see differences)
bt = images[0].copy()   # initial background = first frame

for It in images[1:]:

    # Update background
    bt = k * bt + (1 - k) * It

    # ------------------ DIFFERENCES ------------------
    diff_avg = cv2.absdiff(It, background_avg)
    diff_exp = cv2.absdiff(It, bt)

    # ------------------ THRESHOLD ------------------
    _, mask_avg = cv2.threshold(diff_avg.astype(np.uint8), 25, 255, cv2.THRESH_BINARY)
    _, mask_exp = cv2.threshold(diff_exp.astype(np.uint8), 25, 255, cv2.THRESH_BINARY)

    # ------------------ MEDIAN FILTER ------------------
    mask_avg_f = cv2.medianBlur(mask_avg, 5)
    mask_exp_f = cv2.medianBlur(mask_exp, 5)

    # ------------------ DISPLAY ------------------
    cv2.imshow("Current Frame", It.astype(np.uint8))
    cv2.imshow("Background (Average)", background_avg.astype(np.uint8))
    cv2.imshow("Background (Exponential)", bt.astype(np.uint8))

    cv2.imshow("Difference (Average)", diff_avg.astype(np.uint8))
    cv2.imshow("Difference (Exponential)", diff_exp.astype(np.uint8))

    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
