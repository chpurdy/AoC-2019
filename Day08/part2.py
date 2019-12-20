with open('input.txt') as f:
    data = f.read().strip()

wide = 25
tall = 6
layer_area = wide * tall

# data = '0222112222120000'
# wide = 2 
# tall = 2
# layer_area = wide*tall

i = 0
layers = []
while i < len(data):
    layers.append(data[i:i+layer_area])
    i += layer_area

print(layers[0])

result = []

for i in range(len(layers[0])):
    result.append(layers[0][i])
    
    for layer in layers:
        
        if result[i] == '2' and layer[i] != '2':
           
            
            result[i] = layer[i]
            break
    
print(len(result))
#print(''.join(result))

for i in range(tall):
    for j in range(wide):
        if result[i*wide + j] == '0':
            print("#",end="")
        else:
            print(" ",end="")
        #print(result[i*wide + j],end="")
    print()
        