# Given a string, return only the words that are entirely lowercase, in their original order and with a space between each word.

def get_lowercase_words(s):
 result = []
 for word in s.split():
     if word.islower():
         result.append(word)
 s = ' '.join(result)
 return s

print(get_lowercase_words("hello GOOD world")) # hello GOOD world
