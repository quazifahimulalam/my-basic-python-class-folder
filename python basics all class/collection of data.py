numbers = [10,20,50,90]
fruits = ['apple','pineapple','banana','orange']

numbers.append(100)
print("after append:",numbers)

fruits.insert(2 , "tomato")
print("after insert:" , fruits)

numbers.remove(20)
print("äfter remove:" , numbers)

last_fruit = fruits.pop()
print("after pop:",fruits)
print("laste fruit popped:" , last_fruit)

banana_index = fruits.index("banana")
print("index of banana:" , banana_index)

numbers.sort()
print("after sort:" , numbers)

fruits.reverse()
print("after reverse" , fruits)

count_20 = numbers.count(20)
print("count of 20 in numbers arrray:" , count_20)

fruits.extend(numbers)
print("after extend:" , fruits)

fruits_copy = fruits.copy()
print("fruits copy:" , fruits_copy)