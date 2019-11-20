#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 17:53:50 2019

@author: asukawatanabe
"""
import numpy as np
X = np.random.random((5,5))
xmn = np.mean(X)
xsd = np.std(X)

Z = (X-xmn)/xsd
print(Z)
