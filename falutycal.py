''''
Python Exercise 2 - Faulty Calculator  45 * 3 = 555
59+9 = 77
59/6 = 4     '''


print('Enter First Number')
a=int(input())

print('Enter Second Number')
b=int(input())

print('Enter a operator ')
print('+\t-\t*\t/\t')
c=input()

if a == 59 and b==6 and c=='+':
    print('77')
elif a==45 and b==3 and c=='*':
    print('The ans is : 555')

elif a==59 and b==6 and c=='/':
    print('The ans is : 4')

elif a==43 and b==8 and c=='-':
    print('The ans is : 888')

elif c=='+':
    print('The ans is : ',a+b)

elif c=='-':
    print('The ans is : ',a-b)

elif c=='*':
    print('The ans is : ',a*b)

elif c=='/':
    print('The ans is : ',a/b)

else:
    print(' Error')