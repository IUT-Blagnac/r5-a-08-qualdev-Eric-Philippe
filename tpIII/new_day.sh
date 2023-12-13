#!/bin/bash

# Ask the user the year
echo "Enter the year between 2019 and 2023: "

# Read the year
read INPUT_YEAR

if [ $INPUT_YEAR -lt 2019 ] || [ $INPUT_YEAR -gt 2023 ]
then
    echo "Invalid input"
    exit
fi

echo "Enter the day: "

read DAY

FOLDER_NAME="day_$DAY"


DIR_PATH="$INPUT_YEAR/$FOLDER_NAME"

# If the directory doesn't exist, create it
if [ ! -d "$DIR_PATH" ]
then
    mkdir -p "$DIR_PATH"
fi

# Create a file main.py
cp template.py "$DIR_PATH/main.py"
touch "$DIR_PATH/input.txt"

# Show the user the command to launch the main.py
echo "python3 $DIR_PATH/main.py"

