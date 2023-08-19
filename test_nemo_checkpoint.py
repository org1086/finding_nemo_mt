from nemo.collections.nlp.models import MTEncDecModel

# load PTL checkpoint
model = MTEncDecModel.load_from_checkpoint("saved_models/nemo-en-km/AAYNBase/2023-08-17_10-51-31/checkpoints/AAYNBase--val_sacreBLEU=2.4263-epoch=318.ckpt")

# Translate a sentence or list of sentences
translations = model.translate(["一年多前，有份刊物嘱我写稿，题目已经指定了出来：“如果你只有三个月的寿命，你将会去做些什么事？”我想了很久，一直没有去答这份考卷"], source_lang="km", target_lang="en")

print (translations)