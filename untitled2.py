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
x_vals = ring[:,0]
y_vals = ring[:,1]
distFromOrigin = []
for i in range(len(x_vals)):
    distFromOrigin.append(math.sqrt((x_vals[i] - 0)**2 + (y_vals[i] - 0)**2 ))


fig1 = plt.figure(num=1, clear=True)
ax1 = fig1.add_subplot(1,1,1)
ax1.scatter(x_vals, y_vals)


fig2 = plt.figure(num=1, clear=True)
ax2 = fig2.add_subplot(2,1,1)

kmeans = KM(2)
kmeans.fit(ring)
y_kmeans = kmeans.fit_predict(ring)

ax2.scatter(ring[:, 0], ring[:, 1], c=y_kmeans, s=20, cmap='plasma')
ax2.set(xlim=(-20, 20), ylim=(-20, 20))


fig3 = plt.figure(num=1, clear=True)
ax3 = fig3.add_subplot(3,1,1)

x = np.linspace(0, len(x_vals), 200)
ax3.scatter(x, distFromOrigin, s=10)


kmeans_origin = KM(2)
kmeans_origin.fit(distFromOrigin)
#y_means_origin.fit


