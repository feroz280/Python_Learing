age =int(input("Enter your age :"))
if (age>=18):
    print("You can Join")
elif(age==0): # number of elif can be added 
    print("You entered 0 which is not valid age !")
elif(age<0):
    print("You enterd negative age which is invalid")
else: # else will only execute when if and all elif fails
    print("You are below age , You can't join !")

print(" Thanks for coming...!!")