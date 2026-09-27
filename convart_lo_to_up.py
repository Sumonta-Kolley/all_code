def convert_uppercase(text):
    result = ""
    for ch in text:
        if 'a' <= ch <= 'z':
            result = result + chr(ord(ch) - 32)
        else:
            result = result + ch
    return result

text = input("Enter text: ")
print("Using upper():", text.upper())
print("Using loop:", convert_uppercase(text))