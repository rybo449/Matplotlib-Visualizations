import sys
import csv
import matplotlib.pyplot as plt
from datetime import *
from ggplot import *
import matplotlib.dates as dt

f = open(sys.argv[1])
reader = csv.reader(f,delimiter = ',')

NYPD = {}
d = {}
TLC = {}
DPR = {}
count = 0
next(reader)
for i in reader:
	count = d.setdefault(i[3], 0)
	d[i[3]] = count + 1

topk = sorted(d.items(), key = lambda x:x[1], reverse = True)
k = int(sys.argv[2])
topk = [x for x,y in topk]
topk = topk[:k] 
start_date = datetime.strptime('06/01/2013 00:00:00 AM', '%m/%d/%Y %H:%M:%S %p')
f.close()
f = open(sys.argv[1])
reader = csv.reader(f,delimiter = ',')
next(reader)
complete = {}
for i in topk:
	complete[i] = {}
for i in reader:
	if i[3] in topk:
		date = datetime.strptime(i[1],'%m/%d/%Y %H:%M:%S %p')
		delta = date - start_date
		if int(delta.days) > 90:
			continue
		count = complete[i[3]].setdefault(int(delta.days), 0)
		complete[i[3]][int(delta.days)] = count + 1
labels = complete.keys()
XY = complete.values()

fig,ax = plt.subplots()
L = []
for i in xrange(0,91):
	L.append(start_date + timedelta(days = i))
colors = ['b','g','r','c','m','y','k']
c = 0
for i in labels:
	c += 1
	L = []
	X = complete[i].keys()
	Y = complete[i].values()
	for j in xrange(0,len(X)):
		L.append(start_date + timedelta(days = j))

	plt.xticks(X, L, fontsize = 6)
	plt.plot(L, Y, colors[c%7], label = i)

plt.legend(loc = 2)
ax.xaxis.set_major_formatter(dt.DateFormatter("%b %d %Y"))
ax.xaxis.set_major_locator(dt.DayLocator((1,8,16,24)))

plt.xlabel('Date')
plt.ylabel('Number of Complaints')
plt.show()


