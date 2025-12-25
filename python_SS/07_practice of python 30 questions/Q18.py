user = input("enter you character :- ")
vowel = 0
consonant = 0

for i in user:
    # print(i)
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U" :
        vowel += 1
        print(f"total of vowel char:-{i}")
    else:
        print(f"total of consonant char:-{i}")
        consonant += 1
print(f"total of vowel number: {vowel}")
print(f"total of consonant number: {consonant}")