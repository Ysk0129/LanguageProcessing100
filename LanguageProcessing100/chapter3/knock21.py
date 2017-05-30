
if __name__ == "__main__":

    with open("british_articles.txt") as file:
        lines = file.readlines()
    
    for line in lines:
        if "Category" in line:
            print(line.rstrip("\n"))
