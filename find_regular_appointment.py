#!/usr/bin/env python3

import csv
import statistics
from statistics import mode, StatisticsError
#building_codes.csv -- id,code,name
#meal_plan.csv -- student_id,on_meal_plan
#door_data.csv -- day,day_of_week,student_id,time_of_day,building,is_dining_hall,is_book_return
#Yale health center is building 79

#regular appointment data: day, day_of_week, id,  time_of_day, 

#only needs to run once, gets all data for Yale Health
#
#with open('regular_appointment_data.csv', 'w+', newline='') as csvfile_write:
#	healthcenter_datafile = csv.writer(csvfile_write, delimiter=',')
#	with open('door_data.csv', newline='') as csvfile:
#		row_numb = 0
#		csv_reader = csv.reader(csvfile, delimiter=',')
#		for row in csv_reader: 
#			if row_numb != 0: 
#				if int(row[4]) == 79: 
#					healthcenter_datafile.writerow([row[0], row[1], row[2], row[3]])
#			row_numb += 1

#go throuh all yale health swipes and find students with more than 15 appointments in 150 days

#reads from regular_appointment_data
with open('regular_appointment_data.csv', newline='') as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=',')

	#writes to common data
	with open('common_data.csv', 'w+', newline='') as csvfile_write:
		common_data = csv.writer(csvfile_write, delimiter=',')	
		row_numb = 0
		id_list = []
		data = []

		#for each row, put data into data list and id into id list
		for row in csv_reader:
			data.append(row[1] + ',' + row[2]+ ',' + row[3])
			if (str(row[2]) not in id_list):
				id_list.append(str(row[2]))

		common_ids_list = []
		count = 0

		#go through ids and find how many times they appear in data 
		for one_id in id_list:
			id_count = 0
			for item in data: 
				if (str(one_id) in item): 
					id_count += 1

			#update user on progress
			if ((count % 500) == 0): 
				print(count)
			count += 1

			#if more than 15 appointments, write to common_data 
			if id_count >= 15: 
				common_data.writerow([one_id])

with open('common_data.csv', newline='') as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=',')

	#for each common id, 
	for row in csv_reader: 
		indicator = 0
		day_of_week = "undetermined"
		time = -1
		count = 0

		#go through data and check that all appointments are on same day within 30 min of the first 	
		for item in data: 
			if (str(row[0]) in item):

				#set day of week as the day of the first appointment 
				if day_of_week in "undetermined":
					day_of_week = item[0]

				#if correct day of week
				elif day_of_week in item[0]:
					counter = 0

					#get the time value from data, its the last before the comma
					while (item[len(item) - counter - 1] != ","):
						counter += 1

					#if time unset, set to time
					if time == -1: 
						time = int(item[-counter:])

					#check that time of appointment within 30 of first appointment
					elif (abs(time - int(item[-counter:]))) > 30:
						indicator  = 1
				else: 
					indicator = 1
		#if all appointments within 30 min of first and on same day of week, print row
		if indicator == 0: 
			print(row)

		
		
		
#output
#['7064193937378363']
#['4970873044120770']
#['5642901552002242']
#['3646888760367497']
#['8704172927663738']
#['2999988181898127']
#['8602602593368803']
#['3707268603642004']
#['6008825809400674']
#['5483539856817792']
#['0728408042980297']
#['5304889966484416']
#['6838803552845752']
#['0174656961500874']
#['6615964339958608']
#['7868066743254030']
#['5911462606958356']
#['5323175087784566']
#['5990397828127416']
#['4683470155633945']
#['3562197797260962']
#['7558390090488381']
#['7902357357148089']
#['4744477292616350']
#['0541223934701438']
#['1982709747295420']
#['0797640369431324']
#['8840658962693015']
#['5602831021018673']
#['8307027841608002']
#['7134356017248502']
#['9407480710573348']
#['2636115210517086']
#['6443255918798555']
#['0582759162013126']
#['2493511992683450']
#['7185421670447004']
#['4088151815501921']
#['1701396991357933']
#['4840798488378537']
#['4920886784283651']
#['9509467977208638']
#['5694667011900575']
#['4863250415328962']
#['8297869842790162']
#['3334039999949602']
#['0874792266543693']
#['0471682166371871']
#['9735741845719650']
#['1789416227803547']
#['5827790684809994']
#['0714865390203900']
#['2505225545221038']
#['1375427874518826']
#['1897587018659930']
#['9486380687958501']
#['7504014474762397']
#['7858330027647042']
#['3691342209443546']
#['5024715604738177']
#['2290229445057796']
#['3783578027935621']
#['5515551747399247']
#['5433431394048620']
#['8532530862220945']
#['8332281154527024']
#['3041427612454569']
#['3596070461975954']
#['9692177217832196']
#['3728951300091609']
#['2417577269519170']
#['6776098934598586']
#['2585945057960195']
#['8989380134255799']
#['6055221573566957']
#['3143100254255415']
#['1514879491251753']
#['9613698114601207']
#['1980748486427145']
#['4159350164382452']
#['5765086297362983']
#['2133763195278562']
#['5410448772880588']
#['1950288529357290']
#['4560764709545811']
#['5713267921592207']
#['2746060900876875']
#['9159395569508355']