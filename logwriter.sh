#!/bin/bash
#set -xv
finished=false

if [ "$1" == "" ];then
        logfile=$(date +"%Y_%m_%d_%H_%M_%S")_logfile
else
        logfile=$1
fi

while ! $finished; do
    sleep 1s
    x=$(date +"%S")
    rows=$(echo "scale=2; sqrt((s($x/10) * 100)^2)"| bc -l | cut -d'.' -f1 )
    #get timestamp
    timestamp=$(date +"%Y/%m/%d:%H:%M:%S")
    for i in `seq 1 $rows`;
        do
                echo "$timestamp a logfile row $i of $rows" >> $logfile
        done
    if [ -e "./.killme" ]; then
                finished=true
    fi
done

