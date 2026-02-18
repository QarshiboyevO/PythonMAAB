import numpy as np

def f_to_c(F):
    return (F - 32) * 5 / 9

temps_f = np.array([32, 68, 100, 212, 77])
vec_f_to_c = np.vectorize(f_to_c)

temps_c = vec_f_to_c(temps_f)
print("Task 1 (Celsius):", temps_c)

def power(a, b):
    return a ** b

nums = np.array([2, 3, 4, 5])
pows = np.array([1, 2, 3, 4])

vec_power = np.vectorize(power)
result = vec_power(nums, pows)

print("Task 2 (Power result):", result)

A = np.array([[4, 5, 6],
              [3, -1, 1],
              [2, 1, -2]])

b = np.array([7, 4, 5])

solution = np.linalg.solve(A, b)
print("Task 3 Solution (x, y, z):", solution)

A = np.array([[10, -2, 3],
              [-2, 8, -1],
              [3, -1, 6]])

b = np.array([12, -5, 15])

currents = np.linalg.solve(A, b)
print("Task 4 Currents (I1, I2, I3):", currents)

import numpy as np
from PIL import Image
img = Image.open("images/birds.jpg")
arr = np.array(img)

def flip_image(arr):
    h = np.fliplr(arr)      # left-right
    v = np.flipud(arr)     # up-down
    return h, v


def add_noise(arr, amount=30):
    noise = np.random.randint(-amount, amount, arr.shape)
    noisy = arr + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)


def brighten_channels(arr, value=40):
    bright = arr.copy()
    bright[..., 0] = np.clip(bright[..., 0] + value, 0, 255)  # red channel
    return bright


def apply_mask(arr, size=100):
    masked = arr.copy()
    h, w, _ = masked.shape
    cx, cy = h//2, w//2
    masked[cx-size//2:cx+size//2,
           cy-size//2:cy+size//2] = [0, 0, 0]
    return masked

# 1. Flip
h_flip, v_flip = flip_image(arr)

# 2. Noise
noisy = add_noise(arr)

# 3. Brighten red channel
bright = brighten_channels(arr)

# 4. Mask center
masked = apply_mask(arr)

Image.fromarray(h_flip).save("birds_flip_horizontal.jpg")
Image.fromarray(v_flip).save("birds_flip_vertical.jpg")
Image.fromarray(noisy).save("birds_noisy.jpg")
Image.fromarray(bright).save("birds_bright.jpg")
Image.fromarray(masked).save("birds_masked.jpg")