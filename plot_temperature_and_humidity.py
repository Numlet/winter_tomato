import matplotlib.pyplot as plt
import numpy as np
import datetime
months_str_upper_case=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
saving_file='temperature_log_%s.csv'%months_str_upper_case[datetime.date.today().month-1]



data=np.genfromtxt(saving_file,delimiter=',')
if len(data[:,0])>13000:
    data=np.copy(data[-13000:,:])
date_number=data[:,0]
date_str=data[:,1]
temperature=data[:,2]
humidity=data[:,3]
socket_on=data[:,4]
plt.figure()
f, (ax1, ax2,ax3) = plt.subplots(3, sharex=True)
ax1.plot(date_str,temperature)
ax1.set_title('Temperature (top) and Humidity')
ax2.plot(date_str,humidity)
ax3.plot(date_str,socket_on)
# Fine-tune figure; make subplots close to each other and hide x ticks for
# all but bottom plot.
f.subplots_adjust(hspace=0)
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.savefig('last_week.png')
