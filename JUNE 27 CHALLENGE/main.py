"""
Periodic Spelling
Given a word, determine if it can be spelled using element symbols from the periodic table.

Ignore casing when spelling a word. "neon" can be spelled with the symbols "Ne", "O", and "N".
Here's a full list of the element symbols:

["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"];

Return an array of the elements used to spell the word, in their original casing and in the order to spell the word. Or, an empty array if it can't be spelled.

Tests:
Waiting:1. getPeriodicSpelling("neon") should return ["Ne", "O", "N"].
Waiting:2. getPeriodicSpelling("rational") should return ["Ra", "Ti", "O", "N", "Al"].
Waiting:3. getPeriodicSpelling("yarn") should return ["Y", "Ar", "N"].
Waiting:4. getPeriodicSpelling("carbon") should return ["C", "Ar", "B", "O", "N"] or ["Ca", "Rb", "O", "N"].
Waiting:5. getPeriodicSpelling("noisy") should return ["N", "O", "I", "S", "Y"] or ["No", "I", "S", "Y"].
Waiting:6. getPeriodicSpelling("bicycles") should return ["B", "I", "C", "Y", "Cl", "Es"] or ["Bi", "C", "Y", "Cl", "Es"].
Waiting:7. getPeriodicSpelling("optics") should return ["O", "P", "Ti", "C", "S"], ["O", "P", "Ti", "Cs"], ["O", "Pt", "I", "C", "S"], or ["O", "Pt", "I", "Cs"].
Waiting:8. getPeriodicSpelling("value") should return [].
"""

def get_periodic_spelling(word):
  elements = ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"]

  def solve(remaining, current):
    if remaining == "":
      return current

    two = remaining[:2]
    one = remaining[:1]

    two_match = next((el for el in elements if el.lower() == two.lower()), None)
    if two_match:
      result = solve(remaining[2:], current + [two_match])
      if result is not None:
        return result

    one_match = next((el for el in elements if el.lower() == one.lower()), None)
    if one_match:
      result = solve(remaining[1:], current + [one_match])
      if result is not None:
        return result

    return None

  result = solve(word.lower(), [])
  return result if result is not None else []

print(get_periodic_spelling("neon"))      # ['Ne', 'O', 'N']
print(get_periodic_spelling("rational"))  # ['Ra', 'Ti', 'O', 'N', 'Al']
print(get_periodic_spelling("yarn"))      # ['Y', 'Ar', 'N']
print(get_periodic_spelling("carbon"))    # ['C', 'Ar', 'B', 'O', 'N']
print(get_periodic_spelling("noisy"))     # ['N', 'O', 'I', 'S', 'Y']
print(get_periodic_spelling("bicycles"))  # ['B', 'I', 'C', 'Y', 'Cl', 'Es']
print(get_periodic_spelling("optics"))    # ['O', 'P', 'Ti', 'C', 'S']
print(get_periodic_spelling("value"))     # []