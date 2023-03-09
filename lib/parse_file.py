def open_line_snacks(filename):
    with open(filename) as file:
        i = 0
        for line in file:
            if i == 1:  # Linea 2
                return line.replace("\n", "")   # Remove \n
            else:
                i += 1
                continue

def open_line_matrix(filename):
    matrix_raw = []
    with open(filename) as file:
        i = 0
        for line in file:
            if i > 1:
                matrix_raw.append(line)
            i += 1
        return matrix_raw

def parse_snacks(line):
    snacks_raw = line.split(" ")
    return snacks_raw

def parse_matrix(lines):
    matrix = []
    for line in lines:
        matrix.append(line.split(" "))
    
    i = 0
    j = 0
    for matrix_element in matrix:
        for line in matrix_element:
            matrix[i][j] = matrix[i][j].replace("\n", "")
            j += 1
        j = 0
        i += 1

    return matrix
