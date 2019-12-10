
def intcode_computer(in1, in2):
    with open('input.txt') as f:
        data = f.read()
        #data = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
        data = [int(x) for x in data.split(',')]
    #print(data)

    incount = 0
    inputs = (in1, in2)

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
            ind = inputs[incount] #int(input("Input: "))
            incount += 1
            data[pos1] = ind
            curr_ind += 2

        elif op_code[-1] == '4':
            if len(op_code) == 3:
                if pos1 != 0:
                    pass
                    #print("error at",op_code)
                #print(pos1)
                return(pos1)
            else:
                if data[pos1] != 0:
                    pass
                    #print("error at",op_code)
                #print(data[pos1])
                return(data[pos1])
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





if __name__ == "__main__":
    import itertools
    max_out = -1000000000
    for seq in list(itertools.permutations([0,1,2,3,4],5)):
        print(seq)
        a_out = intcode_computer(seq[0],0)
        b_out = intcode_computer(seq[1],a_out)
        c_out = intcode_computer(seq[2],b_out)
        d_out = intcode_computer(seq[3],c_out)
        e_out = intcode_computer(seq[4],d_out)
        if e_out > max_out:
            max_out = e_out
            max_seq = seq
    print(max_out, max_seq)
    