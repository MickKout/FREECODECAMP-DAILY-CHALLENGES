// Duplicate Character Count
// Given two strings, return a count of characters from the second string that can be found in the first.

// Duplicate characters in the second string are counted separately.
// Tests:
// Waiting:1. duplicate_character_count("aloha", "hei") should return 1.
// Waiting:2. duplicate_character_count("jambo", "bonjour") should return 4.
// Waiting:3. duplicate_character_count("hello", "hola") should return 3.
// Waiting:4. duplicate_character_count("ola", "hej") should return 0.
// Waiting:5. duplicate_character_count("ciao", "konnichiwa") should return 5.
// Waiting:6. duplicate_character_count("merhaba", "xin chao") should return 2.
// Waiting:7. duplicate_character_count("hello world", "hello to everyone around the world") should return 26.

function duplicateCharacterCount(str1, str2) {

  let count = 0;
  for (let i = 0; i < str1.length; i++) {
    for (let j = 0; j < str2.length; j++) {
      if (str2[j] === str1[i] && str1.indexOf(str2[j]) === i) {
        count++;
      }
    
    }
  }
  return count;
}
  
console.log(duplicateCharacterCount("aloha", "hei"));
console.log(duplicateCharacterCount("jambo", "bonjour"));
console.log(duplicateCharacterCount("hello", "hola"));
console.log(duplicateCharacterCount("ola", "hej"));
console.log(duplicateCharacterCount("ciao", "konnichiwa"));
console.log(duplicateCharacterCount("merhaba", "xin chao"));
console.log(duplicateCharacterCount("hello world", "hello to everyone around the world"));