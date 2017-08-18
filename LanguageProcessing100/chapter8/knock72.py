import re

def trim_ignore_marks(word):
    ignore_marks = re.compile(r"[^a-zA-Z!?]")
    return re.sub(ignore_marks, "", word)
