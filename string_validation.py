# String Validation Program

user_input = input("Enter a string: ")

digits = 0
special = 0

for ch in user_input:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        pass
    else:
        special += 1

print("Digits:", digits)
print("Special characters:", special)
