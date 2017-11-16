#!/bin/bash

ARRAY=()
while IFS= read -r LINE || [[ -n "$LINE" ]]; do
    ARRAY+=("$LINE")
done

NEW_ARR=( $(for i in ${ARRAY[@]}; do echo $i; done | sed 's/^./\./g') )
echo ${NEW_ARR[@]}
