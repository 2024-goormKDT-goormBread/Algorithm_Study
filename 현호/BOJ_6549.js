// 백준 6549: 히스토그램에서 가장 큰 직사각형
// 통과여부 : X (추후 수정 예정)
// 설명 : 히스토그램 막대의 높이가 주어졌을 때, 가장 큰 직사각형의 넓이를 구하시오

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

rl.on("line", (line) => {
  input.push(line);
}).on("close", () => {
  solve();
  process.exit();
});

const solve = () => {

  const numbers = input.map((str) => str.split(" ").map(Number));

  numbers.forEach((numberList) => {
    if (numberList[0] === 0) return;
    getMaxSquareSize(numberList.slice(1, numberList.length));
  });
};

const getMaxSquareSize = (numbers) => {
  const copy_numbers = [...numbers];
  const temp = [];
  let max = -1;

  while (copy_numbers.length) {
    // 값을 추가하는 경우
    // case. temp 배열이 비어있음
    // case. copy_numbers의 마지막 값이 temp의 요소 최솟값보다 같거나 크면
    if (
        !temp.length ||
        copy_numbers[copy_numbers.length - 1] >= Math.min(...temp)
    ) {
      temp.push(copy_numbers.pop());
      continue;
    }

    // case. copy_numbers의 마지막 값이 temp의 최솟값보다 작다면
    if (Math.min(...temp) > copy_numbers[copy_numbers.length - 1]) {
      // 지금까지 구한 히스토그램의 넓이가 copy_numbers의 마지막 값을 넣고 계산한거보다 작으면
      // 배열에 투입
      if (
          Math.min(...temp) * temp.length <
          copy_numbers[copy_numbers.length - 1] * (temp.length + 1)
      ) {
        temp.push(copy_numbers.pop());
      }
          // 지금까지 구한 히스토그램의 넓이가 copy_numbers의 마지막 값을 넣고 계산한거보다 크다면
      // 넓이를 최댓값과 비교한 다음 배열을 비운다
      else {
        if (Math.min(...temp) * temp.length > max) {
          max = Math.min(...temp) * temp.length;
        }

        while (temp.length) temp.pop();
        copy_numbers.pop();
      }
    }


    // 한번 과정을 거쳤으면 최댓값과 비교한다.
    if (Math.min(...temp) * temp.length > max) {
      max = Math.min(...temp) * temp.length;
    }
  }

  // temp에 남아있는 값들과 최댓값을 비교한다.
  if (Math.min(...temp) * temp.length > max) {
    max = Math.min(...temp) * temp.length;
  }

  console.log(max);
};
