// Exact Change
// Given an integer amount in cents, return the number of distinct ways to make exact change using pennies (1 cent), nickels (5 cents), dimes (10 cents), and quarters (25 cents).

function exactChange(amount) {

  const coins = [1, 5, 10, 25];
  const ways = new Array(amount + 1).fill(0);
  ways[0] = 1;

  for (const coin of coins) {
    for (let i = coin; i <= amount; i++) {
      ways[i] += ways[i - coin];
    }
  }

  return ways[amount];
}

console.log(exactChange(3));
console.log(exactChange(99));