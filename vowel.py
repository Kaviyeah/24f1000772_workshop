ch = input("Enter a character: ").lower()

vowels = {'a', 'e', 'i', 'o', 'u'}

if ch in vowels:
    print(ch, "is a vowel")
else:
    print(ch, "is a consonant")
