alpha = list("abcdefghijklmnopqrstuvwxyz")
data = input()

# 입력 데이터 내에서 알파벳 순으로 순차탐색
for i in range(len(alpha)):
    # 해당 알파벳이 아예 없으면 -1 넣어줌
    if data.count(alpha[i]) == 0:
        print("-1", end=" ")
    # 해당 알파벳이 처음 등장한 인덱스 출력
    else:
        print(data.index(alpha[i]), end=" ")
