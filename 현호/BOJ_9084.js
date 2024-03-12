const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const testCase = Number(input.shift());

const solve = () => {
  const answer = [];

  for (let i = 0; i < testCase; i++) {
    const n = Number(input.shift());
    const values = input.shift().split(" ").map(Number);
    const m = Number(input.shift());
    const dp = Array.from({ length: m + 1 }, () => 0);

    dp[0] = 1;

    for (let i = 0; i < n; i += 1) {
      for (let j = 0; j <= m; j += 1) {
        if (j >= values[i]) {
          dp[j] += dp[j - values[i]];
        }
      }
    }

    answer.push(dp[m]);
  }

  console.log(answer.join("\n"));
};

solve();
