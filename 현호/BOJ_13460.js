const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input.shift().split(' ').map(Number);
const board = input.map((row) => row.split(''));

// 오른쪽, 왼쪽, 아래, 위
const dy = [0, 0, 1, -1];
const dx = [1, -1, 0, 0];
const BLUE = [0, 0];
const RED = [0, 0];
const HOLE = [0, 0];

const solve = () => {
  initialize();
  console.log(bfs());
};

const initialize = () => {
  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < m; j += 1) {
      if (board[i][j] === 'B') {
        [BLUE[0], BLUE[1]] = [i, j];
        board[i][j] = '.';
      }

      if (board[i][j] === 'R') {
        [RED[0], RED[1]] = [i, j];
        board[i][j] = '.';
      }

      if (board[i][j] === 'O') {
        [HOLE[0], HOLE[1]] = [i, j];
      }
    }
  }
};

const bfs = () => {
  const queue = [];

  queue.push([RED, BLUE, 1]);

  while (queue.length) {
    // console.log(queue);
    const [red, blue, depth] = queue.shift();

    for (let i = 0; i < 4; i += 1) {
      const tempRed = [red[0], red[1]];
      const tempBlue = [blue[0], blue[1]];

      if (isRedBallFirst(tempRed, tempBlue, i)) {
        moveBall(tempRed, tempBlue, i);
        moveBall(tempBlue, tempRed, i);
      } else {
        moveBall(tempBlue, tempRed, i);
        moveBall(tempRed, tempBlue, i);
      }

      const [redCheck, blueCheck] = [isEscape(tempRed), isEscape(tempBlue)];

      if (blueCheck) {
        continue;
      }

      if (redCheck) {
        return depth;
      }

      if (depth === 10) {
        continue;
      }

      const [isRedMove, isBlueMove] = [
        isMove(tempRed, red),
        isMove(tempBlue, blue),
      ];

      if (isRedMove || isBlueMove) {
        queue.push([tempRed, tempBlue, depth + 1]);
      }
    }
  }

  return -1;
};

// 오른쪽, 왼쪽, 아래, 위
const isRedBallFirst = (red, blue, i) =>
  (red[1] > blue[1] && i === 0) ||
  (red[1] <= blue[1] && i === 1) ||
  (red[0] > blue[0] && i === 2) ||
  (red[0] <= blue[0] && i === 3);

const moveBall = (target, opponent, dir) => {
  while (true) {
    const [moveY, moveX] = [target[0] + dy[dir], target[1] + dx[dir]];

    if (moveY === opponent[0] && moveX === opponent[1]) {
      break;
    } else if (board[moveY][moveX] === '.') {
      [target[0], target[1]] = [moveY, moveX];
    } else if (board[moveY][moveX] === 'O') {
      [target[0], target[1]] = [-1, -1];
      break;
    } else {
      break;
    }
  }
};

const isEscape = (ball) => ball[0] === -1 && ball[1] === -1;

const isMove = (move, origin) => move[0] !== origin[0] || move[1] !== origin[1];

solve();
