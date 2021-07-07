#!/bin/sh

read str
echo $str | mecab -O wakati>tmp.txt

onmt_translate\
       	-model test/run/model_step_10000.pt\
	-src tmp.txt \
	-output tmp_out.txt

cat tmp_out.txt
rm tmp.txt
rm tmp_out.txt
