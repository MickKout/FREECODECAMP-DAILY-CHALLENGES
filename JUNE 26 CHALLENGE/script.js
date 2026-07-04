// Blood Bank
// Given an array of the inventory at a blood bank and an array of patient blood type requests, return a string in the format "X of Y patients served". Where X is the maximum number of patients that can receive blood from the bank's inventory, and Y is the total number of patients.

// Each entry in both arrays is one of the following blood types: "AB", "A", "B", or "O".

// Compatibility rules:

// "AB" can receive from any blood type.
// "A" can receive from "A" and "O".
// "B" can receive from "B" and "O".
// "O" can only receive from "O".
// Duplicate entries in the given arrays represent quantity.

// Tests:
// Waiting:1. triageBlood(["O", "A", "B", "AB"], ["O", "A", "B", "AB"]) should return "4 of 4 patients served".
// Waiting:2. triageBlood(["A", "A", "B", "B", "AB"], ["O", "A", "B", "B", "B"]) should return "3 of 5 patients served".
// Waiting:3. triageBlood(["O", "A", "B", "AB"], ["AB", "AB", "AB", "AB", "AB"]) should return "4 of 5 patients served".
// Waiting:4. triageBlood(["O", "O", "O", "O", "O"], ["O", "A", "B", "AB"]) should return "4 of 4 patients served".
// Waiting:5. triageBlood(["A", "O", "B", "AB", "B", "AB", "O", "A", "A"], ["O", "A", "B", "AB", "A", "B", "A", "A", "B", "A", "B"]) should return "8 of 11 patients served".
// Waiting:6. triageBlood(["O", "B", "AB", "AB", "O", "A", "A", "AB", "O", "B", "B", "AB", "A", "B", "AB"], ["O", "A", "B", "B", "A", "B", "AB", "A", "B", "A", "O", "AB", "AB", "O"]) should return "13 of 14 patients served".

function triageBlood(bank, patients) {
  const compatible = {
    "O":  ["O", "A", "B", "AB"],
    "A":  ["A", "AB"],
    "B":  ["B", "AB"],
    "AB": ["AB"]
  };

  // Sort bank: specific donors first (AB, A, B), universal donor O last
  const order = { "AB": 0, "A": 1, "B": 2, "O": 3 };
  const sortedBank = [...bank].sort((a, b) => order[a] - order[b]);
  const remainingPatients = [...patients];

  let count = 0;

  for (let i = 0; i < sortedBank.length; i++) {
    const donor = sortedBank[i];
    const canDonateTo = compatible[donor];

    for (let j = 0; j < remainingPatients.length; j++) {
      if (canDonateTo.includes(remainingPatients[j])) {
        count++;
        remainingPatients.splice(j, 1);
        break;
      }
    }
  }

  return `${count} of ${patients.length} patients served`;
}

console.log(triageBlood(["O", "A", "B", "AB"], ["O", "A", "B", "AB"]));
console.log(triageBlood(["A", "A", "B", "B", "AB"], ["O", "A", "B", "B", "B"]));
console.log(triageBlood(["O", "A", "B", "AB"], ["AB", "AB", "AB", "AB", "AB"]));
console.log(triageBlood(["O", "O", "O", "O", "O"], ["O", "A", "B", "AB"]));
console.log(triageBlood(["A", "O", "B", "AB", "B", "AB", "O", "A", "A"], ["O", "A", "B", "AB", "A", "B", "A", "A", "B", "A", "B"]));
console.log(triageBlood(["O", "B", "AB", "AB", "O", "A", "A", "AB", "O", "B", "B", "AB", "A", "B", "AB"], ["O", "A", "B", "B", "A", "B", "AB", "A", "B", "A", "O", "AB", "AB", "O"]));
