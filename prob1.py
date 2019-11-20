#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 17:51:36 2019

@author: asukawatanabe
"""

import numpy as np
X = np.arange(1,101).reshape(10,10)
Y = X**2
Z = Y[Y%3==0]
print(Y)
print(Z)