const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const size = Number(input.shift());
const numbers = input[0].split(" ").map(Number);

const solve = () => {
  const dp = Array.from({ length: size }, () => 1);

  for (let i = 1; i < size; i += 1) {
    for (let j = 0; j < i; j += 1) {
      if (numbers[j] < numbers[i]) {
        dp[i] = Math.max(dp[j] + 1, dp[i]);
      }
    }
  }

  console.log(Math.max(...dp));
};

solve();
