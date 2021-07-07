onmt_translate \
       	-model test/run/model_step_10000.pt\
	-src kftt-data-1.0/data/tok/kyoto-test.ja\
	-output pred.txt \
	-gpu 0\
	-verbose
sacrebleu -force kftt-data-1.0/data/tok/kyoto-test.en < pred_10000.txt
