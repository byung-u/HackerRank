#!/bin/bash
cat input | uniq -ic | awk '{$1=$1;print}'

