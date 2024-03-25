const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +input[0];
const answer = [];

const solve = () => {
  console.log(2 ** n - 1);
  recursive(1, 3, n);

  console.log(answer.join("\n"));
};

const recursive = (a, b, n) => {
  if (n === 1) {
    answer.push(`${a} ${b}`);
    return;
  }

  recursive(a, 6 - a - b, n - 1);
  answer.push(`${a} ${b}`);
  recursive(6 - a - b, b, n - 1);
};

solve();
