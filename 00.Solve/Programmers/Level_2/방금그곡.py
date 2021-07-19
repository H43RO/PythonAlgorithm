sharp = {'C#': '1', 'D#': '2', 'F#': '3', 'G#': '5', 'A#': '6'}


def solution(m, musicinfos):
    answer = ''

    for x in sharp.keys():
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
        if play_time >= len(note):
            play_note = note * (play_time // len(note))
            play_note += note[:(play_time % len(note))]
        else:
            play_note = note[:play_time]

        index = play_note.find(m)
        if index == -1:
            continue
        music.append((play_time, i, name))  # 재생시간, 입력순서, 제목 삽입

    if not music:
        return '(None)'
    music.sort(key=lambda x: (x[0], -x[1]), reverse=True)
    return music[0][2]


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
