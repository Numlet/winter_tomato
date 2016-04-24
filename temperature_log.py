import datetime
import numpy as np

import time
import sys
import Adafruit_DHT
import tomato_lib as tl
import os
pin_number=21

saving_file='temperature_log_%s.csv'%tl.months_str_upper_case[datetime.date.today().month-1]


socket_on=0
humidity=999
iplot=0
while True:
    humidity, temperature=Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,pin_number)
    if humidity>100:
        humidity=np.nan
        temperature=np.nan
    line='\n'+str(time.time())+','+tl.get_date_str()+','+str(temperature)+','+str(humidity)+','+str(socket_on)
    with open(saving_file,'a') as my_file:my_file.write(line)
    time.sleep(5)
    iplot=iplot+1
    if iplot>6:
        iplot=0
        os.system('python plot_temperature_and_humidity.py')
