#!/bin/bash

cat input | uniq -c | awk '{$1=$1;print}'
