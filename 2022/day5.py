raw = list(open("input_day5", "r"))
clean = [r.rstrip() for r in raw]
stacks = {}
sorted_stacks = {}
top_letters = ''

for c in clean:
    if '[' in c: # rows with elements to build original stacks; transpose in reverse order
        for i in range(len(c)):
            if c[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                stack = int((i+3)/4)
                if stack not in stacks:
                    stacks[stack] = []
                stacks[stack].append(c[i])

for s, crate in stacks.items(): # put each stack in right order
    sorted_stacks[s] = stacks[s][::-1]

for c in clean: # record & apply movements
    if c != '' and c[0] == 'm': # rows with elements related to movements
        for i in range(len(c)):
            if c[i] == 'e':
                nbr_first_digit = c[i+2]
                index1 = i+2
            if c[i] == 'f':
                nbr_last_digit = c[i-2]
                index2 = i-2
                # get no. of items to be moved
                if index1 != index2:
                    nbr = int(nbr_first_digit+nbr_last_digit)
                else:
                    nbr = int(nbr_last_digit)
            # get 'from'-stack# & 'to'-stack#
            if c[i] == 't':
                from_ = int(c[i-2])
                to = int(c[i+3])
                    
        # reverse order of crates of 'from'-stack (to pop them easily) & get last nbr crates
        # for s in list(reversed(sorted_stacks[from_]))[:nbr]: ## PART I
        for s in sorted_stacks[from_][(len(sorted_stacks[from_]) - nbr):]: ## PART II
            sorted_stacks[to].append(s) # add element to 'to'-stack
            del sorted_stacks[from_][-1] # remove last element from 'from'-stack
            #sorted_stacks[from_].remove(s) # remove added element from 'from'-stack

for k in sorted(sorted_stacks): # sort stacks by key in asc order
    if sorted_stacks[k] != []:
        top_letters += sorted_stacks[k][-1]
print(top_letters)