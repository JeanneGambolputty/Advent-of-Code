f = list(open("input_day1", "r"))
# f is a list of strings ending with or containing only \n

all_elves = []
elf_all_calories = 0
top3_sum = 0
for i in f:
    if i == '\n':
        all_elves.append(elf_all_calories)
        elf_all_calories = 0
    else:
        elf_all_calories += int(i.rstrip())

all_elves_desc = sorted(all_elves, reverse=True)
top3 = all_elves_desc[:3]
for c in top3:
    top3_sum += c
print(top3_sum)