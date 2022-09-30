#!/bin/bash


> oldFiles.txt

files=$(grep "jane " ../data/list.txt  | cut -d ' ' -f 3)

echo $files
echo $?

for file in $(echo $files); do
    echo $file
    if test -e ~/$file; then
        echo $file
        echo ~/$file >> oldFiles.txt
    fi
done
