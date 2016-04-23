#!/bin/bash

timestamp=`date +%F_%H-%M-%S`
echo "Temperature Log - $(date)" >/home/pi/temperature_log.txt
while :
do
    /opt/vc/bin/vcgencmd measure_temp >> /home/pi/logs/temperature_log.txt
    sleep 2
done
