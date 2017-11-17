#!/bin/bash
count=$(curl -s http://elastic:changeme@localhost:9200/_xpack/ml/anomaly_detectors/server-metrics/results/records?start=1492830000000 | jq .count)
echo $count
if [ $count -gt 0 ]; then
  curl -s http://10.0.20.153:5000/api/motor/on
  curl -s http://10.0.20.153:5555/display?face=bad
else
  curl -s http://10.0.20.153:5000/api/motor/off
  curl -s http://10.0.20.153:5555/display?face=good
fi
