# Finding Nemo

# Work with Nemo container
```
docker run --name nemo -it -d -v /home/tdh/training_nemo_mt/:/workspace/nemo/finding_nemo/ --restart always --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 nvcr.io/nvidia/nemo:23.06
```
Flags recommended by Nvidia: `--gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864`

## Data pre-processing
Clone Repository
```
git clone https://github.com/moses-smt/mosesdecoder data/mosesdecoder
```
Moses Decoder is used for cleaning the corpus
- Training data:
```
perl mosesdecoder/scripts/training/clean-corpus-n.perl data/train.alt km en data/train.lengthratio 1 250 -ratio 2
```
- Validation data:
```
perl mosesdecoder/scripts/training/clean-corpus-n.perl data/dev.alt km en data/dev.lengthratio 1 250 -ratio 2
```
- Testing data:
```
perl mosesdecoder/scripts/training/clean-corpus-n.perl data/test.alt km en data/test.lengthratio 1 250 -ratio 2
```
Max character length normalisation for `train, dev, test` sets:
```
python3 max_len_filter.py -t train
```

```
python3 max_len_filter.py -t dev
```

```
python3 max_len_filter.py -t test
```

Prepare tarred dataset for training data
```
python create_tarred_parallel_dataset.py \
--src_fname data/train.lengthratio.norm.km \
--tgt_fname data/train.lengthratio.norm.en \
--out_dir tarred_dataset_km_en_tokens \
--clean \
--encoder_tokenizer_name yttm \
--encoder_tokenizer_vocab_size 32000 \
--encoder_tokenizer_coverage 0.999 \
--encoder_tokenizer_bpe_dropout 0.1 \
--decoder_tokenizer_name yttm \
--decoder_tokenizer_vocab_size 32000 \
--decoder_tokenizer_coverage 0.999 \
--decoder_tokenizer_bpe_dropout 0.1 \
--max_seq_length 512 \
--min_seq_length 1 \
--tokens_in_batch 20 \
--lines_per_dataset_fragment 10000 \
--num_batches_per_tarfile 2
```

Three merged dataset:
```
python create_tarred_parallel_dataset.py \
--src_fname preprocessed_data/train.merged_data.km \
--tgt_fname preprocessed_data/train.merged_data.en \
--out_dir tarred_datasets/tarred_3_merged_datasets_km_en_tokens_16384 \
--clean \
--encoder_tokenizer_name yttm \
--encoder_tokenizer_vocab_size 32000 \
--encoder_tokenizer_coverage 0.999 \
--encoder_tokenizer_bpe_dropout 0.1 \
--decoder_tokenizer_name yttm \
--decoder_tokenizer_vocab_size 32000 \
--decoder_tokenizer_coverage 0.999 \
--decoder_tokenizer_bpe_dropout 0.1 \
--max_seq_length 512 \
--min_seq_length 1 \
--tokens_in_batch 16384 \
--lines_per_dataset_fragment 50000 \
--num_batches_per_tarfile 5
```
## Training Nemo-based km-en model
```
python enc_dec_nmt.py \
--config-path=conf \
--config-name=aayn_base \
trainer.devices=1 \
~trainer.max_epochs \
+trainer.max_steps=100000 \
model.beam_size=4 \
model.max_generation_delta=5 \
model.label_smoothing=0.1 \
model.encoder_tokenizer.tokenizer_model=tarred_dataset_km_en_tokens/tokenizer.encoder.32000.BPE.model \
model.decoder_tokenizer.tokenizer_model=tarred_dataset_km_en_tokens/tokenizer.decoder.32000.BPE.model \
model.encoder.inner_size=2048 \
model.encoder.ffn_dropout=0.1 \
model.decoder.num_layers=6 \
model.decoder.hidden_size=512 \
model.decoder.inner_size=2048 \
model.decoder.num_attention_heads=8 \
model.decoder.ffn_dropout=0.1 \
model.train_ds.use_tarred_dataset=true \
model.preproc_out_dir=tarred_dataset_km_en_tokens \
model.train_ds.metadata_file=tarred_dataset_km_en_tokens/metadata.tokens.500.json \
model.train_ds.shard_strategy=scatter \
model.train_ds.tokens_in_batch=500 \
model.validation_ds.src_file_name=data/dev.lengthratio.norm.km \
model.validation_ds.tgt_file_name=data/dev.lengthratio.norm.en \
model.validation_ds.tokens_in_batch=500 \
model.test_ds.src_file_name=data/test.lengthratio.norm.km \
model.test_ds.tgt_file_name=data/test.lengthratio.norm.en \
model.optim.lr=0.001 \
+exp_manager.create_wandb_logger=True \
+exp_manager.wandb_logger_kwargs.name=exp-nemo_mt_km_en \
+exp_manager.wandb_logger_kwargs.project=nemo_mt_km_en \
+exp_manager.create_checkpoint_callback=True \
+exp_manager.checkpoint_callback_params.monitor=val_sacreBLEU \
+exp_manager.exp_dir=saved_models/nemo-en-km \
+exp_manager.checkpoint_callback_params.mode=max \
+exp_manager.checkpoint_callback_params.save_top_k=5 \
+exp_manager.checkpoint_callback_params.always_save_nemo=True
```
