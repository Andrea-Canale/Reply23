import lib.parse_file as parser

lines_matrix = parser.open_line_matrix("example.txt")
lines_snacks = parser.open_line_snacks("example.txt")
snacks = parser.parse_snacks(lines_snacks)
matrix = parser.parse_matrix(lines_matrix)