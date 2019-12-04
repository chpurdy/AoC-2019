with open('input.txt') as f:
    data = []
    for line in f:
        data.append(line)
    data1 = data[0]
    data2 = data[1]
line1 = data1.split(',')
line2 = data2.split(',')

line1_pos = [0,0]
line2_pos = [0,0]

line1_coords = set()
line2_coords = set()

for move in line1:
    if move[0] == 'R':
        for i in range(int(move[1:])):
            line1_pos[0] += 1
            line1_coords.add(tuple(line1_pos))
    elif move[0] == 'L':
        for i in range(int(move[1:])):
            line1_pos[0] -= 1
            line1_coords.add(tuple(line1_pos))
    elif move[0] == 'D':
        for i in range(int(move[1:])):
            line1_pos[1] -= 1
            line1_coords.add(tuple(line1_pos))
    elif move[0] == 'U':
        for i in range(int(move[1:])):
            line1_pos[1] += 1
            line1_coords.add(tuple(line1_pos))
    else:
        print('something is wrong')
    

for move in line2:
    if move[0] == 'R':
        for i in range(int(move[1:])):
            line2_pos[0] += 1
            line2_coords.add(tuple(line2_pos))
    elif move[0] == 'L':
        for i in range(int(move[1:])):
            line2_pos[0] -= 1
            line2_coords.add(tuple(line2_pos))
    elif move[0] == 'D':
        for i in range(int(move[1:])):
            line2_pos[1] -= 1
            line2_coords.add(tuple(line2_pos))
    elif move[0] == 'U':
        for i in range(int(move[1:])):
            line2_pos[1] += 1
            line2_coords.add(tuple(line2_pos))
    else:
        print('something is wrong')
    

#print(line1_coords)
#print(line2_coords)

intersection = line1_coords.intersection(line2_coords)
line1_pos = [0,0]
line2_pos = [0,0]
print(intersection)
step = {}
steps = 0
for move in line1:
    
    if move[0] == 'R':
        for i in range(int(move[1:])):
            steps += 1
            line1_pos[0] += 1
            #print(1,tuple(line1_pos))
            if tuple(line1_pos) in intersection:
                if tuple(line1_pos) not in step.keys():
                    
                    step[tuple(line1_pos)] = [steps,0]
                    
    elif move[0] == 'L':
        for i in range(int(move[1:])):
            steps += 1
            line1_pos[0] -= 1
            #print(2,tuple(line1_pos))
            if tuple(line1_pos) in intersection:
                if tuple(line1_pos) not in step.keys():
                    step[tuple(line1_pos)] = [steps,0]
                    
    elif move[0] == 'D':
        for i in range(int(move[1:])):
            steps += 1
            line1_pos[1] -= 1
            #print(3,tuple(line1_pos))
            if tuple(line1_pos) in intersection:
                if tuple(line1_pos) not in step.keys():
                    step[tuple(line1_pos)] = [steps,0]
                    
    elif move[0] == 'U':
        for i in range(int(move[1:])):
            steps += 1
            line1_pos[1] += 1
            #
            #print(4,tuple(line1_pos))
            if tuple(line1_pos) in intersection:
                if tuple(line1_pos) not in step.keys():
                    step[tuple(line1_pos)] = [steps,0]
                    
    else:
        print('something is wrong')
    
steps = 0
for move in line2:
    if move[0] == 'R':
        
        for i in range(int(move[1:])):
            steps += 1
            line2_pos[0] += 1
            if tuple(line2_pos) in intersection:
                if step[tuple(line2_pos)][1] == 0:
                    step[tuple(line2_pos)][1] = steps
                    
    elif move[0] == 'L':
        
        for i in range(int(move[1:])):
            steps += 1
            line2_pos[0] -= 1
            if tuple(line2_pos) in intersection:
                if step[tuple(line2_pos)][1] == 0:
                    step[tuple(line2_pos)][1] = steps
                    
    elif move[0] == 'D':
        
        for i in range(int(move[1:])):
            steps += 1
            line2_pos[1] -= 1
            if tuple(line2_pos) in intersection:
                if step[tuple(line2_pos)][1] == 0:
                    step[tuple(line2_pos)][1] = steps
                    
    elif move[0] == 'U':
        
        for i in range(int(move[1:])):
            steps += 1
            line2_pos[1] += 1
            if tuple(line2_pos) in intersection:
                if step[tuple(line2_pos)][1] == 0:
                    step[tuple(line2_pos)][1] = steps
                    
    else:
        print('something is wrong')

print(step)

shortest = 100000000000000000000000
for coord, dist in step.items():
    shortest = min(shortest,dist[0]+dist[1])

print(shortest)
