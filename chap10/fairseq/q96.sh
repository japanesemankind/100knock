fairseq-train q95_2 \
	--fp16 \
	--save-dir q96_save \
	--max-epoch 10 \
	--arch transformer \
	--share-decoder-input-output-embed \
	--optimizer adam \
	--clip-norm 1.0 \
	--lr 1e-3 \
	--lr-scheduler reduce_lr_on_plateau \
	--dropout 0.1 \
	--weight-decay 0.0001 \
	--criterion label_smoothed_cross_entropy \
	--label-smoothing 0.1 \
	--batch-size 64 \
	--max-tokens 8000 \
	--task translation \
	--eval-bleu  \
	--eval-bleu-args '{"beam":5}' \
	--tensorboard-logdir q96 \
	>q96/q96.log

