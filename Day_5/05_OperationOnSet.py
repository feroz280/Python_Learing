s = {1,2,3,4,5,6,7,8,9}

# len(set_name) [it will print length of of the set]
print(len(s))

#.remove(element want to reove) 

s.remove(9)
print(s)

print("UNION AND INTERSECTION")
set_1 = {3,6,7,8,5,2}
set_2 = {9,8,7,6,5,4,1}
print("set_1 = {3,6,7,8,5,2}")
print("set_2 = {9,8,7,6,5,4,1}")
print(f"UNION :{set_1.union(set_2)}")
print(f"INTERSECTION :{set_1.intersection(set_2)}")