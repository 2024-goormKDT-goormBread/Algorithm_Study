const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, m] = input.shift().split(" ").map(Number);
const numbers = input
  .shift()
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);

const answer = new Set();

// n개중에서 m개를 고르는 경우의 수를 출력
const solve = () => {
  const visited = Array.from({ length: n }, () => false);

  dfs([], visited);

  console.log(Array.from(answer).join("\n"));
};

const dfs = (list, visited) => {
  if (check(list, m)) {
    answer.add([...list].sort((a, b) => a - b).join(" "));
    return;
  }

  for (let i = 0; i < n; i += 1) {
    if (visited[i]) {
      continue;
    }

    visited[i] = true;
    list.push(numbers[i]);
    dfs(list, visited);
    list.pop();
    visited[i] = false;
  }
};

const check = (list, m) => {
  const set = new Set(list);

  return set.size === m;
};

solve();
