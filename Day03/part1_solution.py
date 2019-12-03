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
closest = 1000000000000000000
for coord in intersection:
    if abs(coord[0]) + abs(coord[1]) < closest:
        closest = abs(coord[0]) + abs(coord[1])
print(closest)

