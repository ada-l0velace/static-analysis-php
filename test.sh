#!/bin/bash

FILES=samples/*.json
for f in $FILES
do
  echo "Processing $f file..."
  python main.py $f
done
