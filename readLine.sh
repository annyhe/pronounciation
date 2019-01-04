#!/bin/bash

# run with source ./readLine.sh
input='./mismatched-word-list-73.txt';
while IFS= read -r var
do
  WORD="${var%%.*}"
  echo $WORD
  # echo "https://www.dictionary.com/browse/${WORD}"
  # this works for cambridge
  python python_script.py $WORD

done < "$input"

