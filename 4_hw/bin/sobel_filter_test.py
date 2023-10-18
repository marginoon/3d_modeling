import numpy as np
from scipy.ndimage.filters import generic_filter
from scipy.ndimage import imread

# Load sample data
with np.DataSource().open("https://i.stack.imgur.com/8zINU.gif", "rb") as f:
    img = imread(f, mode="I")

# Apply the Sobel operator
def sobel_filter(P):
    return (np.abs((P[0] + 2 * P[1] + P[2]) - (P[6] + 2 * P[7] + P[8])) +
            np.abs((P[2] + 2 * P[6] + P[7]) - (P[0] + 2 * P[3] + P[6])))
G = generic_filter(img, sobel_filter, (3, 3))