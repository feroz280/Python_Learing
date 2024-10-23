'''
write a program to greet all the
person names stored in a list 'l' and which starts with S.

'''

# l = ["Harry" , "Soham" , "Sachin" , "Rahul"]
# for n in range(len(l)):
#     print(f"{l[n]} Congratulation you got seleted...")

l = ["Harry" , "Soham" , "Sachin" , "Rahul"]
for n in l :
    if(n.startswith("S")):
        print(f"Wel Come {n}")