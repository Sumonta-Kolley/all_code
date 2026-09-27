def count_consonants(text):
    count = 0
    vowels = "aeiouAEIOU"
    for ch in text:
        if ch.isalpha() and ch not in vowels:
            count = count + 1
    return count

text = input("Enter text: ")
print("Consonants:", count_consonants(text))