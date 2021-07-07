for data in `seq 1 40`
do
  #onmt_translate \
	  #-model test/run/model_step_10000.pt \
	  #-src kftt-data-1.0/data/tok/kyoto-test.ja \
	  #-output q94/pred_$data.txt \
	  #-beam_size $data \
	  #-gpu 1 \
	  #-verbose
  echo $data
  sacrebleu --force kftt-data-1.0/data/tok/kyoto-test.en < q94/pred_$data.txt>>q94_bleu_log.txt
done
