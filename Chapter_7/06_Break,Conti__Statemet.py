# break statement...

print("Break statement works like this...")

for n in range(1,6):
    if(n==4):
        break # it will terminate the program if n == 3 and furhter programm will be skiped..
    print(n)


'''
continue statement only skip the particular iteration 
which is provided in the if condition

'''
print("continue statement works like this..")

for i in range(1,6):
    if (i==3):
        continue # this will skip the value when i==3 remaining will be excuted
    print(i)



# pass statement...
'''
it will skip the one portion of the program and run next ...

'''
for t in range(1,5):
    pass
# pass will skip the for loop and will run further program..
u = 0
while (u<5):
    print("tata")
    u += 1
