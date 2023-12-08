import re

filename = "input.txt"
with open(filename) as diary_file:
    acc = 0
    for line in diary_file:
        arr = re.findall("[0-9]", line)
        acc += int(arr[0] + arr[-1])
print(acc)
