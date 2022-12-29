string = input("Enter a String: ")
word = string.split(" ")
res = ""

if word[0] != "Is":
    print(f"Is {string}")
else:
    print(string)