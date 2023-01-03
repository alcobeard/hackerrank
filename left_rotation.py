import math

d_list = []
d = 5
l_itter = 4

for i in range(1, d+1):
    d_list.append(i)

l_itter = l_itter - d * (l_itter // d)
print(l_itter)

while l_itter != 0:
    poper = d_list.pop(0)
    d_list.append(poper)
    l_itter -= 1

print(d_list)