#!/bin/bash

# Run every main.py file 
# 2021/day_1/main.py

# Ask the user the year
echo "Enter the year: "

# Read the year
read INPUT_YEAR

if [ $INPUT_YEAR -lt 2019 ] || [ $INPUT_YEAR -gt 2025 ]
then
    echo "Invalid input"
    exit
fi

FOLDER_PATH="$INPUT_YEAR"

for i in $(seq -f "%02g" 1 25)
do
    FOLDER_NAME="day_$i"
    DIR_PATH="$FOLDER_PATH/$FOLDER_NAME"
    if [ -d "$DIR_PATH" ]
    then
        echo "Running $DIR_PATH/main.py"
        python3 "$DIR_PATH/main.py"
    fi
done