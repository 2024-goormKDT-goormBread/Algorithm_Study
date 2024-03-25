const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = +input.shift();
const board = input.map((line) => line.split(' ').map(Number));
const result = [0, 0, 0];

const solve = () => {
  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < n; j += 1) {
      board[i][j] += 1;
    }
  }

  divide(0, 0, n);

  console.log(result.join('\n'));
};

const divide = (row, col, num) => {
  if (check(row, col, num)) {
    result[board[row][col]] += 1;
  } else {
    const size = Number(num / 3);

    for (let i = 0; i < 3; i += 1) {
      for (let j = 0; j < 3; j += 1) {
        divide(row + i * size, col + j * size, size);
      }
    }
  }
};

const check = (row, col, num) => {
  const start = board[row][col];

  for (let i = row; i < row + num; i += 1) {
    for (let j = col; j < col + num; j += 1) {
      if (start !== board[i][j]) {
        return false;
      }
    }
  }

  return true;
};

solve();
