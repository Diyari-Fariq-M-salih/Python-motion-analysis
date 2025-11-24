import cv2
import numpy as np
import time
import os

# Path to your images folder
img_dir = "Road/"   # <-- change if needed

# Load first image
I0 = cv2.imread(os.path.join(img_dir, "0000.pgm"), cv2.IMREAD_GRAYSCALE)
I0 = I0.astype(np.float64)

for cpt in range(1, 200):

    # Build filename like MATLAB version
    filename = f"{cpt:04d}.pgm"     # creates 0001.pgm, 0002.pgm, ..., 0199.pgm
    path = os.path.join(img_dir, filename)

    # Load next image
    I1 = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if I1 is None:
        print("File missing:", path)
        continue

    I1 = I1.astype(np.float64)

    # Display image
    cv2.imshow("Frame", I1 / 255.0)   # normalized for display
    cv2.setWindowTitle("Frame", filename)

    # Update previous frame
    I0 = I1.copy()

    # Pause like MATLAB pause(0.2)
    if cv2.waitKey(200) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()