import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt(open("/home/r00t/Radna površina/Python/LV2/mtcars.csv", "rb"), usecols=(1,2,3,4,5,6),delimiter=",",skiprows=1)
mpg = data[:,1]
hp = data[:, 4]
wt = data[:, 5]
cyl = data[:, 2]
br_auta = 0
plt.scatter(mpg, hp)
plt.plot(wt,marker =".",markersize=10, color = "red")
print(np.max(mpg))
print(np.min(mpg))
print(np.mean(mpg))
plt.show()