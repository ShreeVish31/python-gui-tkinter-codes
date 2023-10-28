def is_pangram(sentence):
   
    unique_letters = set()

   
    for char in sentence:
       
        char = char.lower()
        
        
        if 'a' <= char <= 'z':
            unique_letters.add(char)
    
   
    return len(unique_letters) == 26
sentence = "The quick brown fox jumps over the lazy dog"
result = is_pangram(sentence)
if result:
    print("It's a pangram!")
else:
    print("It's not a pangram.")
