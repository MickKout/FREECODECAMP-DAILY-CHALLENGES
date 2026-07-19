""""
Lucky Number
Given a string of a person's first and last name, calculate their lucky number using the following rules:

First and last names are separated by a space
Find the vowel and consonant count for each name
Multiply the smaller vowel and consonant counts by each other and then by the length of the smaller name
Do the same for the two larger counts and the larger name
Subtract the smaller value from the larger one to get their lucky number
If the final value is zero (0), return 13.
"""

import re

def get_lucky_number(name):

    if not name:
        return "Please enter a valid name."

    name_parts = name.split(" ")
    first_name = name_parts[0]
    last_name  = name_parts[1]

    first_vowel_count     = len(re.findall(r'[aeiou]', first_name, re.IGNORECASE))
    first_consonant_count = len(re.findall(r'[bcdfghjklmnpqrstvwxyz]', first_name, re.IGNORECASE))
    last_vowel_count      = len(re.findall(r'[aeiou]', last_name, re.IGNORECASE))
    last_consonant_count  = len(re.findall(r'[bcdfghjklmnpqrstvwxyz]', last_name, re.IGNORECASE))

    smaller_vowel_count     = min(first_vowel_count,     last_vowel_count)
    smaller_consonant_count = min(first_consonant_count, last_consonant_count)
    larger_vowel_count      = max(first_vowel_count,     last_vowel_count)
    larger_consonant_count  = max(first_consonant_count, last_consonant_count)
    smaller_name_length     = min(len(first_name),       len(last_name))
    larger_name_length      = max(len(first_name),       len(last_name))

    first_result  = smaller_vowel_count * smaller_consonant_count * smaller_name_length
    second_result = larger_vowel_count  * larger_consonant_count  * larger_name_length

    lucky_number = abs(first_result - second_result)
    return 13 if lucky_number == 0 else lucky_number

print(get_lucky_number("John Doe"))
print(get_lucky_number("Olivia Lewis"))
print(get_lucky_number("James Wilson"))
print(get_lucky_number("Elizabeth Hernandez"))
print(get_lucky_number("Mike Walker"))
print(get_lucky_number("Chloe Perez"))
