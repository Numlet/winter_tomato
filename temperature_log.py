import datetime
import time
import sys
import Adafruit_DHT

months_str_upper_case=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

pin_number=21

saving_file='temperature_log_%s.csv'%months_str_upper_case[datetime.date.today().month-1]

def get_date_str():
    date_now=datetime.datetime.now()
    date_formatted=str(date_now.day)+'/'+str(date_now.month)+' '+str(date_now.hour)+':'+str(date_now.minute)+':'+str(date_now.second)
    return date_formatted

socket_on=0
humidity=999
while True:
    while humidity>100:
        humidity, temperature=Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,pin_number)

        
    line='\n'+str(time.time())+','+get_date_str()+','+str(temperature)+','+str(humidity)+','+str(socket_on)
    with open(saving_file,'a') as my_file:my_file.write(line)
    time.sleep(5)
