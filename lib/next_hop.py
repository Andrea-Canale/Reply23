import parse_file as parser

lines_matrix = parser.open_line_matrix("../example.txt")
matrix = parser.parse_matrix(lines_matrix)
#lines_snakes = parser.open_line_snacks("../example.txt")
#snakes = parser.parse_snacks(lines_snakes)

def next_hop(x, y, l):
    valori_vicini = []
    valori_vicini.append(matrix[x+1][y]['value'])
    valori_vicini.append(matrix[x][y+1]['value'])
    valori_vicini.append(matrix[x+-1][y]['value'])
    valori_vicini.append(matrix[x][y-1]['value'])

    print(matrix)


print(next_hop(1, 1, 0))