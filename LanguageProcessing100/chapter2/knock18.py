
if __name__ == "__main__":
    with open("hightemp.txt") as file:
        lines = file.readlines()
    
    for line in sorted(lines, key=lambda cols: cols.split()[2], reverse=True):
        print(line.rstrip("\n"))
