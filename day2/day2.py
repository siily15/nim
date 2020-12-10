f = open("input.txt")
lines = f.readlines()

rec = 0

for line in lines:
    splitted = line.split()
    minmax = splitted[0].split("-")
    chor = splitted[1].strip(":")
    c = splitted[2].count(chor)
    if c >= int(minmax[0]) and c <= int(minmax[1]):
        rec += 1

print (rec)
