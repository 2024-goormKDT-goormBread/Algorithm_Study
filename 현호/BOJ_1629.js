const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const solve = () => {
  const [a, b, c] = input[0].split(" ").map(BigInt);

  console.log(parseInt(customMod(a, b, c)));
};

const customMod = (a, b, c) => {
  if (b === 1n) {
    return a % c;
  }

  const temp = customMod(a, b / 2n, c);

  if (b % 2n) {
    return ((temp * temp * a) % c) % c;
  }

  return (temp * temp) % c;
};

solve();
