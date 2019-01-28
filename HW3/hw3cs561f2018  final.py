from copy import deepcopy
import numpy as np
# Gets the necessary info including: 1. the size of grids i.e. 3 * 3
#									 2. the number of cars
#									 3. the number of obstacles
#									 4. locations of obstacles
#									 5. start locations of cars
# 									 6. terminal locations of cars
filename = "input.txt"

DISCOUNT_FACTOR = 0.9
MAX_ERROR = 0.1

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
locations_of_obs = []
starts_of_cars = []
ends_of_cars = []
grids = []

with open(filename) as file_object:
	grids_size = int(file_object.readline())
	number_of_cars = int(file_object.readline())
	number_of_obs = int(file_object.readline())
	for x in range(number_of_obs):
		locations_of_obs.append(file_object.readline().rstrip())
	for x in range(number_of_cars):
		starts_of_cars.append(file_object.readline().rstrip())
	for x in range(number_of_cars):
		ends_of_cars.append(file_object.readline().rstrip())

# each grid has two elements: 1. direction --> default: -1, north: 0, south: 1, east: 2, west: 3
#							  2. value --> default: -1, a obstacle: -101, destination: 99
for x in range(grids_size):
	grids.append([])
	for y in range(grids_size):
		grid = {'direction': -1, 'value': -1, 'index': x * grids_size + y,}
		grids[x].append(grid)


for x in range(number_of_obs):
	ordinates = locations_of_obs[x].split(',')
	grids[int(ordinates[1])][int(ordinates[0])]['value'] = -101



#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

correct = 0.7
uncorrect = 0.1

def max_policy(initial_array, value_array, direction_array, x, y):


	north = south = west = east = 0
	single_directions = []
	new_value = 0

	#north
	if x == 0:
		north = value_array[x][y]
	else:
		north = value_array[x - 1][y]

	#south
	if x == grids_size - 1:
		south = value_array[x][y]
	else:
		south = value_array[x + 1][y]

	#east
	if y == grids_size - 1:
		east = value_array[x][y]
	else:
		east = value_array[x][y + 1]

	#west
	if y == 0:
		west = value_array[x][y]
	else:
		west = value_array[x][y - 1]

	up = correct * north + uncorrect * (south + east + west)
	down = correct * south + uncorrect * (north + east + west)
	left = correct * west + uncorrect * (north + south + east)
	right = correct * east + uncorrect * (north + south + west)

	single_directions.append(up)
	single_directions.append(down)
	single_directions.append(right)
	single_directions.append(left)

	single_direction = 0
	single = up

	for i in range(len(single_directions)):
		if single_directions[i] > single:
			single = single_directions[i]
			single_direction = i

	direction_array[x][y] = single_direction

	new_value = round(initial_array[x][y] + single * DISCOUNT_FACTOR , 6)



	return new_value




def value_iteration(end):

	value_array = []
	direction_array = []
	stop_factor = MAX_ERROR * (1 - DISCOUNT_FACTOR) / DISCOUNT_FACTOR

	for x in range(grids_size):
		value_array.append([])
		direction_array.append([])
		for y in range(grids_size):
			value_array[x].append(grids[x][y]['value'])
			direction_array[x].append(grids[x][y]['direction'])

	new_end_x = int(end[1])
	new_end_y = int(end[0])

	value_array[new_end_x][new_end_y] = 99

	initial_array = deepcopy(value_array)


	while stop_factor >= MAX_ERROR * (1 - DISCOUNT_FACTOR) / DISCOUNT_FACTOR :

		stop_factor = 0
		temp_value_array = []

		for x in range(grids_size):
			temp_value_array.append([])
			for y in range(grids_size):

				if value_array[x][y] == 99:
					temp_value_array[x].append(99)
					continue

				temp_value_array[x].append(max_policy(initial_array,value_array, direction_array,x, y))

		for x in range(grids_size):
			for y in range(grids_size):
				substract = temp_value_array[x][y] - value_array[x][y]
				if (substract > stop_factor):
					stop_factor = substract


		value_array = deepcopy(temp_value_array)


	return direction_array




#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
def car_go(new_girds, start_x, start_y, time):

	x = start_x
	y = start_y
	value = 0

	np.random.seed(time)
	swerve = np.random.random_sample(1000000)
	
	k = 0

	while new_girds[x][y] != -1:

		direction = new_girds[x][y]

		if swerve[k] > 0.7:
			if swerve[k] > 0.8:
				if swerve[k] > 0.9:
					direction = move_right(move_right(direction))
				else:
					direction = move_right(direction)
			else:
				direction = move_left(direction)

		k += 1	

		if direction == 0:
			if (x - 1) < 0:
				value += grids[x][y]['value']
				continue
			else:
				x -= 1
				value += grids[x][y]['value']
		elif direction == 1:
			if (x + 1) >= grids_size:
				value += grids[x][y]['value']
				continue
			else:
				x += 1
				value += grids[x][y]['value']
		elif direction == 2:
			if (y + 1) >= grids_size:
				value += grids[x][y]['value']
				continue
			else:
				y += 1
				value += grids[x][y]['value']
		else:
			if (y - 1) < 0:
				value += grids[x][y]['value']
				continue
			else:
				y -= 1
				value += grids[x][y]['value']


	value += 100

	return value

def move_left(direction):

	if direction == 0:
		return 3
	elif direction == 1:
		return 2
	elif direction == 2:
		return 0
	else: 
		return 1

def move_right(direction):

	if direction == 0:
		return 2
	elif direction == 1:
		return 3
	elif direction == 2:
		return 1
	else:
		return 0

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

moneys = []

for x in range(number_of_cars):

	start_location = starts_of_cars[x].split(',')
	end_location = ends_of_cars[x].split(',')
	start_x = int(start_location[1])
	start_y = int(start_location[0])
	money = 0

	policy = value_iteration(end_location)

	for j in range(10):
		money += car_go(policy, start_x, start_y, j)

	moneys.append(money / 10)


filename = "output.txt"

with open(filename, 'w') as write_file:
	for i in range(len(moneys)): 
		write_file.write(str(moneys[i]) + "\n")

	
