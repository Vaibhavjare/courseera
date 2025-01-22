#!/bin/bash

# Simple Interest Calculator

# Prompt user for input
echo "Enter the principal amount (P): "
read principal

echo "Enter the rate of interest (R): "
read rate

echo "Enter the time period in years (T): "
read time

# Calculate Simple Interest
interest=$(echo "$principal * $rate * $time / 100" | bc)

# Display the result
echo "The simple interest is: $interest"
