// Given a string, return only the words that are entirely lowercase, in their original order and with a space between each word.

// Tests:
// Passed:1. getLowercaseWords("hello GOOD world") should return "hello world".
// Passed:2. getLowercaseWords("these are all lowercase") should return "these are all lowercase".
// Passed:3. getLowercaseWords("less is NoT more") should return "less is more".
// Passed:4. getLowercaseWords("DonT eat pizza every OTHER day") should return "eat pizza every day".
// Passed:5. getLowercaseWords("the Super quick AND snEaky brown fox Leapt anD jumped over aNd AROUND the lazy SloW dog") should return "the quick brown fox jumped over the lazy dog".

function getLowercaseWords(str) {
 const result = [];
  const words = str.split(' ');
  for (let i = 0; i < words.length; i++) {
    if (words[i].toLowerCase() === words[i]) {
      result.push(words[i]);
    }
  }
  str = result.join(' ');
  return str;
}