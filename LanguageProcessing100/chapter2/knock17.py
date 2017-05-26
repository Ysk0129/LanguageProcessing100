
if __name__ == "__main__":

    with open("hightemp.txt") as file:
        first_column_lines = [line.split()[0] for line in file.readlines()]

    unique_strings = set(first_column_lines)

    print(unique_strings)
