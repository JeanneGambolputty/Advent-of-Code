raw = list(open("input_day4", "r"))
clean = [r.rstrip() for r in raw]

count = 0

for c in clean:
    pairs = c.split(",")
    pair1 = pairs[0].split("-")
    pair1_range = set(range(int(pair1[0]), int(pair1[1])+1))
    pair2 = pairs[1].split("-")
    pair2_range = set(range(int(pair2[0]), int(pair2[1])+1))
    if pair1_range.issubset(pair2_range) or pair2_range.issubset(pair1_range):
        count += 1
    elif pair1_range.intersection(pair2_range) or pair2_range.intersection(pair1_range):
        count += 1
print(count)