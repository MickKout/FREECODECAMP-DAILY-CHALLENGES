"""
Blood Bank
Given an array of the inventory at a blood bank and an array of patient blood type requests, return a string in the format "X of Y patients served". Where X is the maximum number of patients that can receive blood from the bank's inventory, and Y is the total number of patients.

Each entry in both arrays is one of the following blood types: "AB", "A", "B", or "O".

Compatibility rules:

"AB" can receive from any blood type.
"A" can receive from "A" and "O".
"B" can receive from "B" and "O".
"O" can only receive from "O".
Duplicate entries in the given arrays represent quantity.

Tests:
Passed:1. triage_blood(["O", "A", "B", "AB"], ["O", "A", "B", "AB"]) should return "4 of 4 patients served".
Passed:2. triage_blood(["A", "A", "B", "B", "AB"], ["O", "A", "B", "B", "B"]) should return "3 of 5 patients served".
Passed:3. triage_blood(["O", "A", "B", "AB"], ["AB", "AB", "AB", "AB", "AB"]) should return "4 of 5 patients served".
Passed:4. triage_blood(["O", "O", "O", "O", "O"], ["O", "A", "B", "AB"]) should return "4 of 4 patients served".
Passed:5. triage_blood(["A", "O", "B", "AB", "B", "AB", "O", "A", "A"], ["O", "A", "B", "AB", "A", "B", "A", "A", "B", "A", "B"]) should return "8 of 11 patients served".
Passed:6. triage_blood(["O", "B", "AB", "AB", "O", "A", "A", "AB", "O", "B", "B", "AB", "A", "B", "AB"], ["O", "A", "B", "B", "A", "B", "AB", "A", "B", "A", "O", "AB", "AB", "O"]) should return "13 of 14 patients served".
"""

def triage_blood(bank, patients):

 compatible = {
    "O":  ["O", "A", "B", "AB"],
    "A":  ["A", "AB"],
    "B":  ["B", "AB"],
    "AB": ["AB"]
}

 # Sort bank: specific donors first (AB, A, B), universal donor O last
 order = { "AB": 0, "A": 1, "B": 2, "O": 3 }
 sorted_bank = sorted(bank, key=lambda x: order[x])
 remaining_patients = list(patients)

 count = 0

 for i in range(len(sorted_bank)):
    donor = sorted_bank[i]
    can_donate_to = compatible[donor]

    for j in range(len(remaining_patients)):
        if remaining_patients[j] in can_donate_to:
            count += 1
            remaining_patients.pop(j)
            break

 return f"{count} of {len(patients)} patients served"

print(triage_blood(["O", "A", "B", "AB"], ["O", "A", "B", "AB"]));
print(triage_blood(["A", "A", "B", "B", "AB"], ["O", "A", "B", "B", "B"]));
print(triage_blood(["O", "A", "B", "AB"], ["AB", "AB", "AB", "AB", "AB"]));
print(triage_blood(["O", "O", "O", "O", "O"], ["O", "A", "B", "AB"]));
print(triage_blood(["A", "O", "B", "AB", "B", "AB", "O", "A", "A"], ["O", "A", "B", "AB", "A", "B", "A", "A", "B", "A", "B"]));
print(triage_blood(["O", "B", "AB", "AB", "O", "A", "A", "AB", "O", "B", "B", "AB", "A", "B", "AB"], ["O", "A", "B", "B", "A", "B", "AB", "A", "B", "A", "O", "AB", "AB", "O"]));
