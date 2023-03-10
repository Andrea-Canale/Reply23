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
    for matrix_element in matrix:       #gubbo e stato qui anche se non ha fatto nientee
        for line in matrix_element:
            is_warm = matrix[i][j] == '*'
            value = ''
            if matrix[i][j].replace("\n", "") != '*':
                value = int(matrix[i][j].replace("\n", ""))
            else:
                value = -1 

            matrix[i][j] = {
                "value": value,
                "snake": 0,
                "cmd": '',
                "worm": is_warm,
                "worm_out": [],
                "first_cell": False
            }
            j += 1
        j = 0
        i += 1

    return matrix

def max_coordinate(matrix):
    i=0
    j=0
    x_max=0
    y_max=0
    n_max=0
    for row in matrix:
        for cel in row:
            if cel['value']!="*" and cel['value']>n_max and cel['snake']==0:
                n_max = cel['value']
                x_max = j
                y_max = i
            j+=1
        i+=1
    max = [x_max, y_max]
    return max
