filename_src = 'data/train.lengthratio.km' # Source Language Corpora
filename_tgt = 'data/train.lengthratio.en' # Target Lanuage Corpora

# Read Source Language
file_src = open(filename_src, 'r')
lines_src = file_src.readlines()
file_src.close()

# Read Target Language
file_tgt = open(filename_tgt, 'r')
lines_tgt = file_tgt.readlines()
file_tgt.close()

length = len(lines_src)
# Creating new file with normalised version 
src_newfile = filename_src[:-2] + 'norm.' + filename_src[-2:]
tgt_newfile = filename_tgt[:-2] + 'norm.' + filename_tgt[-2:]
skip = 0

# Returning src and tgt language sentences 
f_src_out = open(src_newfile, "w")
f_tgt_out = open(tgt_newfile, "w")
for i in range(length):
    src = lines_src[i]
    tgt = lines_tgt[i]
 
    # Finding length ofsetntences , If length is > 512, skipping the line.
    if (len(src) > 512 or len(tgt) > 512):
        skip += 1        
        print('iter {}: skipped {}'.format(i+1, skip))
    # Appending the total number of sententences with max length 512
    else:
        f_src_out.write(src)
        f_tgt_out.write(tgt)  
f_src_out.close()
f_tgt_out.close()

print('Remained: {} / skipped: {}'.format(length-skip, skip))
print('Filenames - {}, {}'.format(src_newfile, tgt_newfile))