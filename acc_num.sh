#!/bin/bash
echo "Start execution code"
echo "Remove account_number.txt"
rm account_number.txt
echo "Creating account numbers file"
python3.6 num_string.py >> account_number.txt
cat account_number.txt
echo "Ending code..."
