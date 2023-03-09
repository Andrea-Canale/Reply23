def parse_size(file):
    with open(file) as f:
        Linea1 = f.readline()
        C, L, S = map(int, Linea1.split())
        return [C, L, S]
