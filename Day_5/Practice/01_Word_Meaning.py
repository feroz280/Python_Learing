# Write a program to create a dictionary of word meanings.Provide user with an option to look it up.

word__meaning = {

    "Timid" : "Darpook",
    "Brave" : "Bahadur",
    "Crazy" : "Dewana"
}
meaning = input("Enter word to find meaning :")

print(word__meaning.get(meaning))