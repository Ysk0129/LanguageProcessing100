import sys

class InvalidSplitException(Exception):
    def __init__(self, msg):
        self.msg = msg

def check_argv(n, lines):
    try:
        if len(lines) < n:
            raise InvalidSplitException("Argument division number is too large")
        if n == 0:
            raise InvalidSplitException("Can not divide by 0")

    except InvalidSplitException as e:
        print(e)
        return False

    return True


if __name__ == "__main__":

    with open("hightemp.txt") as file:
        lines = file.readlines()
        
    n = int(sys.argv[1])
    if not check_argv(n, lines):
        sys.exit()

    if len(lines) % n == 0:
        num_of_lines = int(len(lines) / n)
        rem = 0
    else:
        num_of_lines = int(len(lines) / n) + 1
        rem = len(lines) % n

    for i in range(n):
        with open("splitted{0}".format(i), "w") as file:
            if i == n - 1 and rem != 0:
                file.writelines(lines[i * num_of_lines:(i * num_of_lines) + rem])
            else:
                file.writelines(lines[i * num_of_lines: (i + 1) * num_of_lines])
