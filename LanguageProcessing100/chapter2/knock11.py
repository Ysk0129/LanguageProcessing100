
if __name__ == "__main__":

    txt = ""
    with open("hightemp.txt") as file:
        txt = file.read()
    
    answer = txt.replace("\t", " ")

    print(answer)
