import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("/home/r00t/Radna površina/Python/LV2/tiger.png")
avg = np.mean(img)
brightness_factor = 2
adjusted_img = img * (brightness_factor / avg)
rotated_img = np.rot90(adjusted_img, k = 3)
flipped_img = np.fliplr(rotated_img)
resized_img = np.zoom(adjusted_img, 0.1)


cropped_img = resized_img[:, resized_img.shape[1]//2:resized_img.shape[1]]
new_img = np.zeros((resized_img.shape[0], cropped_img.shape[1], resized_img.shape[2]), dtype=resized_img.dtype)
new_img[:, :cropped_img.shape[1], :] = cropped_img

plt.imshow(flipped_img)
plt.show()