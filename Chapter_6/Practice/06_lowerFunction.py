statement = "My name is Muhammad Jamshaid"
word = input("Enter the word you want to find : ")
if(word.lower() in statement.lower()) :
    print(f"{word} is present in the statement..")

else:
    print(f"{word} is not present in the statement...")