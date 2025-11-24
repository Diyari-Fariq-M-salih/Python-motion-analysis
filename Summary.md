# Motion Detection -- Exercise 1 & 2 Summary (Layman-Friendly)

## 🧩 Overview

This project analyzes motion in an image sequence by comparing frames,
filtering noise, and building background models. The work covers:

- **Exercise 1:** Frame-to-frame motion detection using temporal
  filters\
- **Exercise 2:** Background modeling using average and exponential
  updates

This markdown summarizes all concepts in simple terms.

---

# 🟥 Exercise 1 --- Frame Differencing & Temporal Filters

## 1. Loading Frames

The sequence `0000.pgm` → `0199.pgm` is read like pages of a flipbook.\
Each new frame is compared with the previous one.

---

## 2. Smoothing (Gaussian Blur)

A gentle blur reduces tiny pixel noise.

**Why:**\
Noise creates false motion; smoothing keeps detection stable.

---

## 3. Frame Differencing

Compute the change between consecutive frames:

    difference = | current_frame – previous_frame |

Any changed pixel = motion.

---

## 4. Thresholding

We convert the difference into a black/white mask:

- white = motion\
- black = background

---

## 5. Median Filter

The mask can be noisy, so we apply a median filter:

- removes isolated white dots\
- fills holes\
- keeps edges sharp

---

## 6. Temporal Prewitt & Sobel Filters

These detect "change over time" (not space):

### Prewitt

A simple temporal difference. Good for edge changes.

### Sobel

A stronger gradient; smoother and more sensitive.

Both highlight motion as bright areas.

---

# 🟦 Exercise 2 --- Background Modeling

## 1. Average Background

We average all 200 frames:

    background = mean(frames)

### Why moving objects disappear

Because:

- background stays in the **same place** in all frames\
- moving objects appear in **different places**\
- so the background "wins the vote"

Great for static scenes, poor when lighting changes.

---

## 2. Exponential Background Updating

A dynamic background that updates each frame:

    bt = k * bt_previous + (1 - k) * current_frame

Where **k** controls speed.

### Slow update (k = 0.95--0.99)

- background changes slowly\
- moving objects stay detected longer

### Fast update (k = 0.6--0.9)

- background adapts quickly\
- lighting changes handled well\
- moving objects may fade too fast

---

# ⭐ Comparison: Average vs Exponential Background

Feature Average BG Exponential BG

---

Needs all frames ✔ Yes ✖ No
Adapts over time ✖ No ✔ Yes
Good for real-time ✖ No ✔ Yes
Removes moving objects ✔ Strongly ✔ Moderately
Handles lighting changes ✖ Poorly ✔ Well
Car parked becomes BG ✖ No ✔ Yes

---

# 🎉 Summary (One Sentence)

Frame differencing detects motion by comparing consecutive images, while
background subtraction (average or exponential) builds a stable or
adaptive model of the scene to highlight moving objects.
