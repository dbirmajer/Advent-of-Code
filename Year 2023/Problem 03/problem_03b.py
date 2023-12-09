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
    for i in range(3):
        print(rows[i])
    print()
    gears_it = re.finditer(r"(\*)", rows[1])
    accum = 0
    numbers_0 = list(re.finditer(r"(\d+)", rows[0]))
    numbers_1 = list(re.finditer(r"(\d+)", rows[1]))
    numbers_2 = list(re.finditer(r"(\d+)", rows[2]))
    numbers_02 = numbers_0 + numbers_2    
    for m in gears_it:
        print(f"m.span() = {m.span()}")
        adjacent = 0
        ratio = 1
        ls = []
        gear, _ = [int(v) for v in m.span()]
        # print(f"gear = {gear}")
        for n in numbers_02:
            start, end = n.span()
            if (start <= gear - 1 and end >= gear) or  (gear <= end <= gear + 2) or (gear - 1 <= start <= gear + 1):
                adjacent += 1
                ratio *= int(n.group(0))
                ls.append(int(n.group(0)))
                #print(f"{n.group(0)}, gear = {gear}, start = {start}, end = {end}, adjacent = {adjacent}")
        for n in numbers_1:
            start, end = n.span()
            print(f"gear = {gear}, {n.group(0)}, start = {start}, end = {end}")
            if (end == gear) or (start == gear + 1):
                adjacent += 1
                ratio *= int(n.group(0))
                ls.append(int(n.group(0)))
                print(f"{n.group(0)}, gear = {gear}, start = {start}, end = {end}, adjacent = {adjacent}")
        if (adjacent == 2):
            print(ls)
            print(f"these two ratio = {ratio}")
            accum += ratio
    return accum

def main():
    matrix = wrapper(process_input("input.txt"))
    accum = 0
    for i in range(len(matrix) - 2):
        accum += find_parts(matrix[i : i + 3])
    print(accum)

if __name__ == "__main__":
    main()
