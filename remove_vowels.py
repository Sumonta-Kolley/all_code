def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in text:
        if ch not in vowels:
            result = result + ch
    return result

text = input("Enter text: ")
print("Without vowels:", remove_vowels(text))