const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const directionX = [1, -1, 0, 0];
const directionY = [0, 0, 1, -1];
let ans = 0;

rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  const [n, m] = input.shift().split(' ').map(Number);
  const board = input.map((row) => row.split(' ').map(Number));

  solution(n, m, board);
  process.exit();
});

const solution = (n, m, board) => {
  dfs(n, m, board, 0);
  console.log(ans);
};

const dfs = (n, m, board, cnt) => {
  if (cnt === 3) {
    const copyBoard = board.map((v) => [...v]);
    const safeAreaNum = calculateSafeArea(n, m, copyBoard);

    ans = Math.max(ans, safeAreaNum);

    return;
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (board[i][j] === 0) {
        board[i][j] = 1;
        dfs(n, m, board, cnt + 1);
        board[i][j] = 0;
      }
    }
  }
};

const calculateSafeArea = (n, m, board) => {
  let cnt = 0;
  const queue = [];

  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < m; j += 1) {
      if (board[i][j] === 2) {
        queue.push([i, j]);
      }
    }
  }

  while (queue.length) {
    const [currY, currX] = queue.shift();

    for (let i = 0; i < 4; i++) {
      const [moveY, moveX] = [currY + directionY[i], currX + directionX[i]];

      if (
        moveX >= 0 &&
        moveX < m &&
        moveY >= 0 &&
        moveY < n &&
        board[moveY][moveX] === 0
      ) {
        board[moveY][moveX] = 2;
        queue.push([moveY, moveX]);
      }
    }
  }

  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < m; j += 1) {
      if (board[i][j] === 0) {
        cnt += 1;
      }
    }
  }

  return cnt;
};
