#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:25:20 2019

@author: iris
"""
import wave
import numpy as np
import matplotlib.pyplot as plt

file = 'river'
a = wave.open(file+'.wav')

nf = a.getnframes()
data = a.readframes(nf)

w = np.frombuffer(data, dtype = np.int16)
w = w * 1.0  / (max(abs(w)))

plt.plot(w,linestyle='-',c='g')
plt.savefig(file+'.png')

plt.show()

