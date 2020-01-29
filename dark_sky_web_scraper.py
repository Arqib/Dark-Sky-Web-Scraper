#!/usr/bin/env python3
"""
Documentation:
This program get weather data from darksky.net
It then uses the linux shell and python module to create weather datasets for Nyeri.
It starts from September 4th 2018.
usage : python3 web_scraper.py

"""

try:
    import sys
except Exception:
    print("[-] sys module is missing")
    # Exit in case of an error

try:
	import socket as sck
	import os
	import json
	import re
	import urllib.request
	from bs4 import BeautifulSoup
	from subprocess import run, PIPE
	import csv
	import sys
	import pandas
	import datetime
	from time import strftime
except Exception:
    print("[-] One of the modules imported is missing")
    # Exit in case of an error
    sys.exit()




WEBSITE = "www.google.com"
def darksky_available(hostname):
	try:
		host = sck.gethostbyname(hostname)
		s = sck.create_connection((host, 80), 2)
		s.close()
		print("[+] Internet available")
		return True
	except Exception:
		print("[-] Internet unavailable")
		sys.exit()
	return False

darksky_available(WEBSITE)



# date when comlete weather data from Dark Sky becomes available
start_date = "2018-9-19"

year = 2018
year2019 = 2019
month2019 = 1
#month2018 = 9
#month = 1
#day = 1

def scrape_2019_data():
	#January_2019
	January_2019 = 1; day = 1; year = 2019
	while day <= 31:
		# date = year-month-day
		date = str(year) + '-' + str(January_2019) + '-' + str(day)
		print(date)
		scraper_function(date)
		day+=1
		
	#February_2019
	February_2019 = 2; day = 1; year = 2019
	while day <= 28:
		# date = year-month-day
		date = str(year) + '-' + str(February_2019) + '-' + str(day)
		print(date)
		scraper_function(date)
		day+=1
		
	#March_2019
	March_2019 = 3; day = 1; year = 2019
	while day <= 31:
		# date = year-month-day
		date = str(year) + '-' + str(March_2019) + '-' + str(day)
		print(date)
		scraper_function(date)
		day+=1	 

	#April_2019
	April_2019 = 4; day = 1; year = 2019
	while day <= 30:
		# date = year-month-day
		date = str(year) + '-' + str(April_2019) + '-' + str(day)
		print(date)
		scraper_function(date)
		day+=1
		
	#May_2019
	May_2019 = 5; day = 1; year = 2019
	while day <= 31:
		# date = year-month-day
		date = str(year) + '-' + str(May_2019) + '-' + str(day)
		print(date)
		scraper_function(date)
		day+=1
		
	#June_2019
	June_2019 = 6; day = 1; year = 2019
	while day <= 30:
		# date = year-month-day
		date = str(year) + '-' + str(June_2019) + '-' + str(day)
		print(date)
		scraper_function(date)
		day+=1
		
	#July_2019
	July_2019 = 7; day = 1; year = 2019
	while day <= 31:
		# date = year-month-day
		date = str(year) + '-' + str(July_2019) + '-' + str(day)
		print(date)
		scraper_function(date)
		day+=1
		
	#August_2019
	August_2019 = 8; day = 1; year = 2019
	while day <= 31:
		# date = year-month-day
		date = str(year) + '-' + str(August_2019) + '-' + str(day)
		print(date)
		scraper_function(date)
		day+=1
	
	#September
	September_2019 = 9; day = 1; year = 2019
	while day <= 24:
		# date = year-month-day
		date = str(year) + '-' + str(September_2019) + '-' + str(day)
		print(date)
		scraper_function(date)
		day+=1

def scrape_2018_data():
	#September_2018
	September_2018 = 9; day = 19
	while day <= 30:
		# date = year-month-day
		date = str(year) + '-' + str(September_2018) + '-' + str(day)
		print(date)
		scraper_function(date)
		day+=1
				
	#October_2018
	October_2018 = 10; day = 1
	while day <= 31:
		# date = year-month-day
		date = str(year) + '-' + str(October_2018) + '-' + str(day)
		print(date)
		scraper_function(date)
		day+=1
				
	#November_2018
	November_2018 = 11; day = 1
	while day <= 30:
		# date = year-month-day
		date = str(year) + '-' + str(November_2018) + '-' + str(day)
		print(date)
		scraper_function(date)
		day+=1		

	#December_2018
	December_2018 = 12; day = 1
	while day <= 31:
		# date = year-month-day
		date = str(year) + '-' + str(December_2018) + '-' + str(day)
		print(date)
		scraper_function(date)
		day+=1		

def scraper_function(date):
	exists = os.path.isfile('{}.csv'.format(date))
	if exists:
		print('{}.csv exixts'.format(date))
		print(" ")
	else:
		#accurate_csv.to_csv('{}.csv'.format(date))
		try:
			# GET request to urllib
			dark_sky = urllib.request.urlopen("https://darksky.net/details/-0.3168,36.931/{}/ca12/en".format(date))
			# Beautiful Soup object creation
			soup = BeautifulSoup(dark_sky.read(), 'lxml')
		except Exception:
			print("[-] Opening url unsuccessful")
			sys.exit(1)


		try:
			# searching for the script tag
			data = soup.find_all("script")[1].string
			#print("[+] String found")
		except Exception:
			print("[-] String not found")

		try:
			#os.system("echo '{}' | grep hours".format(data))
			output = run(['echo', data], stdout=PIPE).stdout.decode()
			#print("[+] $echo")
		except Exception:
			print("[-] $echo command unsuccessful")

		try:
			# removing the values.txt file if it exists
			os.system("rm values.txt")
		except Exception:
			print("[-] values.txt file not found")

		# defining the location for temporarily storing weather values
		path = 'values.txt'

		try:
			values_file = open(path, 'w')
			#print("[+][1]")
		except FileNotFoundError:
			# create file
			values_file = open(path, 'x')
			# open file for writing
			values_file = open(path, 'w')
		except Exception:
			print("[-] Unknown error")

		try:
			# write string to file
			values_file.write(output)
			#print("[+][2]")
		except Exception:
			print("[-] [1]Writing to file unsuccessful")
			
		try:
			values_file.close()
		except Exception:
			print("[-] File failed to close")

		try:
			output2 = run(['grep', 'hours', 'values.txt'], stdout=PIPE).stdout.decode()
			#print("[+] grep")
		except Exception:
			print("[-] $grep command unsuccessful")
			
		#os.system("cat values.txt")

		try:
			values_file = open(path, 'w')
			#print("[+][3]")
		except FileNotFoundError:
			# create file
			values_file = open(path, 'x')
			print("[-] File creatin successful")
			# open file for writing
			values_file = open(path, 'w')
		except Exception:
			print("[-] Unknown error")	

		try:
			values_file.write(output2)
			#print("[+][4]")
		except Exception:
			print("[-] [2] Writing to file unsuccessful")

		#os.system("cat values.txt")

		try:
			values_file.close()
		except Exception:
			print("[-] File failed to close")

		os.system("cat values.txt | cut -c15- | sed 's/.$//' > actual_values.txt; cp values.txt values.txt.bak; cp actual_values.txt values.txt")

		#os.system("cat values.txt")
		try:
			output1 = run(['cat', 'values.txt'],stdout=PIPE).stdout.decode()
			output2 = output1[0:(len(output1)-1)]
			json_data = json.loads(output2)
			test34 = json.dumps(json_data)
			csv_output = pandas.read_json(test34)
		except Exception:
			print("[-] Error converting json to csv")
		#print(csv_output)
		try:
			df = pandas.read_json(test34)
			df.to_csv('test.csv')
			accurate_csv = pandas.read_csv('test.csv', usecols=['time', 'summary', 'precipIntensity', 'temperature', 'dewPoint', 'humidity', 'pressure', 'windSpeed', 'windGust', 'windBearing', 'cloudCover', 'uvIndex', 'ozone'])
			accurate_csv.to_csv('{}.csv'.format(date))
		except Exception:
			print("[-] Error creating correct csv file")
		print("{}.csv".format(date))
	
# Invoke function to get 2018 weather data
scrape_2018_data()
# Invoke function to get 2019 weather data
scrape_2019_data()



test_year = strftime("%Y")
test_day = strftime("%d")
test_month = int(strftime("%m")) 
test_date_today = "{}-{}-{}".format(test_year, test_month, test_day)

start_date = "2018-9-1"

year = 2018
year2019 = 2019
month2019 = 1

August = 8; day = 1; year = 2019

September = 9; day = 1; year = 2019
while day <= 24:
	# date = year-month-day
	date = str(year) + '-' + str(August) + '-' + str(day)
	#print(date)
	#scraper_function(date)
	if day == int(strftime("%d")):
		#print("Today's date")
		print("")
		break
	day+=1
	
date_file_path = "date.txt"
try: 
	date_file = open(date_file_path, 'w')
	date_file.write(date)
	date_file.close()
except Exception:	
	print("Date of last weather scraping not recorded")
