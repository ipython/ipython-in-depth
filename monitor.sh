#!/bin/bash

# run `bash monitor.sh namespace` to see your kubernetes note, pods and public IP`
# likely run it in a separate terminal to see howyour hub deployment in google cloud is going.

watch -n1 'echo "get nodes: $ kubectl get nodes"; kubectl get node; echo "\nget pods: kubectl --namespace='$1' get pod"; kubectl --namespace='$1' get pod; echo "\nGet public ip: kubectl --namespace='$1' get svc proxy-public "; kubectl --namespace='$1' get svc proxy-public'
