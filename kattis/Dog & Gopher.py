# CPU: 0.06 s
from sys import stdin

gopher_x, gopher_y, dog_x, dog_y = map(float, input().split())
for hole in stdin.readlines():
	hole_x, hole_y = map(float, hole.split())
	dist_hole_dog = ((dog_x - hole_x) ** 2 + (dog_y - hole_y) ** 2) ** 0.5
	dist_hole_gopher = ((gopher_x - hole_x) ** 2 + (gopher_y - hole_y) ** 2) ** 0.5
	# Speed of dog = 2x
	if dist_hole_dog > dist_hole_gopher * 2:
		print(f"The gopher can escape through the hole at ({hole_x:.3f},{hole_y:.3f}).")
		break
else:
	print("The gopher cannot escape.")
