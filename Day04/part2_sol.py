# 193651-649729
#193651,649729+1
count = 0
for i in range(193651,649729+1):
    num = str(i)
    if num[0] == num[1] and num[0] != num[2]: 
        double_found = True
    elif num[1] == num[2] and num[1] != num[3] and num[1] != num[0]:
        double_found = True 
    elif num[2] == num[3] and num[2] != num[4] and num[2] != num[1]:
        double_found = True
    elif num[3] == num[4] and num[3] != num[5] and num[3] != num[2]:
        double_found = True
    elif num[4] == num[5] and num[4] != num[3]:
        double_found= True
    else:
        double_found = False
    

    if num[0] <= num[1] <= num[2] <= num[3] <= num[4] <= num[5]:
        if double_found:
            print(num)
            count += 1

print(count)