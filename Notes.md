# Choosing a threshold is not trivial because:

### 1. Illumination changes can look like motion

A low threshold → false positives everywhere.

### 2. Sensor noise produces small variations

Even when there is no motion, noise in PGM images can change pixel intensities by 2–10 gray levels.
A threshold too low → noisy background becomes “motion”.

### 3. Motion magnitude varies across objects

Slow-moving objects cause small differences

Fast-moving objects cause large differences
One threshold cannot perfectly handle both.

### 4. Edges dominate the difference

Motion only triggers strong differences on edges, so interior regions of objects may have weak signal → too high threshold causes “holes”.

### 5. Different regions of the image behave differently

Shadows, reflections, textures, flat regions all produce very different pixel differences.

# 🔥 Why median is not regular blur

Let’s test with a 3×3 window:

Gaussian blur example \
[255, 255, 255]\
[255, 0, 255]\
[255, 255, 255]

→ average ≈ 198 → becomes a gray pixel

## Gaussian blur outputs:

198 (gray)

It smears the edge.

Median blur example

Same window:

[255, 255, 255]\
[255, 0, 255]\
[255, 255, 255]\

Sorted neighborhood values:

0, 255, 255, 255, ... , 255

## Median = 255 → stays white.
