# CPU: 0.11 s
while True:
    pos, num1, num2, num3 = map(int, input().split())
    if pos == num1 == num2 == num3 == 0:
        break
    
    # Clockwise 2 full turns
    degrees = 720
    # Stop at num1
    degrees += ((pos - num1) * 9) % 360
    # Counter-clockwise 1 full turn
    degrees += 360
    # Stop at num2
    degrees += ((num2 - num1) * 9) % 360
    # Clockwise until num3
    degrees += ((num2 - num3) * 9) % 360

    print(degrees)
