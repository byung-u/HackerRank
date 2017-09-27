#!/bin/sh

read a

if [ $a == 'N' ] || [ $a == 'n' ]
then
    echo "NO"
elif [ $a == 'Y' ] || [ $a == 'y' ]
then
    echo "YES"
fi
