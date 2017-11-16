#!/bin/bash

read s
for i in `seq 1 1 $s`; do
    read num 
    total=$((total+num))
done
printf "%.3f\n" $(echo "$total/$s" | bc -l)
