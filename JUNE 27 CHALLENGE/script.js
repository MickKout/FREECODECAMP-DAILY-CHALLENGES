// Periodic Spelling
// Given a word, determine if it can be spelled using element symbols from the periodic table.

// Ignore casing when spelling a word. "neon" can be spelled with the symbols "Ne", "O", and "N".
// Here's a full list of the element symbols:

// ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"];
// Return an array of the elements used to spell the word, in their original casing and in the order to spell the word. Or, an empty array if it can't be spelled.

// Tests:
// Waiting:1. getPeriodicSpelling("neon") should return ["Ne", "O", "N"].
// Waiting:2. getPeriodicSpelling("rational") should return ["Ra", "Ti", "O", "N", "Al"].
// Waiting:3. getPeriodicSpelling("yarn") should return ["Y", "Ar", "N"].
// Waiting:4. getPeriodicSpelling("carbon") should return ["C", "Ar", "B", "O", "N"] or ["Ca", "Rb", "O", "N"].
// Waiting:5. getPeriodicSpelling("noisy") should return ["N", "O", "I", "S", "Y"] or ["No", "I", "S", "Y"].
// Waiting:6. getPeriodicSpelling("bicycles") should return ["B", "I", "C", "Y", "Cl", "Es"] or ["Bi", "C", "Y", "Cl", "Es"].
// Waiting:7. getPeriodicSpelling("optics") should return ["O", "P", "Ti", "C", "S"], ["O", "P", "Ti", "Cs"], ["O", "Pt", "I", "C", "S"], or ["O", "Pt", "I", "Cs"].
// Waiting:8. getPeriodicSpelling("value") should return [].

function getPeriodicSpelling(word) {
  
  const elements = [
    "H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"
  ];

  function solve(remaining, current) {
    // Base case: whole word consumed successfully
    if (remaining === '') return current;

    const two = remaining.slice(0, 2);
    const one = remaining.slice(0, 1);

    // Try two-letter match first
    const twoMatch = elements.find(el => el.toLowerCase() === two.toLowerCase());
    if (twoMatch) {
      const result = solve(remaining.slice(2), [...current, twoMatch]);
      if (result !== null) return result; // this path worked, return it
    }

    // Try one-letter match (either as fallback or if two failed)
    const oneMatch = elements.find(el => el.toLowerCase() === one.toLowerCase());
    if (oneMatch) {
      const result = solve(remaining.slice(1), [...current, oneMatch]);
      if (result !== null) return result;
    }

    // Neither worked — this path is a dead end, backtrack
    return null;
  }

  return solve(word.toLowerCase(), []) ?? [];
}

console.log(getPeriodicSpelling("neon"));     // ["Ne", "O", "N"]
console.log(getPeriodicSpelling("rational")); // ["Ra", "Ti", "O", "N", "Al"]
console.log(getPeriodicSpelling("yarn"));     // ["Y", "Ar", "N"]
console.log(getPeriodicSpelling("carbon"));   // ["C", "Ar", "B", "O", "N"]
console.log(getPeriodicSpelling("noisy"));    // ["N", "O", "I", "S", "Y"]
console.log(getPeriodicSpelling("bicycles")); // ["B", "I", "C", "Y", "Cl", "Es"]
console.log(getPeriodicSpelling("optics"));   // ["O", "P", "Ti", "C", "S"]
console.log(getPeriodicSpelling("value"));    // []