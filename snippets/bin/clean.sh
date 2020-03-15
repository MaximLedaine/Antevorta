#!/bin/bash
echo cleaning notebooks

# enter every folder to clean files
cd jupyter

find $directory -type f -name "*.ipynb" | while read line; do
    echo "Processing file '$line'"
    nbstripout "$line"
done

echo done