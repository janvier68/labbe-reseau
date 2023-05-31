import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime

# create data
customdate = datetime.datetime(2016, 1, 1, 13, 30)
y = [ 2,4,6,8,10,12,14,16,18,20 ]
x = []
for i in range(0,5):
 x.append("2023-%u-11;16:0:0"%(i))
for i in range(23,23+int(5)):
 x.append("200%u-6-11;16:0:0"%(i))

# plot
plt.plot(x,y)
plt.gcf().autofmt_xdate()
plt.show()