# en-km-8m
perl mosesdecoder/scripts/training/clean-corpus-n.perl data/en-km-8m/data km en data.lengthratio 1 250 -ratio 2

# km-parallel
perl mosesdecoder/scripts/training/clean-corpus-n.perl data/km-parallel/bible2x4.en-km.clean km en bible2x4.en-km.clean.lengthratio 1 250 -ratio 2

perl mosesdecoder/scripts/training/clean-corpus-n.perl data/km-parallel/GlobalVoices.en-km km en GlobalVoices.en-km.lengthratio 1 250 -ratio 2

perl mosesdecoder/scripts/training/clean-corpus-n.perl data/km-parallel/GNOME.en-km km en GNOME.en-km.lengthratio 1 250 -ratio 2

perl mosesdecoder/scripts/training/clean-corpus-n.perl data/km-parallel/jw300-wmt20.en-km km en jw300-wmt20.en-km.lengthratio 1 250 -ratio 2

perl mosesdecoder/scripts/training/clean-corpus-n.perl data/km-parallel/KDE4.en-km km en KDE4.en-km.lengthratio 1 250 -ratio 2

perl mosesdecoder/scripts/training/clean-corpus-n.perl data/km-parallel/Tatoeba.en-km km en Tatoeba.en-km.lengthratio 1 250 -ratio 2

perl mosesdecoder/scripts/training/clean-corpus-n.perl data/km-parallel/Ubuntu.en-km km en Ubuntu.en-km.lengthratio 1 250 -ratio 2