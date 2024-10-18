marks = {
    "Ali" : 98,
    "Hassan" : 85,
    "Bilal" : 83,
    "Junaid" : 79,

}

# .items()  [this is used to print keys with their values in tuple form]
print(marks.items())

# .keys() [it will print all the keys in the dictionary]
print(marks.keys())

# .values() [it will print all the values in dictionary]
print(marks.values())

# .update({updated_key : updated_value}) , .update({new_key : new:value})   [it will update the key and values and also it can add new keys and values in the dictionary]
marks.update({"Junaid" : 99 , "Azeem" : 93})
print(marks)

# .get("key") [it will retrieve data of that key But it does not exists it will return None]
# But in case of Direct retriel it will return error.

print(marks.get("Junaid"))