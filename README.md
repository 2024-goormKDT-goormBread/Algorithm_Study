# 제출 방법

0. 브랜치가 생성되어있지 않다면 브랜치를 생성해주세요. 브랜치 이름은 feat/이름 으로 설정해주시면 됩니다. ex) feat/현호

```bash
git checkout -b feat/이름 // 브랜치 생성
```

1. 스터디 한 회가 끝나면 반드시 버전을 관리해주세요. 단, 이 때 브랜치를 확인하셔야합니다.

- 콘솔에서 레포지토리를 업데이트 하는 방법

```bash
git checkout main // 브랜치를 main으로 전환

git pull // main 기준으로 브랜치를 업데이트
```

- 업데이트 이후

```bash
git checkout feat/이름 // 자기 브랜치로 복귀
```

**반드시 자기 브랜치 내에서 작업해야합니다. 깃 버전이 꼬여요**

2. 문제 제출은 **BOJ\_문제번호.js** 형식으로 작성해주세요

3. 문제를 업로드 해주세요

```bash
git add -A

git commit -m "feat : 이름 문제이름 풀이 업로드"

git push origin feat/이름
```

4. 풀 리퀘스트를 생성해주세요

![image](https://github.com/SWARVY/Caffhheiene_introduce/assets/53262430/526e31fc-a94a-485f-a7cd-7b4d4807b326)

New pull request 버튼을 눌러서 PR을 생성해주세요

ex) 신현호 N주차 풀이 업로드

5. 리뷰를 작성해주세요

![image](https://github.com/SWARVY/SWARVY/assets/53262430/606b7a32-aeaa-4508-b940-398dd7097f75)

File changed 를 클릭한 후 해당 문제에 대한 리뷰를 진행합니다.

![image](https://github.com/2024-goormKDT-goormBread/Algorithm_Study/assets/53262430/8f7aac3f-f60e-4c89-9d26-072574813947)

+ 버튼을 눌러 해당 부분에 대한 리뷰를 진행할 수 있습니다.

