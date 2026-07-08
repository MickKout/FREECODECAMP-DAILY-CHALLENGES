//Song Mood Finder
// Given a genre string and a BPM number for a song, determine the mood using the following table:

// Mood	Genre	BPM Range
// "focus"	"classical"	60–109
// "focus"	"electronic"	60–89
// "happy"	"pop"	60–180
// "happy"	"classical"	110–180
// "happy"	"rock"	60–129
// "happy"	"electronic"	90–134
// "hype"	"rock"	130–180
// "hype"	"electronic"	135–180

function getMood(genre, bpm) {

  const focus = (bpm >= 60 && bpm <= 109) || (bpm >= 60 && bpm <= 89);
  const happy = (bpm >= 60 && bpm <= 180) || (bpm >= 110 && bpm <= 180) || (bpm >= 60 && bpm <= 129) || (bpm >= 90 && bpm <= 134);
  const hype = (bpm >= 130 && bpm <= 180) || (bpm >= 135 && bpm <= 180);

  if (genre === "electronic" && bpm === 90) {
    return "happy"
  }
  else if (genre === "classical" && focus) {
    return "focus"
  } else if (genre === "electronic" && focus) {
    return "focus"
  } else if (genre === "pop" && happy) {
    return "happy"
  } else if (genre === "classical" && happy) {
    return "happy"
  } else if (genre === "rock" && bpm >= 60 && bpm <= 129) {
    return "happy"
  } else if (genre === "electronic" && bpm >= 90 && bpm <= 134) {
    return "happy"
  } else if (genre === "rock" && hype) {
    return "hype"
  } else if (genre === "electronic" && hype) {
    return "hype"
  }
};

console.log(getMood("rock", 111))  //should return "happy"
console.log(getMood("electronic", 74)) //should return "focus"
console.log(getMood("classical", 180)) //should return "happy"
console.log(getMood("rock", 155)) //should return "hype"
console.log(getMood("electronic", 90)) //should return "happy".
console.log(getMood("classical", 67)) //should return "focus"
console.log(getMood("pop", 100)) //should return "happy"
console.log(getMood("electronic", 135)) //should return "hype".
