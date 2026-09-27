def count_words(text):
    s = text.strip()
    if s == "":
        return 0
    words = 1
    for i in range(len(s)):
        if s[i] == " " and s[i - 1] != " ":
            words = words + 1
    return words

text = input("Enter a sentence: ")
print("Total words:", count_words(text))