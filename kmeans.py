#!/usr/bin/python3

import random
import math

x_bound = 10
y_bound = 10
num_points = 20
num_clusters = 4

class Point:
    def __init__(self, x=random.uniform(-x_bound, x_bound),
                       y=random.uniform(-y_bound, y_bound)):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def distance_to(self, p):
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

# initalize data points and cluster centroids at random
points = []
clusters= []

for i in range(num_points):
    points.append(Point())

for i in range(num_clusters):
    clusters.append(Point())


