const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const testCase = Number(input.shift());
const numbers = input.map(Number);

const solve = () => {
  const dp = Array.from({ length: 41 }, () =>
    Array.from({ length: 2 }, () => -1)
  );
  const answer = [];

  [dp[0][0], dp[0][1]] = [1, 0];
  [dp[1][0], dp[1][1]] = [0, 1];

  for (let i = 0; i < testCase; i += 1) {
    fibonacci(numbers[i], dp);
    answer.push(dp[numbers[i]].join(" "));
  }

  console.log(answer.join("\n"));
};

// 피보나치는 f(n) = f(n - 1) + f(n - 2)
const fibonacci = (n, dp) => {
  if (dp[n][0] === -1) {
    const fibonacci_a =
      dp[n - 1][0] !== -1 ? [dp[n - 1][0], dp[n - 1][1]] : fibonacci(n - 1, dp);
    const fibonacci_b =
      dp[n - 2][0] !== -1 ? [dp[n - 2][0], dp[n - 2][1]] : fibonacci(n - 2, dp);

    [dp[n][0], dp[n][1]] = [
      fibonacci_a[0] + fibonacci_b[0],
      fibonacci_a[1] + fibonacci_b[1],
    ];
  }

  return [dp[n][0], dp[n][1]];
};

solve();
