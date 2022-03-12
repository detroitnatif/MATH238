#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 16:53:04 2022

@author: tylerklimas
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans as KM
import math

ring = np.loadtxt('RingData.csv', delimiter=',')

#loading the data in 
x_vals = ring[:,0]
y_vals = ring[:,1]
#new 1d array
distFromOrigin = []
#for each row in the data file, find the distance from (0,0)
for i in range(len(x_vals)):
    distFromOrigin.append(math.sqrt((x_vals[i] - 0)**2 + (y_vals[i] - 0)**2 ))


fig1 = plt.figure(num=1, clear=True)
ax1 = fig1.add_subplot(1,1,1)
#scatter the original points
ax1.scatter(x_vals, y_vals)


fig2 = plt.figure(num=2, clear=True)
ax2 = fig2.add_subplot(1,1,1)

kmeans = KM(2)
kmeans.fit(ring)
y_kmeans = kmeans.fit_predict(ring)

ax2.scatter(ring[:, 0], ring[:, 1], c=y_kmeans, s=20, cmap='plasma')
ax2.set(xlim=(-20, 20), ylim=(-20, 20))

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=.6)


fig3 = plt.figure(num=3, clear=True)
ax3 = fig3.add_subplot(1,1,1)
x = np.linspace(0, len(x_vals), 200)
'''

HOW TO RESHAPE DATA
np.column_stack(([1, 2, 3], [4, 5, 6]))
array([[1, 4],
       [2, 5],
       [3, 6]])



np.column_stack((portfolio, index))

portfolio = [portfolio_value1, portfolio_value2, ...]
index = [index_value1, index_value2, ...]


[[portfolio_value1, index_value1],
 [portfolio_value2, index_value2],
 [portfolio_value3, index_value3],
 ...]
'''


a = np.column_stack((x, distFromOrigin))
kmeans2 = KM(2)
kmeans2.fit(a)
y_kmeans = kmeans2.fit_predict(a)

ax3.scatter(x, distFromOrigin, c=y_kmeans, s=50, cmap='plasma')



centers2 = kmeans2.cluster_centers_
plt.scatter(centers2[:, 0], centers2[:, 1], c='red', marker = "^", s=300, alpha=.6)





