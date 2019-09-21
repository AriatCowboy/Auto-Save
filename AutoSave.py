import pickle
import os
import shutil
import glob
import time
import datetime
#-------------This is Variable Section for Main Variables----------------
#The following variables are about our program
Author = 'AriatCowboy'
Co_Author = 'Razor1397'
Title = "Ghost Mode Auto-Saver"
ProgramName = 'AutoSave.py'
ReleaseDate = 'Sunday, October 21, 2018 10:54'
Version = 'v2'
ToStop = 'To Stop Press CTRL + C'
#Below are some other variables created for the program to work
#answers_file will include Dir locations
answers_file = 'userinfo.dat'
#config_file will include timers and cylcle numbers
savegames_file = 'savegames.dat'
uplay_id_file = 'uplay_id.dat'
script_location_file = 'script_location.dat'
backup_timer_file = 'backup_timer.dat'
death_check_timer_file = 'death_check_timer.dat'
cycle_num_file = 'cycle_num.dat'
debug_file = 'debug.dat'
'''
VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
THIS IS VERY IMPORTANT FOR EVERYTHING TO WORK
VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
toggleing things true and reading the file when its important
basically allowing overide on line 61 and move whats there down and place: '''
reset_file = 'reset.dat'
#--------------------------Script Starts Here--------------------------
#--------------------------Functions are created here--------------------------------
#Functions are mini scripts
#--------------------------initial_start Starts here---------------------------------
#initial_start just gathers information about the system its running un throught the End-User
#This Initial start begins asking information about save locations OR gathers the data from the file created on a previous launch

def initial_start():
	#Here we need to get the savegames folder, uplay id, back up location, script location, back up timer, death check timer, save cycles
	if not os.path.isfile(savegames_file):
		savegames_folder()          
def savegames_folder():
	savegames_folder = ''
	while savegames_folder == '':
		savegames_folder = input('What is your savegames folder?\nWhere you installed Uplay, it could look like this:\nC:\\UPlay\\Ubisoft Game Launcher\\savegames\n\n')
		if os.path.isdir(savegames_folder):
			clear_screan()
			confirm = ''
			while confirm == '':
				confirm = input('Are you sure you want to set the following address as your savegames folder? \n' + savegames_folder + '\n\nType y or n. \n')
				clear_screan()
				if confirm == 'y':
					write_savegames = open(savegames_file, "wb")
					with write_savegames as wsg:
						savegames_folder = {1:savegames_folder}
						pickle.dump(savegames_folder, wsg)
					if os.path.isfile(reset_file):
						reset = read_reset_file()
						if reset[1] == True:
							os.remove(reset_file)
							pre_main_menu()
					if not os.path.isfile(uplay_id_file):
						uplay_id()
				elif confirm == 'n':
					clear_screan()
					confirm = ''
				else:
					clear_screan()
					print('dont headbut your keyboard!!!!\n\n')
					confirm = ''
		else:
			clear_screan()
			print('That was not a valid entry! Please Try Again\n\n')
			savegames_folder = ''
def uplay_id():
	savegames_folder = read_savegames_file()
	uplay_id = ''
	while uplay_id == '':
		uplay_id = input('what is your Uplay ID\nIt should look like this\n7f1cd098-####-####-####-55bea3c43694\nclick 2 times fairly slow and copy the folder name\n\n')
		check_id = savegames_folder[1] + '\\' + uplay_id
		clear_screan()
		if os.path.isdir(check_id):
			print('You entered the following ID:\n\n' + uplay_id)
			write_uplay_id = open(uplay_id_file, "wb")
			with write_uplay_id as wupid:
				uplay_id = {1:uplay_id}
				pickle.dump(uplay_id, wupid)
			if os.path.isfile(reset_file):
				reset = read_reset_file()
				if reset[1] == True:
					os.remove(reset_file)
			if not os.path.isfile(script_location_file):
				script_location()
		else:
			clear_screan()
			print('The ID ' + uplay_id + ' does not exist!!')
			uplay_id = ''
def script_location():
	script_location = ''
	while script_location == '':
		script_location = input('What is the file location for ' + Title + '\n\n')
		mod_script_location = script_location + '\\' + ProgramName
		if os.path.isfile(mod_script_location):
			write_script_location = open(script_location_file, "wb")
			with write_script_location as wsl:
				script_location = {1:script_location}
				pickle.dump(script_location, wsl)
			if os.path.isfile(reset_file):
				reset = read_reset_file()
				if reset[1] == True:
					os.remove(reset_file)
					clear_screan()
					pre_main_menu()
			if not os.path.isfile(backup_timer_file):
				backup_timer()
		elif not os.path.isfile(mod_script_location):
			clear_screan()
			print('The path you entered is not valid.\n')
			script_location = ''
		else:
			clear_screan()
			print('You entered a invalid entry!\n')
			script_location = ''
def backup_timer():
	backup_timer = ''
	while backup_timer == '':
		clear_screan()
		backup_timer = input('How often would you like ' + ProgramName + ' to make a backup of your save?\n\n')
		try:
			backup_timer = float(backup_timer)
			write_backup_timer = open(backup_timer_file, "wb")
			backup_timer = backup_timer * 60 
			with write_backup_timer as wbut:
				backup_timer = {1:backup_timer}
				pickle.dump(backup_timer, wbut)
			if os.path.isfile(reset_file):
				reset = read_reset_file()
				if reset[1] == True:
					os.remove(reset_file)
					clear_screan()
					pre_main_menu()
			else:
				clear_screan()
				death_check_timer()
		except ValueError:
			clear_screan()
			print('Please enter a number!\n\n')
			backup_timer = ''
def death_check_timer():
	death_check_timer = ''
	while death_check_timer == '':
		clear_screan()
		death_check_timer = input('How often would you like ' + ProgramName + ' to check if you have died?\n\n')
		try:
			death_check_timer = float(death_check_timer)
			write_death_check_timer = open(death_check_timer_file, "wb")
			death_check_timer = death_check_timer * 60 
			with write_death_check_timer as wdct:
				death_check_timer = {1:death_check_timer}
				pickle.dump(death_check_timer, wdct)
			if os.path.isfile(reset_file):
				reset = read_reset_file()
				if reset[1] == True:
					os.remove(reset_file)
					clear_screan()
					pre_main_menu()
			else:
				clear_screan()
				cycle_num()
		except ValueError:
			clear_screan()
			print('Please enter a number!\n\n')
def cycle_num():
	cycle_num = str(0)
	write_cycle_num = open(cycle_num_file, "wb")
	with write_cycle_num as wcn:
		cycle_num = {1:cycle_num}
		pickle.dump(cycle_num, wcn)
		if os.path.isfile(reset_file):
			reset = read_reset_file()
			if reset[1] == True:
				os.remove(reset_file)
				pre_main_menu()
#-----------------------------Read File Functions are here------------------------------
def read_savegames_file():
	read_savegames = open(savegames_file, "rb")
	with read_savegames as rsg:
		savegames_folder = pickle.load(read_savegames)
		return savegames_folder
def read_uplay_id_file():
	read_uplay_id = open(uplay_id_file, "rb")
	with read_uplay_id as rupid:
		uplay_id = pickle.load(read_uplay_id)
		return uplay_id
def read_script_location_file():
	read_script_location = open(script_location_file, "rb")
	with read_script_location as rsl:
		script_location = pickle.load(read_script_location)
		return script_location
def read_backup_timer_file():
	read_backup_timer = open(backup_timer_file, "rb")
	with read_backup_timer as rbut:
		backup_timer = pickle.load(read_backup_timer)
		return backup_timer
def read_death_check_timer_file():
	read_death_check_timer = open(death_check_timer_file, "rb")
	with read_death_check_timer as rdct:
		death_check_timer = pickle.load(read_death_check_timer)
		return death_check_timer
def read_answers_file():
	read_answers = open(answers_file, "rb")
	with read_answers as ra:
		answers = pickle.load(read_answers)
		return answers
def read_reset_file():
	read_reset = open(reset_file, "rb")
	with read_reset as rr:
		reset = pickle.load(read_reset)
		return reset
def read_debug_file():
	read_debug = open(debug_file, "rb")
	with read_debug as rdb:
		debug = pickle.load(read_debug)
		return debug
def read_cycle_num_file():
	read_cycle_num = open(cycle_num_file, "rb")
	with read_cycle_num as rcn:
		cycle_num = pickle.load(read_cycle_num)
		return cycle_num
def write_reset():
	reset = bool(True)
	write_reset = open(reset_file, "wb")
	with write_reset as wr:
		reset = {1:reset}
		pickle.dump(reset, wr)
def pre_main_menu():
	backup_folder = '\\backup'
	if not os.path.isfile(answers_file):
		savegames_folder = read_savegames_file()
		uplay_id = read_uplay_id_file()
		script_location = read_script_location_file()
		backup_timer = read_backup_timer_file()
		death_check_timer = read_death_check_timer_file()
		cycle_num = read_cycle_num_file()
		backup_folder = script_location[1] + backup_folder
		while not os.path.exists(backup_folder):
			os.mkdir(backup_folder)
		write_answers = open(answers_file, "wb")
		with write_answers as wa:
			answers = {1:savegames_folder[1], 2:uplay_id[1], 3:script_location[1], 4:backup_timer[1], 5:death_check_timer[1], 6:cycle_num[1], 7:backup_folder}
			pickle.dump(answers, wa)
	else:
		answers = read_answers_file()
		time.sleep(.01)
		if os.path.isfile(answers_file):
			savegames_fix = answers[1]
			uplay_id_fix = answers[2]
			script_location_fix = answers[3]
			backup_timer_fix = answers[4]
			death_check_timer_fix = answers[5]
			cycle_num_fix = answers[6]
			time.sleep(.01)
		if os.path.isfile(savegames_file):
			savegames_folder = read_savegames_file()
			savegames_fix = savegames_folder[1]
			time.sleep(.01)
		if os.path.isfile(uplay_id_file):
			uplay_id = read_uplay_id_file()
			uplay_id_fix = uplay_id[1]
			time.sleep(.01)
		if os.path.isfile(script_location_file):
			script_location = read_script_location_file()
			script_location_fix = script_location[1]
			time.sleep(.01)
		if os.path.isfile(backup_timer_file):
			backup_timer = read_backup_timer_file()
			backup_timer_fix = backup_timer[1]
			time.sleep(.01)
		if os.path.isfile(death_check_timer_file):
			death_check_timer = read_death_check_timer_file()
			death_check_timer_fix = death_check_timer[1]
			time.sleep(.01)
		if os.path.isfile(cycle_num_file):
			cycle_num = read_cycle_num_file()
			cycle_num_fix = cycle_num[1]
			time.sleep(.01)
		if os.path.isfile(answers_file):
			os.remove(answers_file)
			time.sleep(.01)
		backup_folder = script_location_fix + backup_folder
		while not os.path.exists(backup_folder):
			os.mkdir(backup_folder)
		write_answers = open(answers_file, "wb")
		with write_answers as wa:
			answers = {1:savegames_fix, 2:uplay_id_fix, 3:script_location_fix, 4:backup_timer_fix, 5:death_check_timer_fix, 6:cycle_num_fix, 7:backup_folder}
			pickle.dump(answers, wa)
	if os.path.isfile(answers_file):
		if os.path.exists(savegames_file):
			os.remove(savegames_file)
			time.sleep(.1)
		if os.path.exists(uplay_id_file):
			os.remove(uplay_id_file)
			time.sleep(.1)
		if os.path.exists(script_location_file):
			os.remove(script_location_file)
			time.sleep(.1)
		if os.path.exists(backup_timer_file):
			os.remove(backup_timer_file)
			time.sleep(.1)
		if os.path.exists(death_check_timer_file):
			os.remove(death_check_timer_file)
			time.sleep(.1)
		if os.path.exists(reset_file):
			os.remove(reset_file)
			time.sleep(.1)
		if os.path.exists(cycle_num_file):
			os.remove(cycle_num_file)
			time.sleep(.1)
	main_menu()
def debug_menu():
	clear_screan()
	debug = read_debug_file()
	answers = read_answers_file()
	answers4 = str(answers[4])
	answers5 = str(answers[5])
	answers6 = str(answers[6])
	print('Your savegames directory is:\n' + answers[1] + '\n\nYour uplay ID is:\n' + answers[2] + '\n\nThe directory ' + ProgramName + ' is located is:\n' + answers[3] + '\n\nYour backup folder is located at:\n' + answers[7] + '\n\nYou have it set to save every:\n' + answers4 + ' seconds' + '\n\nYou have ' + ProgramName + ' to check every:\n' + answers5 + ' seconds' + '\n\nThe save cycle you are on is set to:\n' + answers6)
	if debug[1] == True:
		debug = bool(False)
		os.remove(debug_file)
	elif debug[1] == False:
		debug = bool(True)
	write_debug = open(debug_file, "wb")
	with write_debug as wdb:
		debug = {1:debug}
		pickle.dump(debug, wdb)
	main_menu()
def main_menu():
	menu_option = ''
	while menu_option == '':
		print('\nMain Menu\n')
		print('[1] Continuous Backups')
		print('[2] Continuous Backups with periodic death checks')
		print('[3] Make a copy and 1 additional back up')
		print('[4] Make a copy and 1 additional back up with periodic death checks')
		print('[5] Make 1 copy only')
		print('[6] Options')
		print('[7] Quit')
		menu_option = input('\nPlease Select an Option!\n\n')
		if menu_option == '1':
			clear_screan()
			selection_one()
		elif menu_option == '2':
			clear_screan()
			selection_two()
		elif menu_option == '3':
			clear_screan()
			selection_three()
		elif menu_option == '4':
			clear_screan()
			selection_four()
		elif menu_option == '5':
			clear_screan()
			selection_five()
		elif menu_option == '6':
			clear_screan()
			options()
		elif menu_option == '7':
			quit()
		elif menu_option == '911':
			debug_menu()
		elif menu_option == '1397':
			clear_screan()
			print('You sly dog you ;D')
			time.sleep(3)
			clear_screan()
			menu_option = ''
		else:
			clear_screan()
			print('You entered a invalid option!')
def upload_backup():
	answers = read_answers_file()
	#below gets user input on whether they want to continue with the file or find a new one.
	upload_file_answer = ''
	file = answers[7]
	files_path = os.path.join(file, '*')
	files_list = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
	root_src = files_list[0]
	while upload_file_answer != 'y':
		print(root_src, '\nWhich was created on\n', time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(os.path.getmtime(root_src))))
		upload_file_answer = input('Do you want to use this file? Type y or n.\n')
		if upload_file_answer == 'y':
			confirm = ''
			while confirm != 'y':
				clear_screan()
				print(root_src, '\nWhich was created on\n', time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(os.path.getmtime(root_src))))
				confirm = input('Are you sure you want to use this save?\ny or n.\n\n')
				if confirm == 'y':
					root_dst = answers[1] + '\\' + answers[2]
					for src_dir, dirs, files in os.walk(root_src):
						dst_dir = src_dir.replace(root_src, root_dst, 1)
					if not os.path.exists(dst_dir):
						os.makedirs(dst_dir)
					for file_ in files:
						print('file uploaded at:', time.strftime("%m/%d/%Y %I:%M:%S %p"))
						src_file = os.path.join(src_dir, file_)
						dst_file = os.path.join(dst_dir, file_)
						if os.path.exists(dst_file):
							os.remove(dst_file)
						shutil.copy(src_file, dst_dir)
					print('Your Backup was placed!')
					main_menu()
				elif confirm == 'n':
					confirm = 'y'
					upload_file_answer = 'y'
					clear_screan()
					upload_backup()
				else:
					confirm = ''
					clear_screan()
					print('You entered a invanlid entry.')
		elif upload_file_answer == 'n':
			delete_for_user = ''
			upload_file_answer = ''
			while delete_for_user != 'y':
				delete_for_user = input('Would you like me to delete it for you?\nType y or n.\n')
				if delete_for_user == 'y':
					shutil.rmtree(root_src)
					upload_backup()
					clear_screan()
					delete_for_user = ''
					upload_file_answer = ''
				elif delete_for_user == 'n':
					clear_screan()
					files.pop(0)
					delete_for_user = ''
					upload_file_answer = ''
				else:
					clear_screan()
					print('There were no other files.\n')
					delete_for_user = 'y'
					main_menu()
		else:
			clear_screan()
			print('Stop Cheating if you know whats good for you.')
			upload_file_answer = ''
def make_save():
	answers = read_answers_file()
	for src_dir, dirs, files in os.walk(answers[1]):
		dst_dir = src_dir.replace(answers[1], answers[7], 1)
		if not os.path.exists(dst_dir):
			os.makedirs(dst_dir)
		for file_ in files:
			src_file = os.path.join(src_dir, file_)
			dst_file = os.path.join(dst_dir, file_)
			if os.path.exists(dst_file):
				os.remove(dst_file)
			shutil.copy(src_file, dst_dir)
def make_backup():
	answers = read_answers_file()
	root_copy = answers[7] + '\\' + answers[2]
	root_backup = root_copy + '_BAK' 
	for src_dir, dirs, files in os.walk(root_copy):
		dst_dir = src_dir.replace(root_copy, root_backup, 1)
		if not os.path.exists(dst_dir):
			os.makedirs(dst_dir)
		for file_ in files:
			src_file = os.path.join(src_dir, file_)
			dst_file = os.path.join(dst_dir, file_)
			if os.path.exists(dst_file):
				os.remove(dst_file)
			shutil.copy(src_file, dst_dir)
def make_cycle_backup():
	answers = read_answers_file()
	cycle_num = answers[6]
	root_copy = answers[7] + '\\' + answers[2]
	cycle_num_as_str = str(cycle_num)
	root_backup = root_copy + ' ' + cycle_num_as_str
	for src_dir, dirs, files in os.walk(root_copy):
		dst_dir = src_dir.replace(root_copy, root_backup, 1)
		if not os.path.exists(dst_dir):
			os.makedirs(dst_dir)
		for file_ in files:
			src_file = os.path.join(src_dir, file_)
			dst_file = os.path.join(dst_dir, file_)
			if os.path.exists(dst_file):
				os.remove(dst_file)
			shutil.copy(src_file, dst_dir)
def selection_one():
	answers = read_answers_file()
	cycle_num = answers[6]
	if os.path.isdir(answers[7]) and len(os.listdir(answers[7])) > 0:
		shutil.rmtree(answers[7])
		time.sleep(1)
		os.mkdir(answers[7])
	elif not os.path.isdir(answers[7]):
		os.mkdir(answers[7])
	print('You selected Option 1, Make Continuous Backups.')
	print("*** Hit CTRL+C to stop ***")
	timer = answers[4]
	selection_one = bool(True)
	while selection_one == bool(True):
		#Variables for Option 1
		root_copy = answers[7] + '\\' + answers[2]
		cycle_num_as_str = str(cycle_num)
		root_backup = root_copy + ' ' + cycle_num_as_str
		#Copy Starts here
		make_save()
		#Back up replaces copy on the next line
		make_cycle_backup()
		print("Your back up as been created on " + time.strftime("%c"))
		time.sleep(timer)
		cycle_num = int(cycle_num_as_str)
		cycle_num += 1
		os.chdir(answers[3])
		write_answers = open(answers_file, "wb")
		with write_answers as wa:
			answers = {1:answers[1], 2:answers[2], 3:answers[3], 4:answers[4], 5:answers[5], 6:cycle_num, 7:answers[7]}
			pickle.dump(answers, wa)
def selection_two():
	answers = read_answers_file()
	if os.path.isdir(answers[7]) and len(os.listdir(answers[7])) > 0:
		shutil.rmtree(answers[7])
		time.sleep(1)
		os.mkdir(answers[7])
	elif not os.path.isdir(answers[7]):
		os.mkdir(answers[7])
	print('You selected Option 2, Make Continuous Backups with periodic death checks.')
	print("*** Hit CTRL+C to stop ***")
	make_save()
	print("Your save as been created on " + time.strftime("%c"))
	selection_two_part_two()
def selection_two_part_two():
	start_time = time.time()
	answers = read_answers_file()
	cycle_num = answers[6]
	timer = answers[4]
	timer3 = answers[5]
	selection_two = bool(True)
	while selection_two == bool(True):
		#Variables for Option 2
		#Copy Starts here
		elapsed_time = time.time() - start_time
		timer3 = timer3 - elapsed_time
		if elapsed_time >= timer3:
			root_copy = answers[7] + '\\' + answers[2]
			cycle_num_as_str = str(cycle_num)
			root_backup = root_copy + ' ' + cycle_num_as_str
			timer3 = answers[5]
			death_question_selection_two()
			start_time = time.time()
			make_save()
			make_cycle_backup()
			print("Your backup as been created on " + time.strftime("%c"))
		else:
			root_copy = answers[1] + '\\' + answers[2]
			cycle_num_as_str = str(cycle_num)
			root_backup = root_copy + ' ' + cycle_num_as_str
			start_time = time.time()
			timer3 = timer3 - elapsed_time
			timer = int(timer)
			timer = round(timer, 0)
			time.sleep(timer)
			make_save()
			make_cycle_backup()
			print("Your Backup as been created on " + time.strftime("%c"))
		cycle_num = int(cycle_num_as_str)
		cycle_num += 1
		os.chdir(answers[3])
		write_answers = open(answers_file, "wb")
		with write_answers as wa:
			answers = {1:answers[1], 2:answers[2], 3:answers[3], 4:answers[4], 5:answers[5], 6:cycle_num, 7:answers[7]}
			pickle.dump(answers, wa)
def death_question_selection_two():
	death_question = ''
	while death_question != 'n':
		death_question = input('Have you died?\nType y or n.\n')
		if death_question == 'y':
			upload_backup()
		else:
			if death_question == 'n':
				pass
			else:
				clear_screan()
				print('You entered a invalid option silly!')
				death_question = ''
def selection_three():
	answers = read_answers_file()
	if os.path.isdir(answers[7]) and len(os.listdir(answers[7])) > 0:
		shutil.rmtree(answers[7])
		time.sleep(.1)
		os.mkdir(answers[7])
	elif not os.path.isdir(answers[7]):
		os.mkdir(answers[7])
		time.sleep(.1)
	timer = answers[4]
	print('You selected Option 3, Make a copy and 1 additional back up.')
	print("*** Hit CTRL+C to stop ***")
	selection_one = bool(True)
	while selection_one == bool(True):
		#Copy Starts here
		make_save()
		#Back up replaces copy on the next line
		print("Your Save has been created on " + time.strftime("%c"))
		time.sleep(timer)
		make_backup()
		print("Your Backup was created on " + time.strftime("%c"))
		time.sleep(timer)
def selection_four():
	answers = read_answers_file()
	if os.path.isdir(answers[7]) and len(os.listdir(answers[7])) > 0:
		shutil.rmtree(answers[7])
		time.sleep(.1)
		os.mkdir(answers[7])
	elif not os.path.isdir(answers[7]):
		os.mkdir(answers[7])
		time.sleep(.1)
	print('You selected Option 4, Make a copy and 1 additional back up with periodic death checks.')
	make_save()
	print("Your Save has been created on " + time.strftime("%c"))
	selection_four_part_two()
def selection_four_part_two():
	start_time = time.time()
	answers = read_answers_file()
	timer3 = answers[5]
	timer = answers[4]
	print("*** Hit CTRL+C to stop ***")
	selection_one = bool(True)
	while selection_one == bool(True):
		#Copy Starts here
		elapsed_time = time.time() - start_time
		if elapsed_time >= timer3:
			timer3 = answers[5]
			death_question_selection_two()
			start_time = time.time()
			make_save()
			print("Your Save has been created on " + time.strftime("%c"))
		else:
			start_time = time.time()
			timer3 = timer3 - elapsed_time
			timer = int(timer)
			timer = round(timer, 0)
			time.sleep(timer)
			make_save()
			print("Your Save has been created on " + time.strftime("%c"))
		elapsed_time = time.time() - start_time
		timer3 = timer3 - elapsed_time
		if elapsed_time >= timer3:
			timer3 = answers[5]
			death_question_selection_two()
			start_time = time.time()
			make_backup()
			print("Your Backup was created on " + time.strftime("%c"))
		else:
			start_time = time.time()
			timer = int(timer)
			timer = round(timer, 0)
			time.sleep(timer)
			make_backup()
			print("Your Backup was created on " + time.strftime("%c"))
def selection_five():
	print('You selected Option 5, Make 1 Backup.')
	#Copy Starts here
	make_save()
	print("Your backup as been created on " + time.strftime("%c"))
def change_settings():
	selection = ''
	while selection == '':
		print('[1] Change where you installed uplay')
		print('[2] Change stored Uplay ID')
		print('[3] Change where ' + ProgramName + ' is saved')
		print('[4] Change how often you want a save to be created')
		print('[5] Change how often you want the program to check to see if you have died')
		print('[6] Change cycle number (for those using option 1 or 2)')
		print('[7] Back to Options')
		selection = input('Which option would you like to change?\n')
		if selection == '1':
			clear_screan()
			write_reset()
			savegames_folder()
		elif selection == '2':
			clear_screan()
			write_reset()
			uplay_id()
		elif selection == '3':
			clear_screan()
			write_reset()
			script_location()
		elif selection == '4':
			clear_screan()
			write_reset()
			backup_timer()
		elif selection == '5':
			clear_screan()
			write_reset()
			death_check_timer()
		elif selection == '6':
			clear_screan()
			write_reset()
			cycle_num()
		elif selection == '7':
			clear_screan()
			options()
		else:
			clear_screan()
			selection = ''
			print('You entered an invalid entry.')
def options():
	answers = read_answers_file()
	answers4 = str(answers[4])
	answers5 = str(answers[5])
	answers6 = str(answers[6])
	selection = ''
	while selection == '':
		print('Your savegames directory is:\n' + answers[1] + '\n\nYour uplay ID is:\n' + answers[2] + '\n\nThe directory ' + ProgramName + ' is located is:\n' + answers[3] + '\n\nYour backup folder is located at:\n' + answers[7] + '\n\nYou have it set to save every:\n' + answers4 + ' seconds' + '\n\nYou have ' + ProgramName + ' to check every:\n' + answers5 + ' seconds' + '\n\nThe save cycle you are on is set to:\n' + answers6)
		print('[1] Change Settings')
		print('[2] Upload Backup')
		print('[3] Back to main menu')
		selection = input('Which option would you like to change?\n')
		if selection == '1':
			clear_screan()
			change_settings()
		elif selection == '2':
			clear_screan()
			upload_backup()
		elif selection == '3':
			clear_screan()
			main_menu()
		else:
			clear_screan()
			print('Only select one of the options, no cheating here ;D.')
			time.sleep(3)
			clear_screan()
			selection = ''
def quit():
	clear_screan()
	print('A special thanks to all those testing during the alpha stages!\nThanks, You Rock!\nOriginal Developer\nAriatCowboy')
	time.sleep(3)
def wip():
	clear_screan()
	print('This is currently under cunstruction.')
	time.sleep(3)
	main_menu()
def clear_screan():
	try:
		if os.path.isfile(debug_file):
			debug = read_debug_file()
			if debug[1] != True:
				os.system('cls')
	except NameError:
		print('I was to tired to write out a true error code, but your error happened when clearing the screan')
def default_debug():
	if not os.path.isfile(debug_file):
		debug = bool(False)
		write_debug = open(debug_file, "wb")
		with write_debug as wdb:
			debug = {1:debug}
			pickle.dump(debug, wdb)
default_debug()
clear_screan()
print('Hello, my name is ' + Author + ' and my Co-Author is ' + Co_Author +'. We would like to thank you for using ' + Title + ' ' + Version + '. The release date was ' + ReleaseDate + '. We just have a few things we need to clear up before we can start up. ' + ToStop + ' At Anytime!\n')
#Where it all starts ;D SHHH
if not os.path.isfile(answers_file):
	initial_start()
pre_main_menu()