#!/usr/bin/python2.7
import numpy
import matplotlib.pyplot as plt
from pylab import savefig
import sys
import json

output = sys.argv[2]
colors = ['r','b','g']

with open(sys.argv[1]) as input_json:
    json_data = json.load(input_json)

ylabel = json_data.get("xlabel")
xlabel = json_data.get("ylabel")
title  = json_data.get("title")
values = []
legends = json_data["legends"].split(',')
leg_loc = json_data.get("loc")
indexes = map(int,json_data["indexes"].split(','))
ivalues = json_data.get("ivalues")

for x in legends:
    new_entry = map(float,json_data[x].split(','))
    values.append(new_entry)

# indexes = map(int,indexes_str)
for v in values:
    print v

print ylabel,xlabel,indexes

if xlabel != None:
    plt.xlabel(xlabel)

if ylabel != None:
    plt.ylabel(ylabel)

if ivalues == None:
    plt.xticks(indexes)
else:
    plt.xticks(indexes,ivalues.split(','))

for i in range(0,len(values)):
    plot1 = plt.plot(indexes, values[i], marker='o', color=colors[i])
# plt.legend(['HierRDD', 'Bisecting'],loc=2)

if leg_loc != None:
    plt.legend(legends, loc=int(leg_loc))

savefig(output)
