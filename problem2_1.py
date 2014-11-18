import sys
import csv
import matplotlib.pyplot as plt
from datetime import *
from ggplot import *
import matplotlib.dates as dt

f = open(sys.argv[1])
reader = csv.reader(f,delimiter = ',')


NYPD = {}
TLC = {}
DPR = {}
count = 0
next(reader)
start_date = datetime.strptime('06/01/2013 00:00:00 AM', '%m/%d/%Y %H:%M:%S %p')
for i in reader:
	if i[3] == 'NYPD':
		date = datetime.strptime(i[1],'%m/%d/%Y %H:%M:%S %p')
		delta = date - start_date
		count = NYPD.setdefault(int(delta.days), 0)
		NYPD[int(delta.days)] = count + 1
	elif i[3] == 'TLC':
		date = datetime.strptime(i[1],'%m/%d/%Y %H:%M:%S %p')
		delta = date - start_date
		count = TLC.setdefault(int(delta.days), 0)
		TLC[int(delta.days)] = count + 1
	elif i[3] == 'DPR':
		date = datetime.strptime(i[1],'%m/%d/%Y %H:%M:%S %p')
		delta = date - start_date
		count = DPR.setdefault(int(delta.days), 0)
		DPR[int(delta.days)] = count + 1

X = DPR.keys()
Y = DPR.values()
X1 = []
L = []
fig, ax = plt.subplots()
#print len(X),len(Y)
for i in xrange(0, len(X)):
	L.append(start_date + timedelta(days = i))

plt.xticks(X, L, fontsize = 6)
plt.plot(L, Y, 'b', label = 'DPR')
X = NYPD.keys()
Y = NYPD.values()

plt.xticks(X, L, fontsize = 6)
plt.plot(L, Y, 'r', label = 'NYPD')
X = TLC.keys()
Y = TLC.values()



plt.xticks(X, L, fontsize = 6)
plt.plot(L, Y, 'g', label = 'TLC')
plt.legend(loc = 2)
ax.xaxis.set_major_formatter(dt.DateFormatter("%b %d %Y"))
ax.xaxis.set_major_locator(dt.DayLocator((1,8,16,24)))

plt.xlabel('Date')
plt.ylabel('Number of Complaints')
plt.show()

