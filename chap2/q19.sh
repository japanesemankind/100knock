#!/bin/sh
cat popular-names.txt | cut -f 1  | sort | uniq -c | sort -n -r
