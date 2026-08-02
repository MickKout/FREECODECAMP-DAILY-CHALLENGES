""" "
Nearest Multiple
Given two integers, round the first to the nearest multiple of the second.

Tests:
Waiting:1. round_to_nearest_multiple(5, 3) should return 6.
Waiting:2. round_to_nearest_multiple(17, 4) should return 16.
Waiting:3. round_to_nearest_multiple(43, 5) should return 45.
Waiting:4. round_to_nearest_multiple(38, 11) should return 33.
Waiting:5. round_to_nearest_multiple(93, 12) should return 96.
"""

import math

def round_to_nearest_multiple(num, multiple):

    remainder = num % multiple

    if remainder < multiple / 2:
        return num - remainder
    else:
        return num + multiple - remainder
