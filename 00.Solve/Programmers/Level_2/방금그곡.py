# 샾 음계에 대해서 별개의 음계로 치환
# 예를들어 C 와 C# 을 구분해주기 위한 목적도 있고,
# C# 의 문자열 길이가 2인지라 2개 음계로 인식될 수 있기 때문에 한 자리로 치환
sharp = {'C#': '1', 'D#': '2', 'F#': '3', 'G#': '5', 'A#': '6'}


def solution(m, musicinfos):
    answer = ''

    for x in sharp.keys():  # 기억한 멜로디의 샾 음계 모두 치환
        m = m.replace(x, sharp[x])

    music = []
    for i, x in enumerate(musicinfos):
        start, end, name, note = x.split(",")
        start_h, start_m = map(int, start.split(":"))
        end_h, end_m = map(int, end.split(":"))

        for x in sharp.keys():  # 악보의 # 음계를 모두 치환
            note = note.replace(x, sharp[x])

        # 재생 시간과 실제 재생 멜로디를 계산
        play_time = (end_h * 60 + end_m) - (start_h * 60 + start_m)
        play_note = note * (play_time // len(note))
        play_note += note[:(play_time % len(note))]

        index = play_note.find(m)
        if index == -1:  # 문자열을 찾기 못하면 -1 반환
            continue
        music.append((play_time, i, name))  # 재생시간, 입력순서, 제목 삽입

    if not music:
        return '(None)'
    music.sort(key=lambda x: (x[0], -x[1]), reverse=True)
    return music[0][2]


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
