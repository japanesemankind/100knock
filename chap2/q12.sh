#!/bin/sh
cat popular-names.txt | cut -f 1 >col1.txt
cat popular-names.txt | cut -f 2 >col2.txt
