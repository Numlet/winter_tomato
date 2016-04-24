from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt
import numpy as np
import datetime
import tomato_lib as tl
saving_file='temperature_log_%s.csv'%tl.months_str_upper_case[datetime.date.today().month-1]

date_format=DateFormatter('%d %H:%M:%S')

data=np.genfromtxt(saving_file,delimiter=',')
if len(data[:,0])>13000:
    data=np.copy(data[-13000:,:])
date_number=data[:,0]
date_str=data[:,1]
temperature=data[:,2]
humidity=data[:,3]
socket_on=data[:,4]
time_list=[datetime.datetime.fromtimestamp(i) for i in date_number]
#print time_list
#print date_number
#print temperature
plt.figure()
f, (ax1, ax2,ax3) = plt.subplots(3, sharex=True)
ax1.plot(time_list,temperature,'r')
ax1.grid()
ax1.set_ylim(0,35)
ax1.xaxis.set_major_formatter(date_format)
ax1.set_title('Temperature (top), Humidity (mid) and socket on/off (bot)')
ax2.plot(time_list,humidity)
ax2.grid()
ax2.set_ylim(0,100)
ax3.plot(time_list,socket_on,'k--')
ax3.set_ylim(0,1)
# Fine-tune figure; make subplots close to each other and hide x ticks for
# all but bottom plot.
#f.subplots_adjust(hspace=0)
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.gcf().autofmt_xdate()
plt.savefig('/var/www/html/last_week.jpg')
