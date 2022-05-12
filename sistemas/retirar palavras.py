word_without_vowels = ""

user_word = input("digite a palavra:" )# Prompt the user to enter a word
user_word = user_word.upper()# and assign it to the user_word variable.


for letter in user_word:
    if letter == "A":# Complete the body of the loop.
        continue
    if letter == "E":
        continue
    if letter == "I":# Complete the body of the loop.
        continue
    if letter == "O":# Complete the body of the loop.
        continue
    if letter == "U":# Complete the body of the loop.
        continue
 
    word_without_vowels = word_without_vowels + letter

print(word_without_vowels)# Print the word assigned to word_without_vowels.
