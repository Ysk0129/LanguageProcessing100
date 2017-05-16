
def cipher(txt):
    return "".join(chr(219 - ord(c)) if c.islower() else c for c in txt)

if __name__ == "__main__":
    text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    
    # encryption
    print(cipher(text))

    # decryption
    print(cipher(cipher(text)))
