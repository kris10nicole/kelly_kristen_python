# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 23:56:38 2016

@author: 12072062
"""

import pandas as pd   #This is a module that python uses to recognize rows as observations and columns as variables
import os as os     #
import numpy as np
from pylab import *


bin_size = 0.1; min_edge = 0; max_edge = 2.5
N = (max_edge-min_edge)/bin_size; Nplus1 = N + 1
binwidth = np.linspace(min_edge, max_edge, Nplus1)

#The line below reades the diamonds data from the website
diamonds =pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/ggplot2/diamonds.csv ")

plt.hist(diamonds, bins=range(min(diamonds), max(diamonds)+binwidth,binwidth))
