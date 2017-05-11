
if __name__ == "__main__":
    sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    words = sentence.replace(".", "").replace(",", "").split()
    answer = [len(word) for word in words]

    print(answer)
