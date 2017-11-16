#!/bin/bash

read n
read s
arr=($s)
printf '%s\n' "${arr[@]}" | sort | uniq -c | awk '{if($1==1) print $2}'
