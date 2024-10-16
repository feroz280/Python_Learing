multi = ("Apple" , "Mango" , 5 , 23.87 , True , "Muhmmad")
print(multi)

# tuples are immultable (can not be changed) if 
# we want to update the values in tuples then we must create a new 
# variable to store updated value BUT the original tuple will 
# remains same.

# FUNCTIONS IN TUPLE
numbers = (1,5,6,8,3,5,2,7,9,4,5)
# print(type(numbers))

# .count(value) [it will count occurance of value that how many times it appers in tuple]
cont = numbers.count(5)
print(cont)

print( 9 in numbers)# [it will check that if 9 is in the tuple or not]