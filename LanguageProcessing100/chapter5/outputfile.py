import CaboCha

def output_cabocha_file(in_file_name, out_file_name):
    with open(in_file_name) as file:
        lines = file.readlines()
    with open(out_file_name, "w") as file:
        cabocha = CaboCha.Parser()
        for line in lines:
            file.write(cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE))

if __name__ == "__main__":
    output_cabocha_file("../chapter4/neko.txt", "neko.txt.cabocha")
