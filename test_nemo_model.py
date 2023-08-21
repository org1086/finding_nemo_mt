from nemo.collections.nlp.models import MTEncDecModel
import random
import numpy as np
import csv

# To get the list of pre-trained models
MTEncDecModel.list_available_models()

# Download and load the a pre-trained to translate from English to Spanish
# model = MTEncDecModel.from_pretrained("nmt_zh_en_transformer6x6")
model = MTEncDecModel.restore_from("saved_models/nemo_km_en_3_datasets_bpe8000/AAYNBase.nemo")

test_src_file = "preprocessed_data/train.merged_data.km"
test_tgt_file = "preprocessed_data/train.merged_data.en"

with open(test_src_file, "r", encoding="utf-8") as src_file:
    src_sentences = src_file.readlines()
with open(test_tgt_file, "r", encoding="utf-8") as tgt_file:
    tgt_sentences = tgt_file.readlines()

assert len(src_sentences) == len(tgt_sentences)

all_indices = set(range(len(src_sentences)))
picked_indices = set(random.choices(list(all_indices), k=50))

np_src_samples = np.array(src_sentences)
np_tgt_samples = np.array(tgt_sentences)

picked_src_samples = [sent.strip('\n') for sent in list(np_src_samples[list(picked_indices)])]
picked_tgt_samples = [sent.strip('\n') for sent in list(np_tgt_samples[list(picked_indices)])]
# Translate a sentence or list of sentences
translations = model.translate(picked_src_samples, source_lang="km", target_lang="en")

print (f"source sentences: {picked_src_samples}")
print (f"translated sentences: {translations}")
print (f"target sentences: {picked_tgt_samples}")

rows = zip(picked_src_samples, translations, picked_tgt_samples)

with open("testing_results.csv", "w") as f:
    writer = csv.writer(f)
    # write header
    writer.writerow(["source_sentence", "translated_sentence", "target_sentence"])
    for row in rows:
        writer.writerow(row)