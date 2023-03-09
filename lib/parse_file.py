def open_line(filename):
    with open(filename) as file:
        i = 0
        for line in file:
            if i == 1:  # Linea 2
                return line.replace("\n", "")   # Remove \n
            else:
                i += 1
                continue

def parse_snacks(line):
    snacks_raw = line.split(" ")
    return snacks_raw