# This project is used to set places for officers to
# get the greatest "activity points"

# Reads the necessary info from the file (filename)
filename = 'input2.txt'
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
pie = [0] * (2 *city_area_dimension - 1)
shu = [0] * city_area_dimension
na = [0] * (2 * city_area_dimension - 1)
count = 0


def dfs(row, officers):

	global count

	if row >= city_area_dimension and officers != 0:
		return None

	if officers > city_area_dimension - row:
		return None

	if officers == 0:
		count += 1
		return None

	for i in range(city_area_dimension):

		index_pie = row + i
		index_na = city_area_dimension - 1 + i - row

		if shu[i] == 1 or pie[index_pie] == 1 or na[index_na] == 1:
			continue

		shu[i] = 1
		pie[index_pie] = 1
		na[index_na] = 1

		dfs(row + 1, officers - 1)

		shu[i] = 0
		pie[index_pie] = 0
		na[index_na] = 0

	dfs(row + 1, officers)

dfs(0, number_officers)
print(count)


# filename = "output.txt"

# with open(filename, 'w') as file_object:
# 	file_object.write(str(activity_point))
