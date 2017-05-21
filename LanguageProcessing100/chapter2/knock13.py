
if __name__ == "__main__":
    
    with open("col1.txt") as file:
        col1 = file.readlines()
    
    with open("col2.txt") as file:
        col2 = file.readlines()

    with open("merge.txt", "w") as file:
        for c1, c2 in zip(col1, col2):
            file.write(c1.rstrip("\n") + "\t" + c2)
