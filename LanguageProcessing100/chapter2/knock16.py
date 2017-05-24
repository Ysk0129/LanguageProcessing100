from sys import argv

if __name__ == "__main__":

    with open("hightemp.txt") as file:
        lines = file.readlines()
    
    if len(lines) % int(argv[1]) == 0:
        num_of_lines = int(len(lines) / int(argv[1]))
    else:
        num_of_lines = int(len(lines) / int(argv[1])) + 1

    for i in range(int(argv[1])):
        with open("splitted{0}".format(i), "w") as file:
            if i != num_of_lines:
                file.writelines(lines[i * num_of_lines: (i + 1) * num_of_lines - 1])
            else:
                file.writelines(lines[i * num_of_lines: len(lines) - 1])
