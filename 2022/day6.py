raw = list(open("input_day6", "r"))
datastream_buffer = raw[0]
parsed = []
#for d in range(4): ## PART I
for d in range(14): ## PART II
     parsed.append(datastream_buffer[d])
#counter = 4 ## PART I
counter = 14 ## PART II

if len(set(parsed)) != len(parsed): #if parsed (of 4 or 14 characters) X contain only unique characters
    #for db in range(4, len(datastream_buffer)): ## PART I
    for db in range(14, len(datastream_buffer)): ## PART II
        counter +=1
        del parsed[0] #pops the first element in parsed so the length stays N (4 or 14) -1
        parsed.append(datastream_buffer[db]) #adds new element => length of parsed = N
        if len(set(parsed)) == len(parsed):
            print(counter)
            break