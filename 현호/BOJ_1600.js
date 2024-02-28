// 1600 : 말이 되고싶은 원숭이
// 요약 : 도착지점까지 이동하는 최소 횟수를 구해라
// 방문 처리를 까다롭게 하는 경우

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// 일반 이동
const dx = [1, -1, 0, 0];
const dy = [0, 0, 1, -1];

// 말 이동
const horseX = [2, 2, 1, 1, -1, -1, -2, -2];
const horseY = [1, -1, 2, -2, 2, -2, 1, -1];

const solve = () => {
  // 말로 움직이는 횟수
  const K = Number(input.shift());
  const [W, H] = input.shift().split(" ").map(Number);
  const board = input.map((str) => str.split(" ").map(Number));
  // 3차원 배열 형태의 방문배열 생성
  const visited = Array.from({ length: H }, () =>
    Array.from({ length: W }, () => Array(K + 1).fill(false))
  );

  // 방문 예정 목록 생성 및 방문 처리
  const queue = [{ x: 0, y: 0, horseMoves: 0, depth: 0 }];
  visited[0][0][0] = true;

  while (queue.length) {
    const { x, y, horseMoves, depth } = queue.shift();

    // 목표 지점에 도착했다면
    if (x === W - 1 && y === H - 1) {
      console.log(depth);
      return;
    }

    // 일반 이동
    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      // 유효한 범위고 + 벽이 아니며 + 말 이동으로 방문하지 않았다면
      if (
        nx >= 0 &&
        nx < W &&
        ny >= 0 &&
        ny < H &&
        board[ny][nx] === 0 &&
        !visited[ny][nx][horseMoves]
      ) {
        visited[ny][nx][horseMoves] = true;
        queue.push({ x: nx, y: ny, horseMoves, depth: depth + 1 });
      }
    }

    // 말의 이동
    if (horseMoves < K) {
      for (let i = 0; i < 8; i++) {
        const nx = x + horseX[i];
        const ny = y + horseY[i];

        // 유효한 범위고 + 벽이 아니며 + 말 이동을 한번 더 해서 방문 한 적이 없었다면
        if (
          nx >= 0 &&
          nx < W &&
          ny >= 0 &&
          ny < H &&
          board[ny][nx] === 0 &&
          !visited[ny][nx][horseMoves + 1]
        ) {
          visited[ny][nx][horseMoves + 1] = true;
          queue.push({
            x: nx,
            y: ny,
            horseMoves: horseMoves + 1,
            depth: depth + 1,
          });
        }
      }
    }
  }

  // 큐가 다 비워졌는데도 답을 찾을 수 없었으므로 -1 리턴
  console.log(-1);
};

solve();
