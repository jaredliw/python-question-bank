# CPU: 0.05 s
n = int(input())
before = input()
after = input()
if n % 2 == 1:
    # Flip bits
    before = "".join(map(lambda x: "0" if x == "1" else "1", before))
print("Deletion succeeded" if before == after else "Deletion failed")
