def character_frequency(text, ch):
    count = 0
    for letter in text:
        if letter == ch:
            count = count + 1
    return count

text = input("Enter text: ")
ch = input("Enter character to search: ")
print("Frequency:", character_frequency(text, ch))