# CPU: 0.10 s
for _ in range(int(input())):
    beat, sec = map(float, input().split())
    print((beat - 1) * 60 / sec, beat * 60 / sec, (beat + 1) * 60 / sec)
