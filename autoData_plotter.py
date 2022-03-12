import numpy as np
import matplotlib.pyplot as plt

disp = np.loadtxt("autoData.csv", delimiter=",", usecols=(3))
hp = np.loadtxt("autoData.csv", delimiter=",", usecols=(4))
year = np.loadtxt("autoData.csv", delimiter=",", usecols=(1))
old = year[:149]
new = year[149:]

fig1 = plt.figure(num=1, clear=True)
ax1 = fig1.add_subplot(1, 1, 1)

ax1.scatter(disp[0:149], hp[0:149], c="red")
ax1.scatter(disp[149:], hp[149:], c="blue")
plt.show()

# for i, v in enumerate(year):
#    if v == 74.0:
#        print(i)
