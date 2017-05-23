from sys import argv

if __name__ == "__main__":

    with open("hightemp.txt") as file:
        lines = file.readlines()[-int(argv[1]):]

    for line in lines:
        print(line.rstrip("\n"))
