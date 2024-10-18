numbers = [1,6,8,3,5,2,7,9,4]
print(numbers)

# .sort()  [it will sort the numbers]
numbers.sort()
print(numbers)

# .reverse() [it will reverse the list numbers]
numbers.reverse()
print(numbers)

# .append(value) [it will add the given value at the end of the list]
numbers.append(10)
print(numbers)

# numbers.append("Numbers")
# print(numbers)


# .insert(index_value , value want to insert) [it will insert an element at particular index given by the user]

numbers.insert(5,11) # first value is index and the second is the value which will be inserted at that index
print(numbers)
numbers.sort()
print(numbers)


# .pop(index value)  [it will delete value from the index and return its value]
numbers.pop(10)
print(numbers)


# .remove(value want to remove from the list)
numbers.remove(10)
print(numbers)