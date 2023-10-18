import numpy as np
from scipy.ndimage.filters import generic_filter
import cv2

# Load sample data


img_grayscale = cv2.imread('test.jpg',0)

def sobel_filter(P):
    return (np.abs((P[0] + 2 * P[1] + P[2]) - (P[6] + 2 * P[7] + P[8])) +
            np.abs((P[2] + 2 * P[6] + P[7]) - (P[0] + 2 * P[3] + P[6])))
G = generic_filter(img_grayscale, sobel_filter, (3, 3))