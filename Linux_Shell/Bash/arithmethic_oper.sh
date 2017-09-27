#!/bin/sh

read s
S=${s//[[:blank:]]/}
printf "%.3f\n" $(echo "$S" | bc -l)
