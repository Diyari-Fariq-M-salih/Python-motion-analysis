import cv2
import numpy as np
import time
import os

# Path to images folder
img_dir = "Road/"   # <-- change if needed

# Load first image
I0 = cv2.imread(os.path.join(img_dir, "0000.pgm"), cv2.IMREAD_GRAYSCALE)

for cpt in range(1, 200):

    # Build filename like MATLAB version
    filename = f"{cpt:04d}.pgm"
    path = os.path.join(img_dir, filename)

    # Load next image
    I1 = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if I1 is None:
        print("File missing:", path)
        continue

    # ----------- SMOOTHING BEFORE DIFFERENCE -----------

    # Apply Gaussian smoothing to reduce noise impact, can also use bilateral filter or box filter
    I0_s = cv2.GaussianBlur(I0, (5, 5), 1.0)
    I1_s = cv2.GaussianBlur(I1, (5, 5), 1.0)

    diff = cv2.absdiff(I1_s, I0_s)

    
    # ---------- THRESHOLDING ----------
    # Threshold the difference image: 
    # (diff > T) creates a boolean mask (True where diff > T, else False) 
    # .astype(np.uint8) converts True→1 and False→0 
    # multiplying by 255 turns it into a proper binary
    T = 25
    motion_mask = (diff > T).astype(np.uint8) * 255

    # ---------- DISPLAY ----------
    # Median filtering to clean up the binary mask
    motion_mask_filtered = cv2.medianBlur(motion_mask, 5)

    # Display filtered result
    cv2.imshow("Motion Mask (Filtered)", motion_mask_filtered)

    if diff.max() > 0:
        cv2.imshow("Difference", diff / diff.max())
    else:
        cv2.imshow("Difference", diff)

    cv2.imshow("Motion Mask", motion_mask)
    cv2.imshow("Frame", I1)   # Display raw frame

    cv2.setWindowTitle("Frame", filename)

    # Update previous frame (keep uint8!)
    I0 = I1.copy()

    # Pause like MATLAB pause(0.2)
    if cv2.waitKey(200) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
