import re
import functools as ft

pattern = r"Game (\d+): (?P<game>.+)$"
cubes_re = r"(\d+ green|\d+ red|\d+ blue)"


with open("input.txt") as games_file:
    acc = 0
    for line in games_file:
        m = re.match(pattern, line)
        if bool(m):
            turns = m.group('game').split(";")
            flag = True
            bag_max = {"red": 0, "green": 0, "blue": 0}
            for turn in turns:
                cubes_dict = {}
                for cubes in re.findall(cubes_re, turn):
                    value, color = re.match(r"(\d+) ([a-z]+)", cubes).groups()
                    cubes_dict[color] = int(value)
                    if cubes_dict[color] > bag_max[color]:
                        bag_max[color] = cubes_dict[color]
            acc += ft.reduce(lambda x, y: x * y, bag_max.values(), 1)
print(acc)
