"""
Kaprekar's Routine
Given a 4-digit number, return the number of times you need to apply Kaprekar's routine until reaching 6174.

Kaprekar's routine works as follows:

Arrange the digits in descending order to form the largest number
Arrange the digits in ascending order to form the smallest number (pad with leading zeros if necessary)
Subtract the smaller from the larger
Repeat with the new number
"""
def kaprekar(n):
    count = 0
    largest = ''.join(sorted(str(n), reverse=True))
    smallest = ''.join(sorted(str(n)))
    difference = int(largest) - int(smallest)
    while difference != 6174:
        largest = ''.join(sorted(str(difference), reverse=True))
        smallest = ''.join(sorted(str(difference)))
        difference = int(largest) - int(smallest)
        count += 1
    return count + 1

print(kaprekar(1234))
print(kaprekar(2025))
print(kaprekar(7173))
print(kaprekar(3164))
print(kaprekar(8082))