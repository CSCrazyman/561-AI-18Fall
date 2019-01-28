filename = 'input3.txt'
scooter_place_infos = []

with open(filename) as file_object:
	city_area_dimension = int(file_object.readline())
	number_officers = int(file_object.readline())
	number_scooters = int(file_object.readline())
	lines = file_object.readlines()

for x_count in range(city_area_dimension):
	scooter_place_infos.append([])
	for y_count in range(city_area_dimension):
		scooter_place_infos[x_count].append(0)

for line in lines:
	ordinates = line.split(",")
	x_ordinate = int(ordinates[0])
	y_ordinate = int(ordinates[1])
	scooter_place_infos[x_ordinate][y_ordinate] += 1

# --------------------------------------------------------
column = left_dia = right_dia = 0
activity_counts = [0] * number_officers
temp_column = 0
activity_point = 0


def dfs(row, officers):

	global column, left_dia, right_dia, temp_column, activity_point

	if row >= city_area_dimension and officers != 0:
		return None

	if officers > city_area_dimension - row:
		return None

	if officers == 0:
		temp_point = 0
		for x in range(len(activity_counts)):
			temp_point += activity_counts[x]

		if temp_point > activity_point:
			activity_point = temp_point
		return None

	ok = ((1 << city_area_dimension) - 1) & ~(column | (left_dia >> row) | (right_dia >> (city_area_dimension - 1 - row)))

	while ok:

		p = ok & -ok
		ok ^= p

		column ^= p

		diff = column - temp_column
		temp_count = 0
		while diff / 2 != 0:
			temp_count += 1
			diff = diff / 2
		temp_column = column

		left_dia ^= (p << row)
		right_dia ^= (p << (city_area_dimension - 1 - row))

		activity_counts[officers - 1] = scooter_place_infos[row][temp_count]

		dfs(row + 1, officers - 1)

		column ^= p
		temp_column = column
		left_dia ^= (p << row)
		right_dia ^= (p << (city_area_dimension - 1 - row))

	dfs(row + 1, officers)


dfs(0, number_officers)

filename = "output.txt"

with open(filename, 'w') as file_object:
	file_object.write(str(activity_point))

