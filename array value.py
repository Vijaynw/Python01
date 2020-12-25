from array import *

arr= array('i',[])

n = int(input('Enter the length of array'))

for i in range(n):
    x=int(input('Enter the values'))
    arr.append(x)

#print(arr)

s = int(input('Enter the value to find'))
d=0
for c in arr:
    if c == s:
        print(d)
        break
print(s)








