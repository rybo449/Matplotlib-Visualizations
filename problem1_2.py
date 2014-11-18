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
for i in reader:
	count = d.setdefault(i[3], 0)
	d[i[3]] = count + 1

XY = sorted(d.items(), key = lambda x:x[1], reverse = True)
X = [x for x,y in XY]
Y = [y for x,y in XY]
k = int(sys.argv[2])
X = X[:k]
Y = Y[:k]
X1 = [i for i in xrange(1,k+1)]

colors = ['b','g','r','c','m']
plt.bar(X1, Y, align = 'center', color = colors)
plt.xticks(X1, X, fontsize = 6)
plt.xlabel('Agencies')
plt.ylabel('Volume')
plt.title('Top-%d Agencies Jun/01/2013-Aug/31/2013'%(k), fontsize = 20)
plt.show()