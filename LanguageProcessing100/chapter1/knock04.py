
if __name__ == "__main__":
    print(dir(""))
    sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    words = sentence.split()
    one_letter_cases = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    answer = {}

    for i in range(len(words)):
        if i + 1 in one_letter_cases:
            answer[i] = words[i][:1]
        else:
            answer[i] = words[i][:2]

    print(answer)
