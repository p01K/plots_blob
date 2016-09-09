#!/usr/bin/python2

import numpy
import matplotlib.pyplot as plt
from pylab import savefig
import sys

infile = open(sys.argv[1], 'r')
outfile = sys.argv[2]

# fig, ax = plt.subplots()

ind = []
a1 = []
a2 = []
a3 = []

delimeter = '\t'
xlabel = 'Number of workers'
ylabel = 'Runtime (seconds)'
legend_labels = ['HierarchicalKMeans', 'HierarchicalKMeansPar', 'BisectingMLlib']
for line in infile:
    # print line
    ind.append(int(line.split(delimeter)[0]))
    a1.append(float(line.split(delimeter)[1]))
    a2.append(float(line.split(delimeter)[2]))
    a3.append(float(line.split(delimeter)[3]))

indexes = numpy.arange(len(ind))

# ax.set_ylabel('Runtime (milliseconds)')
# ax.set_title('Number of tasks')
# print ind
plt.xlabel(xlabel)
plt.ylabel(ylabel
plt.xticks(indexes, ind)

plot1 = plt.plot(indexes, a1, marker='o', color='r')
plot2 = plt.plot(indexes, a2, marker='o', color='b')
plot2 = plt.plot(indexes, a3, marker='o', color='g')
# plt.legend(['HierRDD', 'Bisecting'],loc=2)

plt.legend(legend_labels, loc=1)

savefig(outfile)
