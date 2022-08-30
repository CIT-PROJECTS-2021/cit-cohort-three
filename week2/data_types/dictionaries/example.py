car = { "brand": "Ford", "model": "Mustang", "year": 1964 }


print(car.get('model'))
print(car.get('brand'))


cars_list = ["Ford", "Volvo", "BMW"]

for index, car in enumerate(cars_list):
    print(index, car)


# Find the output of the following program:

D = {1 : 1, 2 : '2', '1' : 1, '2' : 3} 
D['1'] = 2

print(D)
# 1
# print(D[D[D[str(D[1])]]])
# print(D[D[D[str(1)]]]) 
# print(D[D[D["1"]]])  
# print(D[D[2]]) 
print(D["2"]) # 3

# why does set order its keys?
# This is because sets are unordered. therefore, the order of the keys is not guaranteed.

# reverse a set
s = set([1, 2, 3, 4, 5])
s_reversed = set(reversed(s))