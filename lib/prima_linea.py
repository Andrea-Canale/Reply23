def parse_size():
    with open('testo.txt') as f:
        Linea1 = f.readline().strip()
        C, L, S = map(int, Linea1.split())
        return [C, L, S]
