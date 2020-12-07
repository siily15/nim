import re

def count_bags(color):
    for l in lines:
        match = re.search('(.*) bags contain .*' + color, l)
        if match:
            print(match.group(1))
            count_bags(match.group(1))

f = open ("example.txt")
lines = [l.strip() for l in f.readlines()]

print(count_bags('chiny gold'))
