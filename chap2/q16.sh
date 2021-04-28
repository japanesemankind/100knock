#!/bin/sh
LINES=`cat popular-names.txt | wc -l`
split -l $(($LINES/$1)) popular-names.txt split.
