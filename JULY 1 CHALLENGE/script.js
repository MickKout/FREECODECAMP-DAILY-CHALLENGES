// Lucky Number
// Given a string of a person's first and last name, calculate their lucky number using the following rules:

// First and last names are separated by a space
// Find the vowel and consonant count for each name
// Multiply the smaller vowel and consonant counts by each other and then by the length of the smaller name
// Do the same for the two larger counts and the larger name
// Subtract the smaller value from the larger one to get their lucky number
// If the final value is zero (0), return 13.

function getLuckyNumber(name) {

    if (!name) {
        return "Please enter a valid name.";
    }

    const nameParts = name.split(" ");
    const firstName = nameParts[0];
    const lastName = nameParts[1];

    const firstVowels = firstName.match(/[aeiou]/gi);
    const firstConsonants = firstName.match(/[bcdfghjklmnpqrstvwxyz]/gi);
    const lastVowels = lastName.match(/[aeiou]/gi);
    const lastConsonants = lastName.match(/[bcdfghjklmnpqrstvwxyz]/gi);

    const firstVowelCount = firstVowels ? firstVowels.length : 0;
    const firstConsonantCount = firstConsonants ? firstConsonants.length : 0;
    const lastVowelCount = lastVowels ? lastVowels.length : 0;
    const lastConsonantCount = lastConsonants ? lastConsonants.length : 0;

    const smallerVowelCount = Math.min(firstVowelCount, lastVowelCount);
    const smallerConsonantCount = Math.min(firstConsonantCount, lastConsonantCount);
    const largerVowelCount = Math.max(firstVowelCount, lastVowelCount);
    const largerConsonantCount = Math.max(firstConsonantCount, lastConsonantCount);
    const smallerNameLength = Math.min(firstName.length, lastName.length);
    const largerNameLength = Math.max(firstName.length, lastName.length);

    const firstResult = smallerVowelCount * smallerConsonantCount * smallerNameLength;
    const secondResult = largerVowelCount * largerConsonantCount * largerNameLength;

    const luckyNumber = Math.abs(firstResult - secondResult);
    return luckyNumber === 0 ? 13 : luckyNumber;

}
console.log(getLuckyNumber("John Doe"));
console.log(getLuckyNumber("Olivia Lewis"));
console.log(getLuckyNumber("James Wilson"));
console.log(getLuckyNumber("Elizabeth Hernandez"));
console.log(getLuckyNumber("Mike Walker"));
console.log(getLuckyNumber("Chloe Perez"));
