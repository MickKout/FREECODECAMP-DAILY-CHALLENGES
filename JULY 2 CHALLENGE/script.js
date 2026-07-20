// Max Profit
// Given an array of daily stock prices and a budget (in dollars), calculate the maximum profit you could make by buying and selling the stock over the given period.

// You may only sell after you buy.
// You may perform at most one buy and one sell transaction. Once you sell, you cannot buy again.
// You can only buy whole shares.
// Return the maximum possible profit as a string, rounded down to the nearest cent and formatted to two decimal places.

function getMaxProfit(prices, budget) {
  if (prices.length < 2) return "0.00";

  let maxProfit = 0;

  for (let i = 0; i < prices.length; i++) {
    for (let j = i + 1; j < prices.length; j++) {
      if (prices[j] > prices[i]) {
        const shares = Math.floor(budget / prices[i]);
        const profit = shares * (prices[j] - prices[i]);
        if (profit > maxProfit) {
          maxProfit = profit;
        }
      }
    }
  }

  return (Math.floor(maxProfit * 100) / 100).toFixed(2);
}

console.log(getMaxProfit([5, 6], 50));                                                        // "10.00"
console.log(getMaxProfit([8, 2, 5, 10], 20));                                                 // "80.00"
console.log(getMaxProfit([4, 5, 3, 6], 20));                                                  // "18.00"
console.log(getMaxProfit([54.40, 51.22, 53.99, 50.28, 53.01, 52.84], 200));                  // "8.31"
console.log(getMaxProfit([15.38, 15.01, 14.99, 14.62, 14.28], 80));                          // "0.00"
console.log(getMaxProfit([121.45, 126.82, 122.91, 124.65, 128.83, 128.83, 127.33], 1230.25)); // "73.80"