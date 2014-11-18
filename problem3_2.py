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
complete_dict = {}
agency = ['NYPD','DOT','DOB','TLC','DPR']

for i in reader:
	if i[8] in complete_dict:
		if i[3] in agency:
			count = complete_dict[i[8]].setdefault(i[3], 0)
			complete_dict[i[8]][i[3]] = count + 1
			#count = d.setdefault(i[8], 0)
			#d[i[8]] = count + 1
			z.append(i[8])
	else:
		complete_dict[i[8]] = {}
print complete_dict
#print len(z1)
colors = ['r','g','b','k','m']
c = 0

z1 = set(zipcode.keys())
z2 = set(complete_dict.keys())
z1 = list(z1.intersection(z2))
X = []
Y = []
color = []
temp = []
for i in z1:
	if len(complete_dict[i])!= 0:
		X.append(zipcode[i])
		x = zipcode[i]
		max_value = max(complete_dict[i].iteritems(), key=operator.itemgetter(1))[1]
		y = max_value
		temp1 = max(complete_dict[i].iteritems(), key=operator.itemgetter(1))[0]
		print temp1, temp
		if temp1 not in temp: 
			temp.append(max(complete_dict[i].iteritems(), key=operator.itemgetter(1))[0])
			plt.scatter(x, y, c = colors[agency.index(temp1)-1], alpha = 0.5, label = temp1)
		else:
			plt.scatter(x, y,c = colors[agency.index(temp1)-1], alpha = 0.5) 			
		Y.append(max_value)
		color.append(colors[c%5])
		c += 1
#area = np.pi * (15 * np.random.rand(50))
#plt.scatter(X, Y, c = color, alpha = 0.5, label = agency)
plt.legend(loc = 2)
plt.ylabel('Total Complaints')
plt.xlabel('Total Population')
plt.title('Plot of Total Complaints vs Population for Each Zipcode')
plt.grid(True)
plt.show()