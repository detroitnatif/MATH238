#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 09:15:19 2022

@author: tylerklimas
"""

import random
import math
import matplotlib.pyplot as plt
import numpy as np


def calc_pi(num_of_shots):
    #creating two arrays to append binary results to
    circle_hits = []
    square_hits = []
    a = num_of_shots
    #loop through differing number of trials
    for i in range(a):
        #create random values between -.5 and .5, and then findind their distance
        #from the origin
        xvals = random.uniform(-.5, .5)
        yvals = random.uniform(-.5, .5)

        d = math.sqrt(xvals ** 2 + yvals ** 2)
        
        if d <= .5:
            circle_hits.append(1)
            square_hits.append(0)
        elif d > .5:
            square_hits.append(1)
            circle_hits.append(0)

        pi = 4 * sum(circle_hits) / num_of_shots
    return pi


print(calc_pi(10))
print(calc_pi(1000))
print(calc_pi(10_000))

def plot_pi():
    pi_estimates = []
    for j in range(1, 1_001, 5):
        pi_estimates.append(calc_pi(j))
    #print(len(pi_estimates))
    fig = plt.figure(num=1, clear=True)
    ax = fig.add_subplot(1, 1, 1)
    x = np.linspace(0, 1_000, 200) 
    ax.plot(x, pi_estimates)
    ax.set(xlim=(0, 1_000), ylim=(2.5, 4.2))
    ax.set_xlabel("Number of Shots")
    ax.set_ylabel(r"Estimated Value of $\pi$")
    ax.set_title(r'$\pi$ plotted against number of trials')
    ax.hlines(y=np.pi, xmin=0, xmax=1_100, linewidth=2, color='r')
    fig.tight_layout()
    fig.savefig('pi_vs_montecarlo5')
    return sum(pi_estimates)/len(pi_estimates)
sums = []

def agg(num):
    for i in range(num):
        sums.append(plot_pi())
    aggregate = (sum(sums))/num
    print(aggregate)
    percent_error = ((np.pi - aggregate)/np.pi) * 100
    print(percent_error)    
        
agg(5)
        
        




