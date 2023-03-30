import numpy as np
import matplotlib.pyplot as plt

def checkerboard():
    size = 50
    black = np.zeros((4,4),dtype=int)
    white = np.ones((4,4),dtype=int) * 255
    row1 = np.hstack([white, black] * int(4/2))
    row2 = np.hstack([black, white] * int(4/2))
    checkerboard = np.vstack([row1, row2] * int(4/2))
    return checkerboard

img = checkerboard()
plt.imshow(img, cmap = "gray", vmin=0, vmax=255)
plt.show()