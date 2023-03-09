import parse_file as parser
import prima_linea as dati

lines_matrix = parser.open_line_matrix("../example.txt")
matrix = parser.parse_matrix(lines_matrix)
[C, R, S] = dati.parse_size("../example.txt")
#lines_snakes = parser.open_line_snacks("../example.txt")
#snakes = parser.parse_snacks(lines_snakes)

def is_empty(r, c):
    return matrix[r][c]['snake'] == 0

def cell_sx(r, c):
    if c-1 < 0:
        c = C-1
    else:
        c -= 1
    if is_empty(r, c):
        return [r, c]
    return [-1, -1]

def cell_dx(r, c):
    if c+1 == C:
        c = 0
    else:
        c += 1
    if is_empty(r, c):
        return [r, c]
    return [-1, -1]

def cell_up(r, c):
    if r-1 < 0:
        r = R-1
    else:
        r -= 1
    if is_empty(r, c):
        return [r, c]
    return [-1, -1]

def cell_down(r, c):
    if r+1 == R:
        r = 0
    else:
        r += 1
    if is_empty(r, c):
        return [r, c]
    return [-1, -1]


def next_hop(r, c, l):
    [x_up, y_up] = cell_up(r, c)
    celle = [
            {'coord':cell_up(r, c),
             'val': -1
            },
            {'coord':cell_down(r, c),
             'val': -1
            },
            {'coord':cell_dx(r, c),
             'val': -1
            },
            {'coord':cell_sx(r, c),
             'val': -1
            }]
    celle[0]['val'] = matrix[celle[0]['coord'][0]][celle[0]['coord'][1]]['value']
    celle[1]['val'] = matrix[celle[1]['coord'][0]][celle[1]['coord'][1]]['value']
    celle[2]['val'] = matrix[celle[2]['coord'][0]][celle[2]['coord'][1]]['value']
    celle[3]['val'] = matrix[celle[3]['coord'][0]][celle[3]['coord'][1]]['value']
    print(celle)
    

next_hop(5, 9, 0)