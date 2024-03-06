const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, k] = input[0].split(" ").map(Number);
const numbers = input[1].split(" ").map(Number);

const solve = () => {
  const curr = [];
  let answer = 0;

  for (let i = 0; i < numbers.length; i += 1) {
    // 포트가 다 채워지지 않은 상태일 때
    if (curr.length < n && !curr.includes(numbers[i])) {
      curr.push(numbers[i]);
      continue;
    }

    // 포트가 다 채워진 상태인데 현재 베열에 존재하지 않을 때
    if (!curr.includes(numbers[i])) {
      const idx = getLateIndex(curr, i);

      curr[idx] = numbers[i];
      answer += 1;
    }
  }

  console.log(answer);
};

// 지금 curr 배열에 들어있는 원소 중 다음으로 가장 늦게 나오는 원소를 찾음
const getLateIndex = (curr, currIdx) => {
  const indexArr = [];

  //   console.log(curr, currIdx);

  for (let i = 0; i < curr.length; i += 1) {
    indexArr.push(numbers.indexOf(curr[i], currIdx));
  }

  return indexArr.includes(-1)
    ? indexArr.indexOf(-1)
    : indexArr.indexOf(Math.max(...indexArr));
};

solve();
