
if __name__ == "__main__":

    file = open("hightemp.txt")
    answer = len(file.readlines())
    file.close()

    print(answer)
