for N in `seq 1 25`
do
	fairseq-generate q95_bpe \
		--path q95_bpe_save/checkpoint10.pt \
		--beam $N \
		| grep ^H | sed -e 's/H-//' \
		| sort  -n -k 1 | cut -f 3 \
		>q95_bpe_out/q95_bpe.out.$N.txt
	spm_decode \
		--model=tgt.subword.model \
		--input_format=piece \
		q95_bpe_out/q95_bpe.out.$N.txt >q95_bpe_out/q95_bpe.out.$N.decoded.txt
			
	fairseq-score \
		--sys q95_bpe_out/q95_bpe.out.$N.decoded.txt \
		--ref kftt-data-1.0/data/tok/kyoto-test.en \
		>>q95_bpe_out/bleu_log.txt
done
