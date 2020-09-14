#!/usr/bin/env python3

from sklearn.neighbors import NearestNeighbors
import csv

#building_codes.csv -- id,code,name
#meal_plan.csv -- student_id,on_meal_plan
#door_data.csv -- day,day_of_week,student_id,time_of_day,building,is_dining_hall,is_book_return
dictionary = {}

#ids.csv is made in process_data.py, it is just a list of all the ids
with open('ids.csv', newline='') as csvfile3: 
	rows = csv.reader(csvfile3, delimiter=',')
	for row in rows: 

		#initialize list of 300 markers (-1s) for each id 
		if (row[0]) not in dictionary: 
			dictionary[(row[0])] = [-1]*300

#open neighbors datafile, not necessary for program to work
#with open('neighbors_data.csv', 'w+', newline='') as csvfile_write:
#	neighbors_datafile = csv.writer(csvfile_write, delimiter=',')
	
#open door data 
with open('door_data.csv', newline='') as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=',')
	day_counter = 0
	row_numb = 0

	#for each row, put information into dictionary if its a dinner swipe
	for row in csv_reader: 
		if (row_numb % 100000) == 0:
			print(row_numb)

		if row_numb != 0: 

			#get information from row
			day_counter = int(row[0])
			student_id = row[2]
			time_of_day = int(row[3])
			building = row[4]
			is_dining_hall = int(row[5])

			#if it's a dining hall during dinner time, put into the dictionary for the student 
			if is_dining_hall == 1:
				if ((time_of_day >= 1080) and (time_of_day <= 1200)):
					dictionary[student_id][day_counter * 2] = int(building)
					dictionary[student_id][(day_counter * 2) + 1] = int(time_of_day)
			
		row_numb += 1

		#write into csv file, not necessary for program to work 
		#for item in dictionary: 
		#	neighbors_datafile.writerow([item])
		#	neighbors_datafile.writerow(dictionary[item])

#define function to compare two dining schedules and output score (the lower, the closer the two schedules)
def compare(dining_info_1, dining_info_2):
	score = 0
	for i in range(150): 

		#if they enter the same dining hall within 30 minutes, increase score by one
		if (int(dining_info_1[2*i] == -1) and (dining_info_2[2*i] == -1)): 
			score = score + .25
		elif (dining_info_1[2*i] == dining_info_2[2*i]):
			if (abs((dining_info_1[(2*i) + 1] - dining_info_2[(2*i) + 1]) <= 30)): 
				score = score + 1

	#return 150 minus score because nearest neighbors algorithm counts lower number as closer 
	return (150 - score)


#make list of the dining schedules to input to nearest neighbors 
samples = []
for item in dictionary: 
	samples.append(dictionary[item]) 


#function to run nearest neighbors algorithm
def find_neighbors(student_id):

	#run nearestneighbors with compare function
	neigh  = NearestNeighbors(metric=compare)
	
	#fit on list of all dining schedules
	neigh.fit(samples)

	#find indices of 6 nearest neighbors, first will be self 
	neighbors = (neigh.kneighbors([dictionary[student_id]], n_neighbors=6, return_distance=False))
	
	#get the index of the nearest neighbors, ignore the first 
	neighbor2 = neighbors[0][1]
	neighbor3 = neighbors[0][2]
	neighbor4 = neighbors[0][3]
	neighbor5 = neighbors[0][4]
	neighbor6 = neighbors[0][5]

	counter = 0
	print("Potential friends for student " + student_id + ":")

	#find the indexed items
	for item in dictionary: 
		if (((((counter == neighbor6) or (counter == neighbor2)) or (counter == neighbor3)) or (counter == neighbor4)) or (counter == neighbor5)): 
			print(item)
		counter += 1

#examples, and the one the problem asks for 
find_neighbors('2969414704160674')
find_neighbors('1814363509790015')
find_neighbors('0206083445110298')

#output 
#Five potential friends for student 2969414704160674 are:
#571501919439390
#0889619518791047
#4337759318218479
#3060879441123832
#5098296110212146
#Five potential friends for student 1814363509790015 are:
#2501903768994060
#2095779006886677
#4507644598328615
#6791040759699290
#6206743404600088
#Five potential friends for student 0206083445110298 are:
#5724987220644370
#7709749937413192
#7621283967437135
#0106334226762814
#5817203146277796