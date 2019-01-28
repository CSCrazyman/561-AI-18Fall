# This project is used to set places for officers to
# get the greatest "activity points"

# Reads the necessary info from the file (filename)
filename = 'input1.txt'
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
# count = 0
array = [-city_area_dimension] * city_area_dimension
row_points = [0] * number_officers
activity_point = 0


def dfs(row, officers):

	global count
	global activity_point

	if row >= city_area_dimension and officers != 0:
		return None

	if officers > city_area_dimension - row:
		return None

	if officers == 0:
		# count += 1
		print(row_points)
		for x in range(len(row_points)):
			activity_point += row_points[x]
		print(activity_point)
		activity_point = 0
		return None

	for i in range(city_area_dimension):

		array[row] = i

		if hasPlace(row):

			row_points[officers - 1] = scooter_place_infos[row][i]

			dfs(row + 1, officers - 1)

		array[row] = -city_area_dimension

	dfs(row + 1, officers)


def hasPlace(thisrow):

	for j in range(thisrow):
		if array[j] == array[thisrow]:
			return False
		if (j - array[j]) == (thisrow - array[thisrow]):
			return False
		if (j + array[j]) == (thisrow + array[thisrow]):
			return False
	return True

dfs(0, number_officers)