#!/usr/bin/env python3

import csv

#building_codes.csv -- id,code,name
#meal_plan.csv -- student_id,on_meal_plan
#door_data.csv -- day,day_of_week,student_id,time_of_day,building,is_dining_hall,is_book_return

#load ids into dictionary
dictionary = {}
with open('meal_plan.csv', newline='') as csvfile:
	row_numb = 0
	csv_reader = csv.reader(csvfile, delimiter=',')
	for row in csv_reader:
		if (row_numb != 0):
			if ('1' in row[1]):
				dictionary[int(row[0])] = 0
		row_numb += 1
		
# count total meals for each student in door_data
with open('door_data.csv', newline='') as csvfile:
	row_numb = 0  
	csv_reader = csv.reader(csvfile, delimiter=',')
	for row in csv_reader: 

		#if not first row with headers
		if (row_numb != 0):
			if ((int(row[2])) in dictionary): 

				#add is_dining_hall to dictionary value of student_id 
				dictionary[int(row[2])] += int(row[5])
		row_numb += 1

		#print average meal swipes for each student with less than half 		
for student in dictionary: 
	if (dictionary[student] < 150): 
		print("Student " + str(student) + ": " + str(round(dictionary[student]*(7/150), 2)) + " meal swipes per week on average.")


# write email to student if they are using less than half their swipes
def write_email(student_id):

	#open meal_plan info file 
	with open('meal_plan.csv', newline='') as csvfile:
		csv_reader = csv.reader(csvfile, delimiter=',')
		row_numb = 0
		on_meal_plan = ""
		for row in csv_reader:
			if (row_numb != 0):
				if (student_id in row[0]):
					on_meal_plan = row[1]
			row_numb += 1

		#check that student is on meal plan
		if '0' in on_meal_plan: 
			print("student is not on the meal plan")
		elif ("" == on_meal_plan): 
			print("could not find student's information")
		else: 

			#count meals used 
			meals = 0
			with open('door_data.csv', newline='') as csvfile:
				row_numb = 0  
				csv_reader = csv.reader(csvfile, delimiter=',')
				for row in csv_reader: 
					if (row_numb != 0):
						if (student_id in row[2]):
							meals += int(row[5])
					row_numb += 1

		#if using dictionary made above: 
		#meals = dictionary[student_id]

		#write out email if they are using less than half their meal swipes 
		if (meals < 150):
			print("Dear " + student_id +", ")
			print("You are only using " + str(round(meals*(7/150), 2)) + " of your allotted meals each week.")
			print("")
			print("Sincerely,")
			print("Yale Dining")

write_email('7143237956228680')


# output
#Student 413639203815084: 6.63 meal swipes per week on average.
#Student 854526278940819: 6.39 meal swipes per week on average.
#Student 950585023932070: 6.72 meal swipes per week on average.
#Student 1197594711925368: 6.77 meal swipes per week on average.
#Student 1415256273860564: 6.95 meal swipes per week on average.
#Student 1607679593398219: 6.58 meal swipes per week on average.
#Student 1659016036322956: 6.72 meal swipes per week on average.
#Student 1702409818414424: 6.77 meal swipes per week on average.
#Student 1760494252604426: 6.39 meal swipes per week on average.
#Student 1789958435731915: 6.72 meal swipes per week on average.
#Student 1843480679211333: 6.86 meal swipes per week on average.
#Student 2119869385138211: 6.95 meal swipes per week on average.
#Student 2166181051177116: 6.81 meal swipes per week on average.
#Student 2293755628694343: 6.21 meal swipes per week on average.
#Student 2467404677673916: 6.91 meal swipes per week on average.
#Student 2525195466903999: 6.63 meal swipes per week on average.
#Student 2758954834434972: 6.72 meal swipes per week on average.
#Student 3497908280079933: 6.91 meal swipes per week on average.
#Student 3585702068270764: 6.81 meal swipes per week on average.
#Student 3624623047388877: 6.77 meal swipes per week on average.
#Student 3682129876662973: 6.35 meal swipes per week on average.
#Student 4039754957251485: 6.67 meal swipes per week on average.
#Student 4051728865937478: 6.72 meal swipes per week on average.
#Student 4470328737801842: 6.86 meal swipes per week on average.
#Student 4537735250209802: 6.67 meal swipes per week on average.
#Student 4662672447652388: 6.81 meal swipes per week on average.
#Student 4825006937801939: 6.86 meal swipes per week on average.
#Student 4828900067093876: 6.67 meal swipes per week on average.
#Student 4847813885855762: 6.67 meal swipes per week on average.
#Student 4979793893191145: 6.58 meal swipes per week on average.
#Student 5001074945607777: 6.25 meal swipes per week on average.
#Student 5028638763669296: 6.81 meal swipes per week on average.
#Student 5088719612763739: 6.72 meal swipes per week on average.
#Student 5121661048165188: 6.58 meal swipes per week on average.
#Student 5287869467529300: 6.58 meal swipes per week on average.
#Student 5311725888489624: 6.81 meal swipes per week on average.
#Student 5349646765474341: 6.49 meal swipes per week on average.
#Student 5999321198590986: 6.81 meal swipes per week on average.
#Student 6001177683882402: 6.39 meal swipes per week on average.
#Student 6189777486395250: 6.95 meal swipes per week on average.
#Student 6545698764511064: 6.77 meal swipes per week on average.
#Student 6605135558573565: 6.95 meal swipes per week on average.
#Student 7143237956228680: 6.3 meal swipes per week on average.
#Student 7186589740594251: 6.95 meal swipes per week on average.
#Student 7279283848355366: 6.91 meal swipes per week on average.
#Student 7335417764710635: 6.16 meal swipes per week on average.
#Student 7399531960551992: 6.77 meal swipes per week on average.
#Student 7527212914978325: 6.77 meal swipes per week on average.
#Student 7550092799426684: 6.39 meal swipes per week on average.
#Student 7731812176114420: 6.95 meal swipes per week on average.
#Student 7761022817855619: 6.86 meal swipes per week on average.
#Student 8021300076153295: 6.49 meal swipes per week on average.
#Student 8226353467075582: 6.95 meal swipes per week on average.
#Student 8390931974121376: 6.67 meal swipes per week on average.
#Student 8417045442631509: 6.44 meal swipes per week on average.
#Student 8458537847262277: 6.58 meal swipes per week on average.
#Student 8670053401081190: 6.81 meal swipes per week on average.
#Student 9134829679044759: 6.58 meal swipes per week on average.
#Student 9181632378279189: 6.53 meal swipes per week on average.
#Student 9186290814779485: 6.53 meal swipes per week on average.
#Student 9326103814869278: 6.39 meal swipes per week on average.
#Student 9341565932803415: 6.86 meal swipes per week on average.
#Student 9384900576443370: 6.86 meal swipes per week on average.
#Student 9408236755028183: 6.91 meal swipes per week on average.
#Student 9527097467562136: 6.39 meal swipes per week on average.
#Student 9773030952641562: 6.53 meal swipes per week on average.
#Student 9773799258375465: 6.63 meal swipes per week on average.
#Student 9834663205122834: 6.72 meal swipes per week on average.
#Student 9880998863856542: 6.81 meal swipes per week on average.
#Student 9943757051741934: 6.91 meal swipes per week on average.
#
#Dear 7143237956228680,
#You are only using 6.3 of your allotted meals each week.
#
#Sincerely,
#Yale Dining