#!/bin/sh

read x
read y
read z

if [ $x -eq $y ] && [ $y -eq $z ]
then
    echo "EQUILATERAL"
elif [ $x -eq $y ] && [ $y -ne $z ] && [ $z -ne $x ] 
then
    echo "ISOSCELES"
elif [ $x -ne $y ] && [ $y -eq $z ] && [ $z -ne $x ] 
then
    echo "ISOSCELES"
elif [ $x -ne $y ] && [ $y -ne $z ] && [ $z -eq $x ] 
then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi
