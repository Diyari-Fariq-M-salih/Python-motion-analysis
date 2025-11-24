# 📝 Motion Detection Pipeline --- Layman-Friendly Summary

## 🧩 Overview

This project detects **motion between consecutive images** in a
sequence.\
Think of it like comparing pages in a flipbook to see what changed.

The pipeline uses simple image-processing techniques to highlight moving
objects like cars, people, or any change in the scene.

---

## 📸 1. Frame Sequence

The images (`0000.pgm`, `0001.pgm`, `0002.pgm`...) are read one by one.\
Each new image is compared with the previous one.

**Like:** flipping through a photo book and noticing changes.

---

## 🧽 2. Smoothing (Gaussian Blur)

Before detecting motion, we apply a soft blur.

**Why:**\
Real cameras have noise --- tiny random pixel changes that aren't real
movement.

**Effect:**\
Removes small flickers so the system focuses on meaningful changes.

---

## 🔍 3. Frame Differencing

This step subtracts the previous frame from the current one:

    difference = | current_frame – previous_frame |

**Why:**\
Anything that moved will look different between two frames.

**Like:**\
A "spot the differences" puzzle.

---

## 🎚 4. Thresholding

The difference image often contains small changes from noise or
lighting.

Thresholding isolates only the **big changes** (real motion):

    if difference > threshold → mark as motion
    else → background

**Result:**\
A black-and-white image showing where motion happened.

---

## 🟦 5. Binary Motion Mask

After thresholding:

- **white (255)** = motion\
- **black (0)** = no motion

This creates a clean, simple map of moving areas.

---

## 🚮 6. Median Filtering (cleaning the mask)

Thresholding alone is noisy.\
The median filter removes:

- isolated white pixels (noise)\
- small holes in detected motion

**Effect:**\
A cleaner, smoother motion map.

---

## 📈 7. Temporal Filters (Prewitt & Sobel)

These filters detect **how much a pixel changed over time**, producing
more detailed motion responses than simple differencing.

### 🔹 Temporal Prewitt

A basic time-derivative:\
It highlights quick changes between frames.

### 🔹 Temporal Sobel

A slightly stronger version that emphasizes edges and smooths noise.

**Both** show motion as bright areas.

---

## 🖥️ 8. Displaying All Results

The program shows multiple windows:

- the original frame\
- the difference image\
- Prewitt output\
- Sobel output\
- raw motion mask\
- cleaned motion mask

This helps compare how each method detects motion.

---

## 🔁 9. Updating Frames

After processing, the current frame becomes the new "previous frame":

    I0 = I1

This enables continuous analysis as the sequence plays.

---

## 🎉 **In one sentence:**

The system compares each image with the next, removes noise, detects
changes, cleans the results, and shows different visualizations of
motion.
