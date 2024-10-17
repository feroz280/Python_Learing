# write a program to find the greatest of four numbers entered by the user.

first_number = input("Enter first number :")
second_number = input("Enter seconnd number :")
third_number = input("Enter third number :")
fourth_number = input("Enter fourth number :")
if(first_number>second_number):
    if(first_number>third_number):
        if(first_number>fourth_number):    
            print(f"{first_number} : is greatest number ...!!")
elif(second_number>first_number):
    if(second_number>third_number):
        if(second_number>fourth_number):
            print(f"{second_number} : is the greates number")
elif(third_number>first_number):
    if(third_number>second_number):
        if(third_number>fourth_number):
            print(f"{fourth_number} : if the greatest number")
else:
    print(f"{fourth_number} : is the greatest number")            
  

