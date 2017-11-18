#!/bin/bash

# Time window for anomalies
ts=$(( $(date +%s) - 300 ))

# Pull the anomaly count from elasticsearch
count=$(curl -s "http://elastic:changeme@localhost:9200/_xpack/ml/anomaly_detectors/server-metrics-small-bucket/results/records?start=${ts}000" | jq .count)

# Notify apps for state
if [ $count -gt 0 ]; then
  #curl -s http://10.0.20.153:5000/api/motor/on
  curl -s http://10.0.20.153:5555/display?face=bad
else
  #curl -s http://10.0.20.153:5000/api/motor/off
  curl -s http://10.0.20.153:5555/display?face=good
fi
