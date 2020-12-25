a=10

def sompething():
#    global a
    x=globals()['a']
    a=15
    print('in fucn :',a)

sompething()
print('out func',a)
