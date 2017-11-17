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
    rows_sinus=$(echo "scale=2; sqrt((s($x/10) * 100)^2)"| bc -l | cut -d'.' -f1 )
    noise=$(echo "$(shuf -i 00-20 -n 1)-10" | bc -l)
    rows=$(echo "$rows_sinus  - $noise" | bc -l)
    #get timestamp
    timestamp=$(date +"%Y/%m/%d:%H:%M:%S")
        #normal
    for i in `seq 1 $rows`;
        do
                echo "$timestamp a logfile row $i of $rows" >> $logfile
        done
        if [ -e "./.freakout" ]; then
            for i in `seq 1 15`;
                do
                        sleep 1s
                        for i in `seq 1 500`;
                                do
                                        echo "$timestamp a logfile row $i of 500" >> $logfile
                        done
                done
    fi

    if [ -e "./.killme" ]; then
                finished=true
    fi
        #
done

