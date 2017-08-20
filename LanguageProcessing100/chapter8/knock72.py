import re
from stopword import StopWord
from stemming.porter2 import stem

def trim_ignore_marks(word):
    ignore_marks = re.compile(r"[^a-zA-Z!?']")
    return re.sub(ignore_marks, "", word)

def preprocess_stems(stems):
    sw = StopWord()
    return [trim_ignore_marks(stm) for stm in stems if not sw.is_included_stem(stm)]
