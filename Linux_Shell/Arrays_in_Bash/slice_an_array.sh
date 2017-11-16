#!/bin/bash

ARRAY=()
while IFS= read -r LINE || [[ -n "$LINE" ]]; do
    ARRAY+=("$LINE")
done

# index 3부터 5개
echo ${ARRAY[@]:3:5}

####################################################
#  Input 
#    0  Namibia
#    1  Nauru
#    2  Nepal
#  * 3  Netherlands
#  * 4  NewZealand
#  * 5  Nicaragua
#  * 6  Niger
#  * 7  Nigeria
#    8  NorthKorea
#    9  Norway
#  
#  
#  Result
#  - Netherlands NewZealand Nicaragua Niger Nigeria
####################################################
