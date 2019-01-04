#!/bin/bash
input='./mismatched-word-list-73.txt';
while IFS= read -r var
do
  echo "${var%%.*}"
done < "$input"

