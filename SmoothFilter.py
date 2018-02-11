import scipy.signal as sig
import numpy as np

def get_gaussian_mask(sigma, mask_size):
    size_left = -mask_size // 2 + 1
    size_right = mask_size // 2 + 1

    x, y = np.mgrid[size_left:size_right, size_left:size_right]
    mask = np.exp(-((x ** 2 + y ** 2) / (2.0 * sigma ** 2))) / (2 * np.pi * sigma ** 2)
    return mask / mask.sum()

def filter_image(img, mask):
    img = np.asarray(img, dtype=float)
    img = sig.convolve2d(img, mask)
    return img