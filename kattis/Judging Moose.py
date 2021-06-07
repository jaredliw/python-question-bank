# CPU: 0.06 s
left, right = map(int, input().split())
if left == right:
    if left == 0:
        print("Not a moose")
    else:
        print("Even", left * 2)
else:
    print("Odd", max(left, right) * 2)
