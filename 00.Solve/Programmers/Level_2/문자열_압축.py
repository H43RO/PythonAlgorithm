def solution(s):
    if len(s) == 1:  # 길이가 1인 문자열은
        return 1  # 항상 1이 답임

    result = len(s)
    window = len(s) // 2  # 끊는 단위를 입력 문자열 길이 // 2 로부터

    # 단위를 1씩 줄여가며 탐색
    for i in range(window, 0, -1):
        compression = 0
        temp = s[:i]  # 끊는 단위만큼 문자열 담아줄 거임
        count = 1  # 끊은 문자열이 몇 번 등장했는지 담아줄 거임
        for j in range(i, len(s), i):
            if temp == s[j:j + i]:  # 같은 문자열을 만나면
                count += 1  # 등장 횟수 1 증가
            else:  # 다른 문자열을 만나면 이전에 쌓아둔 문자열 압축
                if count > 1:  # 등장 횟수 1 초과였다면
                    compression += len(str(count))  # 등장횟수 자릿수 추가
                compression += len(temp)  # 끊은 문자열 개수 추가
                temp = s[j:j + i]  # 새로 등장한 문자열 저장
                count = 1  # 등장 횟수 1로 초기화

        # 루프가 끝나고 남은 문자열 처리
        if count > 1:  # 등장 횟수 1 초과였다면
            compression += len(str(count))  # 등장횟수 자릿수 추가
        compression += len(temp)  # 끊은 문자열 개수 추가

        result = min(result, compression)  # 최소 결과값 갱신
    return result


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
