f = open ("nimsis0.txt", "r")
n = f.readline()

y = {}
y2 = {}
y3 = {}
for x in range(int(n)):
    name = f.readline()
    splitted = name.split()
    y[splitted[0]] = splitted[1]

for r in range(int(n)):
    name2 = f.readline()
    splitted2 = name2.split()
    y2[splitted2[0]] = splitted2[1]

for z in y:
    for v in y2:
        if z == v:
            y3[y[z]] = y2[v]
print(y3)
