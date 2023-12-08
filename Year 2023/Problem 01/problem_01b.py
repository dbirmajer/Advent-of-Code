import regex

values = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def digit(s: str) -> str:
    if s in values.keys():
        return values[s]
    else:
        return s


pattern = r"one|two|three|four|five|six|seven|eight|nine|[1-9]"
first_rgx = regex.compile(pattern)
last_rgx = regex.compile(pattern, flags=regex.REVERSE)

filename = "input.txt"
with open(filename) as diary_file:
    acc = 0
    for line in diary_file:
        first = first_rgx.search(line)
        last = last_rgx.search(line)
        acc += int(digit(first.captures()[0]) + digit(last.captures()[0]))

print(acc)
