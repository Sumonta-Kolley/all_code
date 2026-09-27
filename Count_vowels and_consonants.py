def count_vowels_consonants(text):
    vowels_count = 0
    consonants_count = 0
    vowels = "aeiouAEIOU"
    for ch in text:
        if ch.isalpha():
            if ch in vowels:
                vowels_count = vowels_count + 1
            else:
                consonants_count = consonants_count + 1
    print("Vowels:", vowels_count)
    print("Consonants:", consonants_count)

text = input("Enter text: ")
count_vowels_consonants(text)