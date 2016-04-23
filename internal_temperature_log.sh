#!/bin/bash

timestamp=`date +%F_%H-%M-%S`
FILE=/home/pi/temperature_log.txt
echo "Temperature Log - $(date)" >$FILE
while :
do
    /opt/vc/bin/vcgencmd measure_temp >> $FILE
    date +%F_%H-%M-%S >> $FILE
    sleep 2
done
