f = open ("nimsis0.txt", "r")
n = f.readline()

y = {

}

for x in range(int(n)):
    name = f.readline()
    splitted = name.split()
    y[splitted[0]] = splitted[1]
print(y)

y2 = {

}

for r in range(int(n)):
    name = f.readline()
    splitted2 = name.split()
    y2[splitted2[0]] = splitted2[1]
print(y2)

print(y + y2)
