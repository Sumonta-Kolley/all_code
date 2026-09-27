def remove_spaces(text):
    result = ""
    for ch in text:
        if ch != " ":
            result = result + ch
    return result

text = input("Enter text: ")
print("Result:", remove_spaces(text))