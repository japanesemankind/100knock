#前処理の実行
onmt_build_vocab -config toy_en_de.yaml -n_sample 440288
#モデルの訓練
onmt_train -config toy_en_de.yaml
#検証データでの翻訳
onmt_translate -model test/run/model_step_7000.pt -src test_input3.txt -output test_output3.txt -gpu 0 -verbose
