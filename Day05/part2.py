with open('input.txt') as f:
    data = f.read()

#     data = '''3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
# 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
# 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'''
    #data = '3,3,1105,-1,9,1101,0,0,12,4,12,99,1'

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
        try:
            to_pos = data[curr_ind + 3]
        except:
            pass
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

        elif op_code[-1] == '5':  # jump-if-true
            if len(op_code) < 3: # position mode
                if data[pos1] != 0:
                    curr_ind = data[pos2]
                else:
                    curr_ind += 3
            else:
                if op_code[-3] == '0':
                    
                    if data[pos1] != 0:
                        curr_ind = pos2
                    else:
                        curr_ind += 3
                else:
                    if len(op_code) == 4:
                        if pos1 != 0:
                            curr_ind = pos2
                        else:
                            curr_ind += 3 
                    else:
                        if pos1 != 0:
                            curr_ind = data[pos2]
                        else:
                            curr_ind += 3

        elif op_code[-1] == '6': # jump-if-false
            if len(op_code) < 3: # position mode
                if data[pos1] == 0:
                    curr_ind = data[pos2]
                else:
                    curr_ind += 3
            else:
                if op_code[-3] == '0':
                    if data[pos1] == 0:
                        curr_ind = pos2
                    else:
                        curr_ind += 3
                else:
                    if len(op_code) == 4:
                        if pos1 == 0:
                            curr_ind = pos2
                        else:
                            curr_ind += 3
                    else:
                        if pos1 == 0:
                            curr_ind = data[pos2]
                        else:
                            curr_ind += 3
        
        elif op_code[-1] == '7': # less than
            if len(op_code) < 3:
                if data[pos1] < data[pos2]:
                    data[to_pos] = 1
                else:
                    data[to_pos] = 0
            
            else:
                if op_code[-3] == '0':
                    if data[pos1] < pos2:
                        data[to_pos] = 1
                    else:
                        data[to_pos] = 0
                
                else:
                    if len(op_code) < 4:
                        if pos1 < data[pos2]:
                            data[to_pos] = 1
                        else:
                            data[to_pos] = 0
                    else:
                        if pos1 < pos2:
                            data[to_pos] = 1
                        else:
                            data[to_pos] = 0
            curr_ind += 4

        elif op_code[-1] == '8': #equals
            if len(op_code) < 3:
                if data[pos1] == data[pos2]:
                    data[to_pos] = 1
                else:
                    data[to_pos] = 0
            
            else:
                if op_code[-3] == '0':
                    if data[pos1] == pos2:
                        data[to_pos] = 1
                    else:
                        data[to_pos] = 0
                
                else:
                    if len(op_code) < 4:
                        if pos1 == data[pos2]:
                            data[to_pos] = 1
                        else:
                            data[to_pos] = 0
                    else:
                        if pos1 == pos2:
                            data[to_pos] = 1
                        else:
                            data[to_pos] = 0
            curr_ind += 4
        

        else:
            print('something is wrong - opcode',op_code)
            break


