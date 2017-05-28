
if __name__ == "__main__":

    with open("hightemp.txt") as file:
        first_column_lines = [line.split()[0] for line in file.readlines()]
    
    col1 = {}
    for line in first_column_lines:
        if line in col1:
            col1[line] += 1
        else:
            col1[line] = 1

    for prefecture, occurrences in sorted(col1.items(), key=lambda x: x[1],reverse=True):
        print("{0} : {1}".format(prefecture, occurrences))
