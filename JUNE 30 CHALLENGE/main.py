"""
Duplicate Character Count
Given two strings, return a count of characters from the second string that can be found in the first.

Duplicate characters in the second string are counted separately.
Tests:
Waiting:1. duplicate_character_count("aloha", "hei") should return 1.
Waiting:2. duplicate_character_count("jambo", "bonjour") should return 4.
Waiting:3. duplicate_character_count("hello", "hola") should return 3.
Waiting:4. duplicate_character_count("ola", "hej") should return 0.
Waiting:5. duplicate_character_count("ciao", "konnichiwa") should return 5.
Waiting:6. duplicate_character_count("merhaba", "xin chao") should return 2.
Waiting:7. duplicate_character_count("hello world", "hello to everyone around the world") should return 26.
"""
def duplicate_character_count(str1, str2):

    count = 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str2[j] == str1[i] and str1.index(str2[j]) == i:
                count += 1

    return count

print(duplicate_character_count("aloha", "hei"))
print(duplicate_character_count("jambo", "bonjour"))
print(duplicate_character_count("hello", "hola"))
print(duplicate_character_count("ola", "hej"))
print(duplicate_character_count("ciao", "konnichiwa"))
print(duplicate_character_count("merhaba", "xin chao"))
print(duplicate_character_count("hello world", "hello to everyone around the world"))