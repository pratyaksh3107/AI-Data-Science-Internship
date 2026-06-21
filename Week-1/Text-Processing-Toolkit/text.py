print("----- Text Processing Toolkit -----")

text = input("\nEnter Text:\n")

characters = len(text)
words = len(text.split())

vowels = "aeiouAEIOU"
vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1

uppercase_text = text.upper()
lowercase_text = text.lower()
title_text = text.title()
reversed_text = text[::-1]

print("\nCharacters:", characters)
print("Words:", words)
print("Vowels:", vowel_count)

print("\nUppercase:")
print(uppercase_text)

print("\nLowercase:")
print(lowercase_text)

print("\nTitle Case:")
print(title_text)

print("\nReversed Text:")
print(reversed_text)
