# CPU: 0.09 s
students = {}
projects = {}
cur_project = None
while True:
	inp = input()

	if inp == "0":
		break

	if inp == "1":
		projects = sorted(projects.items(), key=lambda x: (-x[1], x[0]))
		for project, count in projects:
			print(project, count)

		students = {}
		projects = {}
		cur_project = None
		continue

	if inp.isupper():
		cur_project = inp
		projects[cur_project] = 0
	elif inp in students:
		if students[inp] != cur_project:
			if students[inp] is not None:
				projects[students[inp]] -= 1
				students[inp] = None
	else:
		students[inp] = cur_project
		projects[cur_project] += 1
