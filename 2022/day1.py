calories = list(open("input_day1", "r"))
# f is a list of strings ending with or containing only \n

elf_all_calories = 0
all_elves = []
for cal in calories:
    if cal == '\n': # new elf
        all_elves.append(elf_all_calories)
        elf_all_calories = 0
    else: # sum calories
        elf_all_calories += int(cal.rstrip())

all_elves_desc = sorted(all_elves, reverse=True)
print(all_elves_desc[0])

top3_sum = 0
top3 = all_elves_desc[:3]
for c in top3:
    top3_sum += c
print(top3_sum)