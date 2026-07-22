// Kaprekar's Routine
// Given a 4-digit number, return the number of times you need to apply Kaprekar's routine until reaching 6174.

// Kaprekar's routine works as follows:

// Arrange the digits in descending order to form the largest number
// Arrange the digits in ascending order to form the smallest number (pad with leading zeros if necessary)
// Subtract the smaller from the larger
// Repeat with the new number
// Tests:
// Waiting:1. kaprekar(1234) should return 3.
// Waiting:2. kaprekar(2025) should return 6.
// Waiting:3. kaprekar(7173) should return 4.
// Waiting:4. kaprekar(3164) should return 7.
// Waiting:5. kaprekar(8082) should return 2.

function kaprekar(n) {

  let count = 0;
  let largest = n.toString().split("").sort().reverse().join("");
  let smallest = n.toString().split("").sort().join("");
  let difference = largest - smallest;
  while (difference !== 6174) {
    largest = difference.toString().split("").sort().reverse().join("");
    smallest = difference.toString().split("").sort().join("");
    difference = largest - smallest;
    count++;
  }
  return count + 1;
}

console.log(kaprekar(1234));
console.log(kaprekar(2025));
console.log(kaprekar(7173));
console.log(kaprekar(3164));
console.log(kaprekar(8082));