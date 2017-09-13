
if __name__ == "__main__":

    with open("hightemp.txt") as f:
        answer = len(f.readlines())

    print(answer)
