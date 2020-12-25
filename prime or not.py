x = int(input('Enter number'))


#print(x)

#x = int(input())

for i in range(2,x):

    if x % i ==0:

        print("not prime")

        break

else:

    print("Prime")
