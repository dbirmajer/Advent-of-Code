import re

bag = {"red": 12, "green": 13, "blue": 14}

pattern = r"Game (?P<id>\d+): (?P<game>.+)$"
marbles_re = r"(\d+ green|\d+ red|\d+ blue)"

filename = "input.txt"
with open(filename) as games_file:
    acc = 0
    for line in games_file:
        m = re.match(pattern, line)
        if bool(m):
            turns = m.group('game').split(";")
            flag = True
            for turn in turns:
                for cubes in re.findall(marbles_re, turn):
                    value, color = re.match(r"(\d+) ([a-z]+)", cubes).groups()
                    flag = flag and (int(value) <= bag[color])
                    if not flag:
                        break
            if flag:
                acc += int(m.group('id'))
print(acc)
