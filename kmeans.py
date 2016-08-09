#!/usr/bin/python3

import random
import math
import matplotlib
import matplotlib.pyplot as plt

matplotlib.style.use('ggplot')

x_bound = 10
y_bound = 10
num_points = 20
num_clusters = 4

# initalize data points and cluster centroids at random

#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.set_xlabel('X')
#ax.set_ylabel('Y')
#ax.set_title('K-means clustering')
plt.axis([-10, 10, -10, 10])
#plt.plot([p.x], [p.y], 'ro')

plt.show()
