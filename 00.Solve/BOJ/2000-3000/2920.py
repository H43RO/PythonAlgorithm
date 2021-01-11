note = list(map(int, input().split()))

ascending_note = sorted(note)
descending_note = sorted(note, reverse=True)

if note == ascending_note:
    print("ascending")
elif note == descending_note:
    print("descending")
else:
    print("mixed")