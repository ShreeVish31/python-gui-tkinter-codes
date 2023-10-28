def is_vowel(character):
    
    character = character.lower()
    

    return character in ('a', 'e', 'i', 'o', 'u')


user_character = input("Enter a character: ")


if len(user_character) != 1:
    print("Please enter a single character.")
else:
    
    if is_vowel(user_character):
        print(f"{user_character} is a vowel.")
    else:
        print(f"{user_character} is not a vowel.")
