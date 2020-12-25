
def person(name, **data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)
person('rock', age=68 , city= 'mumbai', mob= 985652)