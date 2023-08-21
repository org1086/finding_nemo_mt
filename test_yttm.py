import random

import youtokentome as yttm

train_data_path = "preprocessed_data/alt/train.lengthratio.norm.en"
test_data_path = "preprocessed_data/alt/test.lengthratio.norm.en"
model_path = "example.model"

# Generating random text
with open(test_data_path, "r") as f:
    lines = f.readlines()
test_text = ' '.join(lines)

# Training model
yttm.BPE.train(data=train_data_path, vocab_size=32000, model=model_path)

# Loading model
bpe = yttm.BPE(model=model_path)

# Two types of tokenization
# print(bpe.encode([test_text], output_type=yttm.OutputType.ID))
# print(bpe.encode([test_text], output_type=yttm.OutputType.SUBWORD))

print (bpe.vocab())