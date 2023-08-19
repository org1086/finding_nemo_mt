import glob
import numpy as np
import random

src_cleaned_files = glob.glob("preprocessed_data" + '/**/*.norm.km', recursive=True)
tgt_cleaned_files = glob.glob("preprocessed_data" + '/**/*.norm.en', recursive=True)

# sort file names both for src and tgt
src_cleaned_files = list(sorted(src_cleaned_files))
tgt_cleaned_files = list(sorted(tgt_cleaned_files))

assert len(src_cleaned_files) == len(tgt_cleaned_files)

f_src_merged_data = open("preprocessed_data/merged_data.km", "w", encoding='utf-8')
f_tgt_merged_data = open("preprocessed_data/merged_data.en", "w", encoding='utf-8')

src_sentences, tgt_sentences = [], []
for idx in range(len(src_cleaned_files)):
    src_filename = src_cleaned_files[idx]
    tgt_filename = tgt_cleaned_files[idx]
    
    src_count, tgt_count = 0,0
    with open(src_filename, 'r', encoding='utf-8') as f_src:
        for line in f_src:
            src_count += 1
            f_src_merged_data.write(line)
            src_sentences.append(line)
    with open(tgt_filename, 'r', encoding='utf-8') as f_tgt:
        for line in f_tgt:
            tgt_count += 1
            f_tgt_merged_data.write(line)
            tgt_sentences.append(line)

    print (f"{src_filename}: {src_count}. {tgt_filename}: {tgt_count}")
    
    assert src_count == tgt_count, f"{src_filename}, {tgt_filename}"


f_src_merged_data.close()
f_tgt_merged_data.close()

# split data into train, val and test
# {train. val, test} ratio: {0.9, 0.05, 0.05}
num_val_samples = round(0.05 * len(src_sentences))
num_test_samples = round(0.05 * len(src_sentences))
num_val_test_samples = num_val_samples + num_test_samples

all_indices = set(range(len(src_sentences)))
val_test_indices = set(random.choices(list(all_indices), k=num_val_test_samples))
train_indices = all_indices.difference(val_test_indices)
val_indices = set(random.choices(list(val_test_indices), k=num_val_samples))
test_indices = val_test_indices.difference(val_indices)

np_src_samples = np.array(src_sentences)
np_tgt_samples = np.array(tgt_sentences)

train_src_samples = list(np_src_samples[list(train_indices)])
val_src_samples = list(np_src_samples[list(val_indices)])
test_src_samples = list(np_src_samples[list(test_indices)])
train_tgt_samples = list(np_tgt_samples[list(train_indices)])
val_tgt_samples = list(np_tgt_samples[list(val_indices)])
test_tgt_samples = list(np_tgt_samples[list(test_indices)])

# write train, val, test samples to files
with open("preprocessed_data/train.merged_data.km", "w", encoding="utf-8") as f_src_train:
    f_src_train.writelines(train_src_samples)
with open("preprocessed_data/val.merged_data.km", "w", encoding="utf-8") as f_src_val:
    f_src_val.writelines(val_src_samples)
with open("preprocessed_data/test.merged_data.km", "w", encoding="utf-8") as f_src_test:
    f_src_test.writelines(test_src_samples)
    
with open("preprocessed_data/train.merged_data.en", "w", encoding="utf-8") as f_tgt_train:
    f_tgt_train.writelines(train_tgt_samples)
with open("preprocessed_data/val.merged_data.en", "w", encoding="utf-8") as f_tgt_val:
    f_tgt_val.writelines(val_tgt_samples)
with open("preprocessed_data/test.merged_data.en", "w", encoding="utf-8") as f_tgt_test:
    f_tgt_test.writelines(test_tgt_samples)