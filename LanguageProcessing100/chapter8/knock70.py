import random

if __name__ == "__main__":

    with open("rt-polaritydata/rt-polaritydata/rt-polarity.neg", encoding="cp1252") as neg_f:
        neg_lines = ["-1 " + line for line in neg_f.readlines()]
    
    with open("rt-polaritydata/rt-polaritydata/rt-polarity.pos", encoding="cp1252") as pos_f:
        pos_lines = ["+1 " + line for line in pos_f.readlines()]


    new_lines = neg_lines + pos_lines
    random.shuffle(new_lines)

    with open("sentiment.txt", "a", encoding="utf-8") as new_f:
        new_f.writelines(new_lines)
