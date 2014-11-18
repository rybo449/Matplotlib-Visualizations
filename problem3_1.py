import matplotlib.pyplot as pyplot
import sys
import csv
import operator
import matplotlib.pyplot as plt
import numpy as np

f = open(sys.argv[2])
reader = csv.reader(f, delimiter = ',')
next(reader)
zipcode = {}
for i in reader:
	zipcode[i[0]] = int(i[1])

f.close()
f = open(sys.argv[1])
reader = csv.reader(f,delimiter = ',')
d = {}
count = 0
X = []
Y = []
next(reader)
z = []
for i in reader:
	count = d.setdefault(i[8], 0)
	d[i[8]] = count + 1
	z.append(i[8])

z1 = set(zipcode.keys())
z2 = set(d.keys())
z1 = list(z1.intersection(z2))
X = []
Y = []
for i in z1:
	X.append(zipcode[i])
	Y.append(d[i])
#area = np.pi * (15 * np.random.rand(50))
plt.scatter(X, Y,c = 'b', alpha = 0.5)
plt.legend(loc = 2)
plt.ylabel('Total Complaints')
plt.xlabel('Total Population')
plt.title('Plot of Total Complaints vs Population for Each Zipcode')
plt.grid(True)
plt.show()