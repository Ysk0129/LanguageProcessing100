
if __name__ == "__main__":

    with open("hightemp.txt") as file:
        hightemp = file.readlines()

    col1 = []
    col2 = []
    for line in hightemp:
        cols = line.split("\t")
        col1.append(cols[0])
        col2.append(cols[1])
    
    with open("col1.txt", "w") as file:
        file.write("\n".join(col1))
    
    with open("col2.txt", "w") as file:
        file.write("\n".join(col2))
