raw = list(open("input_day3", "r"))
clean = [r.rstrip() for r in raw]

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
dicts = {} # key = letter from alphabet; val = eg a:1
for val in range(52):
    dicts[alphabet[val]] = val+1
sum_vals = 0

common = []
first_half = []
second_half = []

for i in clean:
    middle = len(i)//2
    first_half.append(i[:middle])
    second_half.append(i[middle:])

for (f, s) in zip(first_half, second_half):
    common.append(list(set(f).intersection(s))[0])

for c in common:
    sum_vals += dicts[c]

print(sum_vals)

index = 0
elf1 = []
elf2 = []
elf3 = []

for i in clean:
    if index % 3 == 0:
        elf1.append(i)
    elif index % 3 == 1:
        elf2.append(i)
    elif index % 3 == 2:
        elf3.append(i)
    index += 1

for (a, b, c) in zip(elf1, elf2, elf3):
    common.append(list(set(a).intersection(b).intersection(c))[0])

for c in common:
    sum_vals += dicts[c]

print(sum_vals)