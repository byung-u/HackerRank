#!/bin/bash

ARRAY=()
while IFS= read -r LINE || [[ -n "$LINE" ]]; do
    ARRAY+=("$LINE")
done
echo ${ARRAY[@]}
