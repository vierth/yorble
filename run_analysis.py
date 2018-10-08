import prepare_corpus, index_corpus, detect_intertexuality, compile_and_filter_results, align_quotes, form_quote_system, build_chord_viz

####################
# ANALYSIS OPTIONS #
####################
# Set seedlength
seedlength = 4

# Matches must be above this percent similar. Use floats between 0 and 1
# .8 works well for prose Chinese documents
threshold = .8

# Set the minimum length of an acceptable match. The shorter the length
# the more noisy the results are.
matchlength = 10

# Set this to limit the similarity comparison to last n characters
# Set to None for no limit. Setting a limit significantly
# speeds the calculations up.
max_comp = 100



###############
# CORPUS PREP #
###############
# Name of save file. Leave as "corpus.pickle" for best compatibility with other scripts
picklefile = "corpus.pickle"

# Items to remove from texts
toremove = ['』','。', '！', '，', '：', '、', '（', '）', '；', '？', '〉', '〈', '」', '「', '『', '“', '”', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '_', '`''{', '|', '}', '~', '¤', '±', '·', '×', 'à', 'á', 'è', 'é', 'ê', 'ì', 'í', 'ò', 'ó', '÷', 'ù', 'ú', 'ü', 'ā', 'ī', 'ń', 'ň', 'ō', 'ū', 'ǎ', 'ǐ', 'ǔ', 'ǖ', 'ǘ', 'ǚ', 'ǜ', 'ǹ', 'ɑ', 'ɡ', 'α', 'β', 'γ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω', 'а', 'б', 'в', 'г', 'д', 'е', 'к', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'ё', '—', '‖', '‘', '’', '…', '※', 'ⅰ', 'ⅲ', '∈', '∏', '∑', '√', '∠', '∥', '∧', '∩', '∪', '∫', '∮', '∶', '∷', '∽', '≈', '≌', '≡', '⊙', '⊥', '⌒', '①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑩', '⑴', '⑵', '⑶', '⑷', '⑸', '⑹', '⑺', '⑻', '⑼', '⑽', '⑾', '⑿', '⒀', '⒁', '⒂', '⒃', '⒄', '⒅', '⒆', '⒈', '⒉', '⒊', '⒋', '⒌', '⒍', '⒎', '⒏', '⒐', '⒑', '⒒', '⒓', '⒔', '⒕', '⒖', '⒗', '⒘', '⒙', '⒚', '⒛', '─', '┅', '┋', '┌', '┍', '┎', '┏', '┐', '┑', '┒', '┓', '└', '┕', '┘', '┙', '┚', '┛', '├', '┝', '┞', '┠', '┡', '┢', '┣', '┤', '┥', '┦', '┧', '┩', '┪', '┫', '┬', '┭', '┮', '┯', '┰', '┱', '┲', '┳', '■', '□', '▲', '△', '◆', '◇', '○', '◎', '●', '★','︶', '﹑', '﹔', '﹖', '＂', '＃', '％', '＆', '＊','．', '／', '０', '１', '２', '３', '４', '５', '６', '７', '８', '９', '＜', '＝', '＞', '＠', '［', '＼', '］', '＿', '｀', 'ａ', 'ｂ', 'ｃ', 'ｄ', 'ｅ', 'ｆ', 'ｇ', 'ｈ', 'ｉ', 'ｊ', 'ｋ', 'ｌ', 'ｍ', 'ｎ', 'ｏ', 'ｐ', 'ｑ', 'ｒ', 'ｓ', 'ｔ', 'ｕ', 'ｖ', 'ｗ', 'ｘ', 'ｙ', 'ｚ', '｛', '｝', '～', '￥','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','《', '》', '〔', '〕', '【', '】', 'A',  'B',  'C',  'D',  'E',  'F',  'G',  'H', 'I', 'J', 'K', 'L', "M", 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',  'Ｗ',  'Ｘ',  'Ｙ',  'Ｚ',  '＾',  '｜', '￠',  '￡', '~']

####################
# INDEXING OPTIONS #
####################
# Index the corpus? True to do so, False to skip
# Indexing the corpus significantly speeds the analysis up when working with
# large corpora, but will use significant system resources.
create_index = False

# Output corpus index filename (will only read if create_index is set to True)
indexfile = 'index.db'

#************************#
# INPUT AND OUTPUT FILES #
#************************#

# By default, the script will compare every document in the corpus
# against every other document.
# Optionally, you can provide a file with a list of titles to analyze
# Set to None if you do not wish to use this. This will also default
# to None if the listed file does not exist.
# This file should just contain one filename per line seperated with a
# carraige return.
textstoanalyze = None

# You can also limit the part of the corpus you want to compare against
# By default the provided texts to analyze will be compared against all docs
corpuscomposition = None

# Provide a file with a precalculated index. If such a file exists, this
# will be used for detecting matches. Otherwise, indices are calcuated on
# the fly.



# Provide a directory for the output files. The script will produce one file
# per input text (they are aggregated into one file by align_quotes.py)

# IMPORTANT!!!!! If DEBUG is set to True, this folder will be deleted if it exists!!!!!
result_directory = 'results'

#***************#
# OTHER OPTIONS #
#***************#

# While debug is True, the script does not track which files
# have been compared and also deletes results from old runs.foranalysis.txt"
# If this is False, then the script can be stopped and restarted
# without losing progress.
DEBUG=False

# This following setting is necessary because of the multiprocessing module
# The higher the maxtasks, the faster the processing is but the more memory
# use fluctuates. If index is around 2.5 GB, use 50 workers, 150 < 1 GB
# Set to None if you don't want to have processes expire, but watch out for
# large memory use spikes. The multiprocessing occurs at the document level,
# so if you have fewer documents, you can also use fewer tasks
maxchildtasks = 150

# You can sort so the longest texts will be processed first. This will speed
# up overall processing time at the cost of RAM usuage.
frontloading = False

#**********************#
# FILTERING PARAMETERS #
#**********************#

# Filter the common, short quotes?
filtercommon = True
# What length constitutes "short"?
shortquotelength = 20
# How many repetitions consitute common?
repmax = 400

# Should similar to the common ones be filtered?
# This will add significant slowdown depending on how many
# quotes are included
filtersimilar = True
# What is the similarity threshold?
similaritythreshold = .6
# Limit check? If this is true, similarity will only be checked
# for quotes that start with the same characters. This speeds the
# code up significantly
limitcheck = True
limextent = 2

#************************#
# Input and output files #
#************************#

# Input directory
result_directory = "results"
# Output
filteredresultfile = "corpus_results.txt"


#************#
# PARAMETERS #
#************#

# Set a minimum threshold for similarity. 100 means one 100-character quote
# or alternatively ten 10-character quotes (or something like that)
scorelimit = 100

#*******************#
# OUTPUT FILE EDGES #
#*******************#
# Output
edgefile = 'edgetable.csv'

#********************#
# DOCUMENTS TO ALIGN #
#********************#

# Align quotes occuring between the following documents. Provide at
# least two. If None, all quotes will be aligned. If your corpus contains
# signficant reuse, this may be slow.
alignment_docs = ["KR2a0018 梁書-唐-姚思廉_10","KR2a0024 南史-唐-李延壽_54","KR2a0018 梁書-唐-姚思廉_11"]


#**********************#
# ALIGNMENT PARAMETERS #
#**********************#

# Match, mismatch, and gap scores
matchscore = 1
misalignscore = -1
mismatchscore = -1

# Limit the length of text that will be aligned
# This significantly speeds up the algorithm when
# aligning very long quotes. This divides the quotes
# into blocks of chunklim length. It tries to divide
# the chunks in places where the alignment is exact
# So overlap looks at the 10 character before and after
# the proposed break. When it finds rangematch exact
# characters, it inserts a break in the middle.
chunklim = 200
overlap = 10
rangematch = 6


#***********************#
# Alignment Output File #
#***********************#
# Output
alignmentoutput = "corpus_alignment.txt"


corpus_text_lengths = "corpus_text_lengths.txt"
################
# RUN ANALYSIS #
################

prepare_corpus.run(picklefile, toremove)

if create_index:
    index_corpus.run(seedlength, picklefile, indexfile)

detect_intertexuality.run(seedlength, threshold, matchlength, max_comp, textstoanalyze, corpuscomposition, picklefile, indexfile, create_index, result_directory, maxchildtasks, frontloading, DEBUG=False)

compile_and_filter_results.run(filtercommon, shortquotelength, repmax, filtersimilar, similaritythreshold, limitcheck,limextent, result_directory, filteredresultfile)

form_quote_system.run(scorelimit, filteredresultfile, edgefile)

align_quotes.run(alignment_docs,matchscore, misalignscore, mismatchscore, chunklim, overlap,rangematch, filteredresultfile, alignmentoutput)

build_chord_viz.run(alignmentoutput, alignment_docs, corpus_text_lengths)