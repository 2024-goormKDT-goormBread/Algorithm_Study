const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input.shift().split(' ').map(Number);
const board = input.map((row) => row.split(''));

// 오른쪽, 왼쪽, 아래, 위
const dy = [0, 0, 1, -1];
const dx = [1, -1, 0, 0];
const visited_red = Array.from({ length: n }, () =>
  Array.from({ length: m }, () => Infinity)
);

const blue = {
  y: 0,
  x: 0,
};
const red = {
  y: 0,
  x: 0,
};
const hole = {
  y: 0,
  x: 0,
};
let goal = false;

const solve = () => {
  initialize();
  console.log(bfs());
};

const initialize = () => {
  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < m; j += 1) {
      if (board[i][j] === 'B') {
        blue.y = i;
        blue.x = j;
        board[i][j] === '.';
      }

      if (board[i][j] === 'R') {
        red.y = i;
        red.x = j;
        board[i][j] === '.';
      }

      if (board[i][j] === 'O') {
        hole.y = i;
        hole.x = j;
      }
    }
  }
};

const bfs = () => {
  const queue = [];

  queue.push([red, blue, 0]);
  visited_red[red.y][red.x] = 0;

  while (queue.length) {
    console.log(queue);
    const [red, blue, depth] = queue.shift();

    if (depth >= 10) {
      return -1;
    }

    for (let i = 0; i < 4; i += 1) {
      let [redMoveY, redMoveX] = [red.y, red.x];
      let [blueMoveY, blueMoveX] = [blue.y, blue.x];
      let redMoveRes;
      let blueMoveRes;
      let flag = false;

      // 구슬이 먼저 출발하는 순서를 지정
      // 오른쪽, 왼쪽, 위, 아래
      if (
        (redMoveX >= blueMoveX && i === 0) ||
        (redMoveX < blueMoveX && i === 1) ||
        (redMoveY >= blueMoveY && i === 2) ||
        (redMoveY < blueMoveY && i === 3)
      ) {
        const tempRedMoveRes = redMove(
          { y: redMoveY, x: redMoveX },
          { y: blueMoveY, x: blueMoveX },
          i,
          depth
        );

        redMoveRes = tempRedMoveRes
          ? tempRedMoveRes
          : { y: redMoveY, x: redMoveX };

        const tempBlueMoveRes = blueMove(
          { y: blueMoveY, x: blueMoveX },
          { y: redMoveRes.y, x: redMoveRes.x },
          i
        );

        blueMoveRes = tempBlueMoveRes
          ? tempBlueMoveRes
          : { y: blueMoveY, x: blueMoveX };

        flag = tempRedMoveRes ? true : false;
      } else {
        const tempBlueMoveRes = blueMove(
          { y: blueMoveY, x: blueMoveX },
          { y: redMoveY, x: redMoveX },
          i
        );

        blueMoveRes = tempBlueMoveRes
          ? tempBlueMoveRes
          : { y: blueMoveY, x: blueMoveX };

        const tempRedMoveRes = redMove(
          { y: redMoveY, x: redMoveX },
          { y: blueMoveRes.y, x: blueMoveRes.x },
          i,
          depth
        );

        redMoveRes = tempRedMoveRes
          ? tempRedMoveRes
          : { y: redMoveY, x: redMoveX };

        flag = tempRedMoveRes ? true : false;
      }

      if (goal) {
        // console.log(blueMoveRes);
        if (blueMoveRes.y === hole.y && blueMoveRes.x === hole.x) {
          goal = false;
          continue;
        } else {
          return depth + 1;
        }
      }

      if (flag) {
        queue.push([
          { y: redMoveRes.y, x: redMoveRes.x },
          { y: blueMoveRes.y, x: blueMoveRes.x },
          depth + 1,
        ]);
      }
    }
  }

  return -1;
};

const redMove = (currRed, currBlue, i, depth) => {
  let [tempRedY, tempRedX] = [currRed.y, currRed.x];

  while (true) {
    // 다음으로 이동하는 위치가 유효한 범위 내에 있고, 다음 칸이 벽이나 파란 구슬이 아니라면 해당 방향으로 계속 이동한다.
    // 만약 도착 지점에 도착한다면 즉시 값을 반환한다.
    if (
      rangeCheck(tempRedY + dy[i], tempRedX + dx[i]) &&
      board[tempRedY + dy[i]][tempRedX + dx[i]] !== '#' &&
      !duplicateCheck(
        tempRedY + dy[i],
        tempRedX + dx[i],
        currBlue.y,
        currBlue.x
      )
    ) {
      tempRedY += dy[i];
      tempRedX += dx[i];

      if (tempRedY === hole.y && tempRedX === hole.x) {
        goal = true;
        return { y: tempRedY, x: tempRedX };
      }
    }
    // 다음으로 이동하는 위치가 유효한 범위 내에 있고, 다음 칸이 벽이나 파란 구슬이라면 이동을 멈춘다.
    // 이미 방문했는지 여부를 체크하고 해당 칸을 더 적은 이동으로 방문할 수 있다면 좌표값을 반환한다.
    else if (
      rangeCheck(tempRedY + dy[i], tempRedX + dx[i]) &&
      (board[tempRedY + dy[i]][tempRedX + dx[i]] === '#' ||
        duplicateCheck(
          tempRedY + dy[i],
          tempRedX + dx[i],
          currBlue.y,
          currBlue.x
        )) &&
      visited_red[tempRedY][tempRedX] > depth + 1
    ) {
      visited_red[tempRedY][tempRedX] = depth + 1;
      return { y: tempRedY, x: tempRedX };
    }
    // 위의 경우에 해당하지 않는다면 구슬이 유효한 범위 내에 있지 않으므로 이동 할 수 없다.
    else {
      return false;
    }
  }
};

const blueMove = (currBlue, currRed, i) => {
  let [tempBlueY, tempBlueX] = [currBlue.y, currBlue.x];

  while (true) {
    // 다음으로 이동하는 위치가 유효한 범위 내에 있고, 다음 칸이 벽이나 빨간 구슬이 아니라면 해당 방향으로 계속 이동한다.
    // console.log('blue move : ', currRed, tempBlueY, tempBlueX);
    if (
      rangeCheck(tempBlueY + dy[i], tempBlueX + dx[i]) &&
      board[tempBlueY + dy[i]][tempBlueX + dx[i]] !== '#' &&
      (!duplicateCheck(
        tempBlueY + dy[i],
        tempBlueX + dx[i],
        currRed.y,
        currRed.x
      ) ||
        goal)
    ) {
      tempBlueY += dy[i];
      tempBlueX += dx[i];

      if (tempBlueY === hole.y && tempBlueX === hole.x) {
        return { y: tempBlueY, x: tempBlueX };
      }
    }
    // 다음으로 이동하는 위치가 유효한 범위 내에 있고, 다음 칸이 벽이나 빨간 구슬이라면 이동을 멈추고 위치를 반환한다.
    else if (rangeCheck(tempBlueY + dy[i], tempBlueX + dx[i])) {
      return { y: tempBlueY, x: tempBlueX };
    }
    // 위의 경우에 해당하지 않는다면 구슬이 유효한 범위 내에 있지 않으므로 이동 할 수 없다.
    else {
      return false;
    }
  }
};

const rangeCheck = (axisY, axisX) =>
  axisY >= 0 && axisY < n && axisX >= 0 && axisX < m;

const duplicateCheck = (currY, currX, opponentY, opponentX) =>
  currY === opponentY && currX === opponentX;

solve();
