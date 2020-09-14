#!/usr/bin/env python3

#building_codes.csv -- id,code,name
#meal_plan.csv -- student_id,on_meal_plan
#door_data.csv -- day,day_of_week,student_id,time_of_day,building,is_dining_hall,is_book_return

# transform data into daily volumes, the number of people who enter the library each day 
# day, number of people who enter, number of people who return (Bass and then law library each)

import csv

#make a file with a list of ids for later use in nearest neighbors
with open('ids.csv', 'w+', newline='') as csvfile_write2:
	ids_datafile = csv.writer(csvfile_write2, delimiter=',')


	#make library_data to store data about library use 
	with open('library_data.csv', 'w+', newline='') as csvfile_write:
		library_datafile = csv.writer(csvfile_write, delimiter=',')    

		#open door_data.csv
		with open('door_data.csv', newline='') as csvfile:
			csv_reader = csv.reader(csvfile, delimiter=',')
			row_numb = 0
			day = 0
			ids = {}
			bass_return = 0
			bass_enter = 0
			lawlib_enter = 0 
			lawlib_return = 0
			previous_day = 0
			for row in csv_reader:
				if row_numb == 0:

					#do nothing
					p = 1
				else: 

					#write id into id_datafile
					if row[2] not in ids: 
						ids_datafile.writerow([row[2]])
						ids[(row[2])] = 1
					day = int(row[0])
					if day == previous_day: 

						# if havent changed day, add to both entered and returned counters if before 6pm
						if (1080 > int(row[3])):
							if int(row[4]) == 80: 
								lawlib_enter += 1
								lawlib_return += int(row[6])
							elif int(row[4]) == 3: 
								bass_enter += 1
								bass_return += int(row[6])

						# if after 6pm, just add to returned counter because we are using entered before 6pm as the predictor
						else: 
							if int(row[4]) == 80: 
								lawlib_return += int(row[6])
							elif int(row[4]) == 3: 
								bass_return += int(row[6])

					#if new day, write counters into library datafile for decision trees
					else: 
						library_datafile.writerow([str(day-1), str((day-1) % 7), str(bass_enter), str(bass_return), str(lawlib_enter), str(lawlib_return)])
						
						#reset counters
						bass_enter = 0
						bass_return = 0
						lawlib_enter = 0 
						lawlib_return = 0
					previous_day = day
				row_numb += 1
			
			#write last line
			library_datafile.writerow([str(day), str(int(row[1])), str(bass_enter), str(bass_return), str(lawlib_enter), str(lawlib_return)])
				
