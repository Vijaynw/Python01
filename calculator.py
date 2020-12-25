
print("___________________Hello________________________")
print('                   Cals')

print('Make a choice:')
print('1.: +')
print('2.: -')
print('3.: *')
print('4.: %')
z = int(input("Enter: "))

if z <= 4:


    x = int(input("Enter 1st number"))
    y = int(input("Enter 2st number"))

    if z == 1:
        c = x+y
        print("+ : ", c)
    elif z == 2:
        c = x-y
        print("- : ", c)

    elif z == 3:
        c = x*y
        print("* : ", c)
    elif z == 4:
        c = x % y
        print("% : ", c)
else:
    print("wrong input")