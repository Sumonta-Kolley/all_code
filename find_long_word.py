def find_longest_word(text):
    longest = ""
    current_word = ""
    for ch in text + " ":
        if ch != " ":
            current_word = current_word + ch
        else:
            if len(current_word) > len(longest):
                longest = current_word
            current_word = ""
    return longest

text = input("Enter a sentence: ")
print("Longest word is:", find_longest_word(text))