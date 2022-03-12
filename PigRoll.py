#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 12:48:06 2022

@author: tylerklimas

"""
import numpy as np
import random
def play_pig():
    score = 0
    plays = []
    r = True
    while r == True:
        play = input("Enter stop or roll: " )
        if play == "roll":
            b = random.randint(1, 6)
            plays.append(b)
            score += b
            print(score, plays)
            
            if b == 1:
                score = 0
                print(score)
                break
        if play == "stop":
            r = False
            print(score)
            break
        
        
    
    
play_pig()