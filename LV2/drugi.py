import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt(open("/home/r00t/Radna površina/Python/LV2/mtcars.csv", "rb"), usecols=(1,2,3,4,5,6),delimiter=",",skiprows=1)
mpg = data[:,0]
hp = data[:, 3]
wt = data[:, 5]
cyl = data[data[:, 1]==6]
br_auta = 0
plt.scatter(hp, mpg, s = wt * 10)

print(np.max(mpg))
print(np.min(mpg))
print(np.mean(mpg))

mpg_6cyl_min = np.min(cyl[:, 0])
mpg_6cyl_max = np.max(cyl[:, 0])
mpg_6cyl_mean = np.mean(cyl[:, 0])

print(np.max(mpg_6cyl_max))
print(np.min(mpg_6cyl_min))
print(np.mean(mpg_6cyl_mean))
print("\n")
plt.show()
