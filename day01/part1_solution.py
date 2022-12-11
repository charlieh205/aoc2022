with open("input.txt") as infile:
    lines = infile.readlines()

most_cals = 0
temp = 0
for i in range(len(lines)):
    if lines[i] != "\n":
        temp += int(lines[i].strip())
    else:
        if temp > most_cals:
            most_cals = temp
            temp = 0
        else:
            temp = 0

print(most_cals)