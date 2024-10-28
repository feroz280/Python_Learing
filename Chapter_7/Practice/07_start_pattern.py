# print("*")
print("SQUAR  PATTERN")
n=5
for i in range(n) :
    for j in range(5):
        print("*", end="  ")
    print()
print("INCREASING PATTERN")
n=5
for i in range(n) :
    for j in range(i+1):
        print("*", end="  ")
    print()
print("DECREASING PATTERN")
n=5
for i in range(n) :
    for j in range(i,n):
        print("*", end="  ")
    print()
print("RIGHT TRRIANGLE")
n=5
for i in range(n) :
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
        
print("RIGHT DECREASING TRIANGLE")

n=5
for i in range(n) :
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n):
        print("*", end=" ")
    print()

print("HILL PATTERN")
n=5
for i in range(n) :
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
print("DECREASING HILL PATTERN")
n=5
for i in range(n) :
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n-1):
        print("*", end=" ")
    for j in range(i,n):
        print("*", end=" ")
    print()

print("DIMONND PATTERN")
n=5
for i in range(n-1) :
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(n) :
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n-1):
        print("*", end=" ")
    for j in range(i,n):
        print("*", end=" ")
    print()
