from nemo.collections.nlp.models import MTEncDecModel

# To get the list of pre-trained models
MTEncDecModel.list_available_models()

# Download and load the a pre-trained to translate from English to Spanish
# model = MTEncDecModel.from_pretrained("nmt_zh_en_transformer6x6")
model = MTEncDecModel.restore_from("saved_models/nemo-en-km/AAYNBase/2023-08-17_10-51-31/checkpoints/AAYNBase.nemo")

# Translate a sentence or list of sentences
translations = model.translate(["អ៊ីតាលី បាន ឈ្នះ លើ ព័រទុយហ្គាល់ 31-5 ក្នុង ប៉ូល C នៃ ពិធី ប្រកួត ពាន រង្វាន់ ពិភព លោក នៃ កីឡា បាល់ ឱប ឆ្នាំ 2007 ដែល ប្រព្រឹត្ត នៅ ប៉ាស ឌេស ប្រីន ក្រុង ប៉ារីស បារាំង ។"], source_lang="km", target_lang="en")

print (translations)