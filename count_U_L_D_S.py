def count_case(text):
    upper = 0
    lower = 0
    digits = 0
    spaces = 0
    for ch in text:
        if ch.isupper():
            upper = upper + 1
        elif ch.islower():
            lower = lower + 1
        elif ch.isdigit():
            digits = digits + 1
        elif ch == " ":
            spaces = spaces + 1
    print("Uppercase:", upper)
    print("Lowercase:", lower)
    print("Digits:", digits)
    print("Spaces:", spaces)

text = input("Enter text: ")
count_case(text)
