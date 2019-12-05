with open('input.txt') as f:
    data = f.read()
        

    #data = '1002,4,3,4,33'

    data = [int(x) for x in data.split(',')]
    #print(data)


    curr_ind = 0
    while True:
        op_code = str(data[curr_ind])
        if op_code == '99':
            break

        pos1 = data[curr_ind + 1]
        pos2 = data[curr_ind + 2]
        to_pos = data[curr_ind + 3]
        if op_code[-1] == '1':
            if len(op_code) < 3:
                data[to_pos] = data[pos1] + data[pos2]
            else:
                if op_code[-3] == '0': # pos mode
                    d1 = data[pos1]
                elif op_code[-3] == '1': # immediate mode
                    d1 = pos1

                if len(op_code) < 4 or op_code[-4] == '0':
                    d2 = data[pos2]
                elif op_code[-4] == '1':
                    d2 = pos2
                data[to_pos] = d1 + d2            
            curr_ind += 4

        elif op_code[-1] == '2':
            if len(op_code) < 3:
                data[to_pos] = data[pos1] * data[pos2]
            else:
                if op_code[-3] == '0': # pos mode
                    d1 = data[pos1]
                elif op_code[-3] == '1': # immediate mode
                    d1 = pos1

                if len(op_code) < 4 or op_code[-4] == '0':
                    d2 = data[pos2]
                elif op_code[-4] == '1':
                    d2 = pos2
                data[to_pos] = d1 * d2            
            curr_ind += 4

        elif op_code[-1] == '3':
            ind = int(input("Input: "))
            data[pos1] = ind
            curr_ind += 2
        elif op_code[-1] == '4':
            if len(op_code) == 3:
                if pos1 != 0:
                    print("error at",op_code)
                print(pos1)
            else:
                if data[pos1] != 0:
                    print("error at",op_code)
                print(data[pos1])
            curr_ind += 2
        else:
            print('something is wrong - opcode',op_code)
            break


