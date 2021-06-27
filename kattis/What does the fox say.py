# CPU: 0.06 s
for _ in range(int(input())):
    recording = input().split()
    line = input()
    while line != "what does the fox say?":
        sound = line.split()[-1]
        recording = list(filter(lambda x: x != sound, recording))
        line = input()
    print(" ".join(recording))
