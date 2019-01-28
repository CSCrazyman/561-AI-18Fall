# This project is used to set places for officers to
# get the greatest "activity points"

# Reads the necessary info from the input.txt
with open('input3.txt') as file_object:
	city_area_dimension = int(file_object.readline())
	number_officers = int(file_object.readline())
	number_scooters = int(file_object.readline())
	lines = file_object.readlines()

scooter_place_infos = []
scooter_place_visitors = []
x_count =0

while x_count < city_area_dimension:
	scooter_place_infos.append([])
	scooter_place_visitors.append([])
	y_count = 0
	while y_count < city_area_dimension:
		scooter_place_infos[x_count].append(0)
		scooter_place_visitors[x_count].append(0)
		y_count += 1
	x_count += 1


for line in lines:
	ordinates = line.split(",")
	x_ordinate = int(ordinates[0])
	y_ordinate = int(ordinates[1])
	scooter_place_infos[x_ordinate][y_ordinate] += 1


for number in range(0, city_area_dimension):
	print(scooter_place_infos[number][:])

# --------------------------------------------------------
print('-------------------------------------------------')
print('-------------------------------------------------')

count = 0

activity_point = 0
temp_point = 0

def dfs(row, officers):

	global count
	global activity_point
	global temp_point

	if row >= city_area_dimension and officers != 0:
		return None

	if officers > city_area_dimension - row:
		return None

	if officers == 0:
		count += 1
		for x in range(0, city_area_dimension):
			for y in range(0, city_area_dimension):
				if scooter_place_visitors[x][y] == 1:
					temp_point += scooter_place_infos[x][y]
		if temp_point > activity_point:
			activity_point = temp_point
		temp_point = 0
		return None

	for i in range(city_area_dimension):


		scooter_place_visitors[row][i] = 1


		if hasPlace(row, i):

			dfs(row + 1, officers - 1)

		scooter_place_visitors[row][i] = 0

	dfs(row + 1, officers)


def hasPlace(thisrow, thisline):
	for j in range(thisrow):
		if scooter_place_visitors[j][thisline] == 1:
			return False
		if thisrow + thisline - j >= 0 and thisrow + thisline - j < city_area_dimension:
			if scooter_place_visitors[j][thisrow + thisline - j] == 1:
				return False
		if thisline - thisrow + j >= 0 and thisline - thisrow + j < city_area_dimension:
			if scooter_place_visitors[j][thisline - thisrow + j] == 1:
				return False
	return True

dfs(0, number_officers)

print(activity_point)
print(count)
