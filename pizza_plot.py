#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 14:27:35 2022

@author: tylerklimas
"""
from sklearn.cluster import KMeans as KM
from sklearn.metrics.pairwise import pairwise_distances_argmin
from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt 
points = np.loadtxt('PizzaData.csv', delimiter=',')
x_vals = points[:,0]

y_vals = points[:,1]

fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1)






kmeans = KM(n_clusters=3)
kmeans.fit(points)
y_kmeans = kmeans.fit_predict(points)

plt.scatter(points[:, 0], points[:, 1], c=y_kmeans, s=50, cmap='plasma')

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=3000, alpha=.1)

