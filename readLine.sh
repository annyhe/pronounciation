#!/bin/bash

# run with source ./readLine.sh
input='./mismatched-word-list-73.txt';
while IFS= read -r var
do
  WORD="${var%%.*}"
  echo $WORD
  # works for dictionary.com
  python python_script.py $WORD
  # works for cambridge
  # python cam.py $WORD

done < "$input"

