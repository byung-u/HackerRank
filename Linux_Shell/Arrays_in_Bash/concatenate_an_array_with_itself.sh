#!/bin/bash

ARRAY=()
while IFS= read -r LINE || [[ -n "$LINE" ]]; do
    ARRAY+=("$LINE")
done

NEW_ARR+=("${ARRAY[@]}")
NEW_ARR+=("${ARRAY[@]}")
NEW_ARR+=("${ARRAY[@]}")
echo ${NEW_ARR[@]}

# More shorter
Total=("${ARRAY[@]}" "${ARRAY[@]}" "${ARRAY[@]}")
echo ${Total[@]}

