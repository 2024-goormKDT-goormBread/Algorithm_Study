// 2573: 빙산
// 요약 : 빙산이 언제 두덩어리 이상으로 갈라지는지 계산하시오
// bfs로 탐색을 모두 마쳤을 때 큐에 남아있는 원소의 개수와 탐색한 원소의 개수가 다르다면 두덩어리 이상으로 갈라졌음을 알수있다
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const dy = [0, 0, 1, -1];
const dx = [1, -1, 0, 0];

const solve = () => {
  const [n, m] = input.shift().split(" ").map(Number);
  const board = Array.from({ length: n }, (_, idx) =>
    input[idx].split(" ").map(Number)
  );
  let queue = [];
  let currDepth = 0;
  let cnt = 0;

  // queue에 노드 추가
  // cnt는 아직 녹지 않은 빙산의 개수를 카운팅
  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < m; j += 1) {
      if (board[i][j] !== 0) {
        queue.push({ axis: [i, j], val: board[i][j], depth: 0 });
        cnt += 1;
      }
    }
  }

  while (queue.length) {
    // 1년이 지났을 경우
    if (queue[0].depth !== currDepth) {
      const temp_queue = [];

      for (let i = 0; i < queue.length; i += 1) {
        // 녹지 않은 빙산 카운팅
        if (queue[i].val > 0) {
          temp_queue.push(queue[i]);
        }

        // 빙산이 다 녹으면 cnt를 감소시킴
        if (queue[i].val <= 0) {
          cnt -= 1;
        }

        // board에 값 갱신
        board[queue[i].axis[0]][queue[i].axis[1]] =
          queue[i].val > 0 ? queue[i].val : 0;
      }

      // queue 갱신
      queue = temp_queue;

      // 빙산이 다 녹았으면 불가능하므로 0 리턴
      if (cnt === 0) {
        return 0;
      }

      // 빙산이 갈라졌는지 체크, 갈라졌으면 depth 리턴
      if (isSplitted(n, m, queue, board)) {
        return queue[0].depth;
      }

      currDepth += 1;
    }

    // 노드 체크
    const { axis, val, depth } = queue.shift();
    // 빙산 주위 빈칸 체크
    let temp = 0;

    for (let i = 0; i < 4; i += 1) {
      const moveY = axis[0] + dy[i];
      const moveX = axis[1] + dx[i];

      if (
        depth === currDepth &&
        moveY >= 0 &&
        moveY < n &&
        moveX >= 0 &&
        moveX < m
      ) {
        // 빈칸이 있으면 temp + 1
        if (board[moveY][moveX] === 0) {
          temp += 1;
        }
      }
    }

    // queue에 다음 노드 추가
    queue.push({ axis, val: val - temp, depth: depth + 1 });
  }

  return 0;
};

// bfs로 빙산이 갈라졌는지 체크하는 로직
// bfs로 탐색한 노드와 queue의 원소의 개수가 다르면 빙산이 갈라졌음을 체크할 수 있음
const isSplitted = (n, m, queue, board) => {
  const copy_queue = [...queue];
  const visited = Array.from({ length: n }, () => new Array(m).fill(false));
  const check_queue = [];
  const { axis } = copy_queue.shift();
  // 탐색한 노드의 개수
  let cnt = 0;

  check_queue.push(axis);
  visited[axis[0]][axis[1]] = true;
  cnt += 1;

  while (check_queue.length) {
    const [currY, currX] = check_queue.shift();

    for (let i = 0; i < 4; i += 1) {
      const moveY = currY + dy[i];
      const moveX = currX + dx[i];

      if (moveY >= 0 && moveY < n && moveX >= 0 && moveX < m) {
        if (board[moveY][moveX] !== 0 && !visited[moveY][moveX]) {
          visited[moveY][moveX] = true;
          check_queue.push([moveY, moveX]);
          cnt += 1;
        }
      }
    }
  }

  return queue.length !== cnt;
};

console.log(solve());
