#!/usr/bin/env python3

import csv
import statistics
from statistics import mode, StatisticsError
#building_codes.csv -- id,code,name
#meal_plan.csv -- student_id,on_meal_plan
#door_data.csv -- day,day_of_week,student_id,time_of_day,building,is_dining_hall,is_book_return


colleges_list = ['49', '6', '10', '68', '71', '62', '70', '7', '17', '22', '31', '26', '51', '46']
college_dictionary = {}
college_dictionary['49'] = 'Pauli Murray'
college_dictionary['6'] = 'Benjamin Franklin'
college_dictionary['10'] = 'Branford'
college_dictionary['68'] = 'Saybrook'
college_dictionary['71'] = 'Timothy Dwight'
college_dictionary['62'] = 'Silliman'
college_dictionary['70'] = 'Trumbull'
college_dictionary['7'] = 'Berkeley'
college_dictionary['17'] = 'Davenport'
college_dictionary['22'] = 'Ezra Stiles'
college_dictionary['31'] = 'Johnathan Edwards'
college_dictionary['26'] = 'Grace Hopper'
college_dictionary['51'] = 'Pierson'
college_dictionary['46'] = 'Morse'
days_of_week_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# Select last swipe into a residential college for each student each day


dictionary = {}

#Only needs to run once, makes "sleep_data.csv" with the last swipe of each student into a res college each day 

#with open('pre_sleep_data.csv', 'w+', newline='') as csvfile_write:
#	pre_sleep_datafile = csv.writer(csvfile_write, delimiter=',')
#	with open('door_data.csv', newline='') as csvfile:
#		row_numb = 0
#		id_list = []
#		emptied_list = 0
#
#		#reverse so that the last entry into a dorm is first 
#		rows = reversed(list(csv.reader(csvfile, delimiter=',')))
#		for row in rows:
#			if (row_numb % 1000000 == 0):
#				print(row_numb)
#			if ("day" not in row[0]): 
#
#				if ((int(row[3]) < 120) and (int(row[0]) == 0)):
#					#do nothing
#					p = 1
#				elif ((int(row[3]) >= 120) and (int(row[0]) == 149)):
#					#do nothing 
#					p = 1
#				
#				#if its a new day (before 2am, going backwards), empty the id list, and put it in as the previous day scaled back two hours
#				elif ((int(row[3]) < 120) and (emptied_list == 0)): 
#					id_list = []
#					emptied_list = 1
#					if ((row[4] in colleges_list) and (row[2] not in id_list)):
#						pre_sleep_datafile.writerow([(str(int(row[0]) - 1)), (str(int(row[1]) - 1)), row[2], (str(int(row[3]) + 1320)), row[4], row[5], row[6]])
#						id_list.append(row[2])
#
#				#if its before 2 am, and is a dining hall and havent run into the id yet, then put into sleep_data as previous day scaled back two hours
#				elif (int(row[3]) < 120): 
#					if ((row[4] in colleges_list) and (row[2] not in id_list)):
#						pre_sleep_datafile.writerow([(str(int(row[0]) - 1)), (str(int(row[1]) - 1)), row[2], (str(int(row[3]) + 1320)), row[4], row[5], row[6]])
#						id_list.append(row[2])
#
#				#if its after 2am, then decrease time by two hours and put in the output as same day. 
#				elif (int(row[3]) >= 120):
#					emptied_list = 0
#					if ((row[4] in colleges_list) and (row[2] not in id_list)):
#						pre_sleep_datafile.writerow([row[0], row[1], row[2], (str(int(row[3]) - 120)), row[4], row[5], row[6]])
#						id_list.append(row[2])
#			row_numb += 1			
#print("made pre_sleep_data.csv")

#reverse pre_sleep_data back into correct order
with open('sleep_data.csv', 'w+', newline='') as csvfile_write: 
	sleep_datafile = csv.writer(csvfile_write, delimiter=',')
	with open('pre_sleep_data.csv', newline='') as csvfile: 
		rows = reversed(list(csv.reader(csvfile, delimiter=',')))
		for row in rows: 
			sleep_datafile.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6]])

#print("made sleep_data.csv")

#read ids into dictionary with list of colleges for each day of week
with open('ids.csv', newline='') as csvfile3: 
	rows = csv.reader(csvfile3, delimiter=',')
	for row in rows: 
		if (row[0]) not in dictionary: 
			dictionary[(row[0])] = [[], [], [], [], [], [], []]

#go through sleep data and read into dictionary
with open('sleep_data.csv', newline='') as csvfile:
	rows = csv.reader(csvfile, delimiter=',')
	for row in rows:
		if ("day" not in row):
			dictionary[(row[2])][int(row[1])].append(row[4])

#for each student in the dictionary, find most common college for each day 
for item in dictionary:
	for num in range(7):
		try:
			dictionary[item][num] = statistics.mode(dictionary[item][num])
		except StatisticsError:
			dictionary[item][num] = "error_marker"

#go through dictionary, for each student with a non homogenous sleep schedule without errors
for item in dictionary: 

	#Check if schedule is homogenous 
	if (((((((dictionary[item][0] == dictionary[item][1]) and (dictionary[item][0] == dictionary[item][2])) and (dictionary[item][0] == dictionary[item][3])) and (dictionary[item][0] == dictionary[item][4])) and (dictionary[item][0] == dictionary[item][5])) and (dictionary[item][0] == dictionary[item][6]))):
		
		#do nothing if homogenous 
		p = 1

	#if error in finding most common college each night
	elif ("error_marker" in dictionary[item]): 

		#do nothing 
		p = 1

	#check all other items in dictionary for match
	else: 
		for other_item in dictionary: 
			if ((item != other_item) and (dictionary[item] == dictionary[other_item])):
				print("Student " + item + " and Student " + other_item + ":")
				number =  0
				for college_num in dictionary[other_item]: 
					print(days_of_week_list[number] + ": " + college_dictionary[college_num])
					number += 1
			
#output
#Student 3398615277913271 and Student 7960088203188404:
#Sunday: Pauli Murray
#Monday: Pauli Murray
#Tuesday: Pauli Murray
#Wednesday: Pauli Murray
#Thursday: Pauli Murray
#Friday: Davenport
#Saturday: Pauli Murray
#Student 0765962408196153 and Student 3124439410410272:
#Sunday: Grace Hopper
#Monday: Grace Hopper
#Tuesday: Grace Hopper
#Wednesday: Grace Hopper
#Thursday: Grace Hopper
#Friday: Branford
#Saturday: Grace Hopper
#Student 3124439410410272 and Student 0765962408196153:
#Sunday: Grace Hopper
#Monday: Grace Hopper
#Tuesday: Grace Hopper
#Wednesday: Grace Hopper
#Thursday: Grace Hopper
#Friday: Branford
#Saturday: Grace Hopper
#Student 5830128969325564 and Student 2354406661737117:
#Sunday: Benjamin Franklin
#Monday: Benjamin Franklin
#Tuesday: Benjamin Franklin
#Wednesday: Johnathan Edwards
#Thursday: Benjamin Franklin
#Friday: Benjamin Franklin
#Saturday: Benjamin Franklin
#Student 4924217780685219 and Student 8443468076449460:
#Sunday: Saybrook
#Monday: Saybrook
#Tuesday: Pauli Murray
#Wednesday: Saybrook
#Thursday: Pauli Murray
#Friday: Saybrook
#Saturday: Saybrook
#Student 2354406661737117 and Student 5830128969325564:
#Sunday: Benjamin Franklin
#Monday: Benjamin Franklin
#Tuesday: Benjamin Franklin
#Wednesday: Johnathan Edwards
#Thursday: Benjamin Franklin
#Friday: Benjamin Franklin
#Saturday: Benjamin Franklin
#Student 3744572510273101 and Student 9411194630318190:
#Sunday: Trumbull
#Monday: Trumbull
#Tuesday: Trumbull
#Wednesday: Saybrook
#Thursday: Trumbull
#Friday: Trumbull
#Saturday: Trumbull
#Student 7960088203188404 and Student 3398615277913271:
#Sunday: Pauli Murray
#Monday: Pauli Murray
#Tuesday: Pauli Murray
#Wednesday: Pauli Murray
#Thursday: Pauli Murray
#Friday: Davenport
#Saturday: Pauli Murray
#Student 4277638156313387 and Student 0453479941811688:
#Sunday: Pierson
#Monday: Pierson
#Tuesday: Trumbull
#Wednesday: Pierson
#Thursday: Pierson
#Friday: Pierson
#Saturday: Pierson
#Student 5279368555596210 and Student 6894568629444131:
#Sunday: Pierson
#Monday: Pierson
#Tuesday: Grace Hopper
#Wednesday: Pierson
#Thursday: Pierson
#Friday: Pierson
#Saturday: Pierson
#Student 0453479941811688 and Student 4277638156313387:
#Sunday: Pierson
#Monday: Pierson
#Tuesday: Trumbull
#Wednesday: Pierson
#Thursday: Pierson
#Friday: Pierson
#Saturday: Pierson
#Student 9411194630318190 and Student 3744572510273101:
#Sunday: Trumbull
#Monday: Trumbull
#Tuesday: Trumbull
#Wednesday: Saybrook
#Thursday: Trumbull
#Friday: Trumbull
#Saturday: Trumbull
#Student 6894568629444131 and Student 5279368555596210:
#Sunday: Pierson
#Monday: Pierson
#Tuesday: Grace Hopper
#Wednesday: Pierson
#Thursday: Pierson
#Friday: Pierson
#Saturday: Pierson
#Student 8443468076449460 and Student 4924217780685219:
#Sunday: Saybrook
#Monday: Saybrook
#Tuesday: Pauli Murray
#Wednesday: Saybrook
#Thursday: Pauli Murray
#Friday: Saybrook
#Saturday: Saybrook