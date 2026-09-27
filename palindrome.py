def check_palindrome(text):
    rev = ""
    for ch in text:
        rev = ch + rev
    if text == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")

text = input("Enter a string: ")
check_palindrome(text)