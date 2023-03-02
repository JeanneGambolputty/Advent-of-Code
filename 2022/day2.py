raw = list(open("input_day2", "r"))
clean = [r.rstrip() for r in raw]
shape = []
score = []

### Part I ###

for i in clean:
    
    if i[2] == 'X': #rock
        p2 = 1
        if i[0] == 'A': #rock 
            score.append(3) #
        elif i[0] == 'B': #paper
            score.append(0)
        elif i[0] == 'C': #scissors
            score.append(6)
    elif i[2] == 'Y': #paper
        p2 = 2
        if i[0] == 'A': #rock 
            score.append(6)
        elif i[0] == 'B': #paper
            score.append(3) #
        elif i[0] == 'C': #scissors
            score.append(0)
    elif i[2] == 'Z': #scissors
        p2 = 3
        if i[0] == 'A': #rock 
            score.append(0)
        elif i[0] == 'B': #paper
            score.append(6)
        elif i[0] == 'C': #scissors
            score.append(3) #

    shape.append(p2)

print(sum(shape) + sum(score))

### Part II ###

for i in clean:
    
    if i[2] == 'X': #LOSE
        score.append(0)
        if i[0] == 'A': #rock 
            shape.append(3) #scissors
        elif i[0] == 'B': #paper
            shape.append(1) #rock
        elif i[0] == 'C': #scissors
            shape.append(2) #paper
    elif i[2] == 'Y': #DRAW
        score.append(3)
        if i[0] == 'A': #rock 
            shape.append(1)
        elif i[0] == 'B': #paper
            shape.append(2) #
        elif i[0] == 'C': #scissors
            shape.append(3)
    elif i[2] == 'Z': #WIN
        score.append(6)
        if i[0] == 'A': #rock 
            shape.append(2) #paper
        elif i[0] == 'B': #paper
            shape.append(3) #scissors
        elif i[0] == 'C': #scissors
            shape.append(1) #rock

print(sum(shape) + sum(score))