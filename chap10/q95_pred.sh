for data in `seq 1 40`
do
  onmt_translate \
	  -model toy-ende/run/model_step_35000.pt \
	  -src subword_source/test.sub.ja \
	  -output q95/pred_$data.txt \
	  -beam_size $data \
	  -gpu 1 \
	  -replace_unk \
	  -verbose
  echo $data
  sacrebleu --force subword_source/test.sub2.en < q95/pred_$data.txt>>q95_bleu_log.txt
done
