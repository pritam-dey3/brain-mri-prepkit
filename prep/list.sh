#!/bin/bash
while IFS= read -r line
do
  mv "$line" $2
done < "$1"