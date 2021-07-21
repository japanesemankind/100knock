#ファイルをバイナリ化して出力
#fairseq-preprocess -s ja -t en \
	#--trainpref q95_train_encoded \
	#--validpref q95_dev_encoded \
	#--testpref q95_test_encoded \
	#--bpe sentencepiece \
	#--destdir q95_bpe \
	#--workers 20
#訓練
fairseq-train q95_bpe \
	--save-dir q95_bpe_save\
	--fp16 \
	--max-epoch 10 \
	--bpe sentencepiece \
	--arch transformer \
	--share-decoder-input-output-embed \
	--optimizer adam \
	--clip-norm 1.0 \
	--lr 1e-3 \
	--lr-scheduler inverse_sqrt \
	--warmup-updates 2000 \
	--update-freq 1 \
	--dropout 0.2 \
	--weight-decay 0.0001 \
	--criterion label_smoothed_cross_entropy \
	--label-smoothing 0.1 \
	--batch-size 64 \
	--max-tokens 6400 >q95_bpe_save/q95_bpe.log
