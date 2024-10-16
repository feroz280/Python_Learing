s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))

# its length will be 2 because inn python if the values are same then datatype does not matter hence 20 and 20.0 are considered as 1 value.And in sets unique vauess are take.