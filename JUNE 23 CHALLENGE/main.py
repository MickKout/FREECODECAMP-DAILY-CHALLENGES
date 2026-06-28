# BMI Calculator
# Given a weight in pounds and a height in inches, return the BMI (Body Mass Index) rounded to one decimal place.

# To get BMI: divide the weight by the height squared, then multiply the result by 703.

# Tests:
# Waiting:1. calculate_bmi(180, 70) should return 25.8.
# Waiting:2. calculate_bmi(140, 64) should return 24.0.
# Waiting:3. calculate_bmi(160, 76) should return 19.5.
# Waiting:4. calculate_bmi(200, 60) should return 39.1.
# Waiting:5. calculate_bmi(150, 68) should return 22.8.


def calculate_bmi(weight, height):

    bmi = round((weight / (height * height) * 703), 1)
    return bmi

print(calculate_bmi(180, 70))
print(calculate_bmi(140, 64))
print(calculate_bmi(160, 76))
print(calculate_bmi(200, 60))
print(calculate_bmi(150, 68))
