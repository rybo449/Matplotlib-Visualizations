import matplotlib.pyplot as pyplot
import sys
import csv
import operator
import matplotlib.pyplot as plt
f = open(sys.argv[1])
reader = csv.reader(f,delimiter = ',')
d = {}
count = 0
next(reader)
L = ['NYPD','DOT','DOB','TLC','DPR']
for i in reader:
	if i[3] in L:
		count = d.setdefault(i[3], 0)
		d[i[3]] = count + 1

X = d.keys()
Y = d.values()
X1 = [i for i in xrange(1,6)]
colors = ['b','g','r','c','m']
plt.bar(X1, Y, align = 'center', color = colors)
plt.xticks(X1, X, fontsize = 6)
plt.xlabel('Agency')
plt.ylabel('Volume')
plt.title('Agencies Jun/01/2013-Aug/31/2013')
plt.show()