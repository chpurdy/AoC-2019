stop = False
for i in range(100):
    if stop:
        break
    for j in range(100):
        with open('input.txt') as f:
            data = f.read()

        data = [int(x) for x in data.split(',')]
        #print(data)

        data[1] = i
        data[2] = j
        curr_ind = 0
        while True:
            op_code = data[curr_ind]
            if op_code == 99:
                break

            pos1 = data[curr_ind + 1]
            pos2 = data[curr_ind + 2]
            to_pos = data[curr_ind + 3]
            if op_code == 1:
                data[to_pos] = data[pos1] + data[pos2]
            elif op_code == 2:
                data[to_pos] = data[pos1] * data[pos2]
            else:
                print('something is wrong - opcode',op_code)
                break
            curr_ind += 4
        if data[0] == 19690720:
            print(i,j)
            print(i*100+j)
            stop = True
            break


