#!/usr/bin/env python
"""
Test plotting from inside IPython
"""

# Should be able to replace with matplotlib.pyplot.ion() in newer ipython
%matplotlib
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()  # an empty figure with no axes
fig.suptitle('No axes on this figure')  # Add a title so we know which it is
plt.close()

fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
plt.close()
