with open("input.txt") as infile:
    lines = infile.readlines()

cals = []
temp = 0
for i in range(len(lines)):
    if lines[i] == "\n":
        cals.append(temp)
        temp = 0
    else:
        temp += int(lines[i].strip())
if lines[-1] != "\n":
    cals.append(temp)

print(sum(sorted(cals)[-1:-4:-1]))