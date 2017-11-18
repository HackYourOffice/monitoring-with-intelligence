#!/bin/bash
#Ab jetzt
date=$(date -u +%Y-%m-%d)

# make copy to have a dataset for the current day
sed "s/2017-11-01T/${date}T/" server-metrics-23.json > server-metrics-today.json

while true; do
  time=$(date -u +%H:%M)

  # get a dataset for the current minute
  grep -B1 "${date}T${time}" server-metrics-today.json | grep -v -- -- > server-metrics-now.json

  # put data into elasticsearch
  curl -s -u elastic:changeme -X POST -H "Content-Type: application/json" http://localhost:9200/server-metrics1/_bulk --data-binary "@server-metrics-now.json" -v > /dev/null

  # sleep for a minute
  sleep 60
done
