import re

def process_input(file: str) -> list[str]:
    '''Reads the input file and returns a list of its lines'''
    with open(file) as input_file:
        lines = input_file.read().split()
        return lines

    
def wrapper(lines: list[str]) -> list[str]:
    '''Adds a border of '.' around the input matrix'''
    ls = ['.' + line + '.' for line in lines]
    s = '.' * len(ls[0])
    return [s] + ls + [s]


def find_parts(rows: list[str]) -> list[int]:
    '''input: a list of 3 rows from the wrapperd matrix
    output: the list of parts on the middle row'''
    # print("rows", rows)
    gears_it = re.finditer(r"(\*)", rows[1])
    numbers_it = re.finditer(r"(\d+)", rows[1])
    accum = 0
    for m in gears_it:
        # print(rows[1])
        print(m.span())
    for m in numbers_it:
        start, end = m.span()
        above = all(c == '.' for c in rows[0][start-1 : end + 1])
        below = all(c == '.' for c in rows[2][start-1 : end + 1])
        left = all(c == '.' for c in [rows[0][start - 1], rows[1][start - 1], rows[2][start - 1]])
        right = all(c == '.' for c in [rows[0][end], rows[1][end], rows[2][end]])
        if not (all((above, below, left, right))):
            accum += int(m.group(0))
    return accum

def main():
    matrix = wrapper(process_input("example.txt"))
    accum = 0
    for i in range(len(matrix) - 2):
        # find_parts(matrix[i : i + 3])
        accum += find_parts(matrix[i : i + 3])
    print(accum)

if __name__ == "__main__":
    main()
