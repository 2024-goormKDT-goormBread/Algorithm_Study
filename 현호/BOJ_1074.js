const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, r, c] = input[0].split(" ").map(Number);

const solve = (n, r, c) => {
  if (n === 0) {
    return 0;
  }

  const half = 1 << (n - 1);

  if (r < half && c < half) {
    return solve(n - 1, r, c);
  } else if (r < half && c >= half) {
    return half * half + solve(n - 1, r, c - half);
  } else if (r >= half && c < half) {
    return 2 * half * half + solve(n - 1, r - half, c);
  } else {
    return 3 * half * half + solve(n - 1, r - half, c - half);
  }
};

console.log(solve(n, r, c));
