#!/usr/bin/python2.7
import numpy
import matplotlib.pyplot as plt
from pylab import savefig
import sys


infile = open(sys.argv[1], 'r')
outfile = sys.argv[2]
x = []
dst = []
default = []
for line in infile:
        # print line
        x.append(int(line.split('\t')[0]))
        dst.append(float(line.split('\t')[1]))
        default.append(float(line.split('\t')[2]))

# diff = numpy.array(default)-numpy.array(dst)

fig, ax = plt.subplots()
width = 0.2
bar_width = 0.35
# rects1 = ax.bar(ind-width, sp, width, color='b')
ind = numpy.arange(len(x))+1
rects1 = ax.bar(ind, dst, width, color='r')
rects2 = ax.bar(ind+width, default, width, color='b')

ax.set_ylabel('Runtime  (seconds)')
ax.set_title('Nof Elements')
ax.set_xticks(ind + width)
ax.set_xticklabels(x)
plt.legend(['nested', 'flat'], loc='upper left')

savefig(outfile)#.format(sys.argv[1].split('.')[0]))

infile.close()
