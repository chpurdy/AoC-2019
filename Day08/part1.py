with open('input.txt') as f:
    data = f.read().strip()

wide = 25
tall = 6
layer_area = wide * tall

i = 0
layers = []
while i < len(data):
    layers.append(data[i:i+layer_area])
    i += layer_area

print(len(layers))
min_num_zeros = 100000000000000
max_layer = 0
for i,layer in enumerate(layers):
    if layer.count('0') < min_num_zeros:
        min_num_zeros = layer.count('0')
        max_layer = i
print(max_layer)

print(layers[max_layer])
print(layers[max_layer].count('1') * layers[max_layer].count('2'))
