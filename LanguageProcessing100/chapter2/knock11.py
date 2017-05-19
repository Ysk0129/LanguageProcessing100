
if __name__ == "__main__":

    file = open("hightemp.txt")
    file.close()

    txt = ""
    with open("hightemp.txt") as file:
        txt = file.read()
    
    answer = txt.replace("\t", " ")

    print(answer)
