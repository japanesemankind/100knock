#spm_train --input=kftt-data-1.0/data/orig/kyoto-train.ja \
#	--model_prefix=src.subword \
#	--vocab_size=16000 \
#	--character_coverage=0.9995 \
#	--model_type=unigram
#spm_train --input=kftt-data-1.0/data/orig/kyoto-train.en \
#	--model_prefix=tgt.subword \
#	--vocab_size=16000 \
#	--character_coverage=1.0 \
#	--model_type=unigram

spm_encode --model=src.subword.model \
	--output_format=piece \
	<kftt-data-1.0/data/orig/kyoto-test.ja >q95_test_encoded.ja
spm_encode --model=tgt.subword.model \
	--output_format=piece \
	<kftt-data-1.0/data/orig/kyoto-test.en >q95_test_encoded.en
#fairseq-generate q95 \
#       	--path q95_save/checkpoint10.pt \
#       	--beam 5 \
#	>q95_out.txt
