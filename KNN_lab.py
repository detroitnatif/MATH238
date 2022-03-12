#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 14:50:03 2022

@author: tylerklimas
"""
import numpy as np
import matplotlib.pyplot as plt

x0_x = []
x0_y = []
x1_x = []
x1_y = []
for i in range(100):
    x0_x.append(0)
    x0_y.append(np.random.uniform(0, 1))
    x1_x.append(5)
    x1_y.append(np.random.uniform(0, 1))


fig1 = plt.figure(num=1, clear=True)
ax1 = fig1.add_subplot(1, 1, 1)
# scatter the original points
ax1.scatter(x0_x, x0_y, c="blue")
ax1.scatter(x1_x, x1_y, c="orange")

fig2 = plt.figure(num=2, clear=True)
ax2 = fig2.add_subplot(1, 1, 1)

ax2.scatter(x0_x[0:20], x0_y[0:20], c="black", marker="v", s=20)
ax2.scatter(x1_x[0:20], x1_y[0:20], c="black", marker="v", s=20)
ax2.scatter(x0_x[21:100], x0_y[21:100], c="red", marker="*", s=20)
ax2.scatter(x1_x[21:100], x1_y[21:100], c="red", marker="*", s=20)

fig3 = plt.figure(num=3, clear=True)
ax3 = fig3.add_subplot(1, 1, 1)

ax3.scatter(x0_x[0:20], x0_y[0:20], c="black")
ax3.scatter(x1_x[0:20], x1_y[0:20], c="black")


y_0 = []
x_0 = []

for i in range(200):
    x_0.append(np.random.uniform(-1, 1))
    y_0.append(np.random.uniform(-1, 1))


fig4 = plt.figure(num=4, clear=True)
ax4 = fig4.add_subplot(1, 1, 1)
ax4.scatter(x_0[0:50], y_0[0:50], c="blue")
ax4.scatter(x_0[50:100], y_0[50:100], c="orange")

fig5 = plt.figure(num=4, clear=True)
ax5 = fig5.add_subplot(1, 1, 1)
ax5.scatter(x_0[0:20], y_0[0:20], c="red", marker="v", s=20)
ax5.scatter(x_0[21:100], y_0[21:100], c="black", marker="*", s=20)

plt.show()
