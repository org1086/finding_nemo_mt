from nemo.collections.nlp.models import MTEncDecModel

# load PTL checkpoint
model = MTEncDecModel.load_from_checkpoint("saved_models/nemo_km_en_3_datasets_bpe8000/AAYNBase--val_sacreBLEU=6.5572-epoch=217.ckpt")

# Translate a sentence or list of sentences
translations = model.translate(["អ៊ីតាលី បាន ឈ្នះ លើ ព័រទុយហ្គាល់ 31-5 ក្នុង ប៉ូល C នៃ ពិធី ប្រកួត ពាន រង្វាន់ ពិភព លោក នៃ កីឡា បាល់ ឱប ឆ្នាំ 2007 ដែល ប្រព្រឹត្ត នៅ ប៉ាស ឌេស ប្រីន ក្រុង ប៉ារីស បារាំង ។"], source_lang="km", target_lang="en")

print (translations)