const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const amount = +input.shift();
const numbers = input.map(Number).sort((a, b) => a - b);

const solve = () => {
  const two = new Map();
  let max = -1;

  for (let i = 0; i < amount; i += 1) {
    for (let j = i; j < amount; j += 1) {
      if (!two.has(numbers[i] + numbers[j])) {
        two.set(numbers[i] + numbers[j], 1);
      }
    }
  }

  for (let i = amount - 1; i > 0; i -= 1) {
    for (let j = 0; j < i; j += 1) {
      if (two.has(numbers[i] - numbers[j])) {
        max = Math.max(max, numbers[i]);
      }
    }
  }

  console.log(max);
};

solve();
