import requests
import sys
from time import sleep
from os import system

ORANGE_COLOR = "\33[1;33m"
WHITE_COLOR = "\33[1;37m"
RED_COLOR = "\33[1;31m"
GREEN_COLOR = "\33[1;32m"
arguments = sys.argv

system("clear")
print(f"""{RED_COLOR}░▒▓██████████████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░      ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░░▒▓██████▓▒░░▒▓███████▓▒░░▒▓██████▓▒░        ░▒▓███████▓▒░ ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░         ░▒▓█▓▒░     
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓██▓▒░▒▓█▓▒░         ░▒▓█▓▒░     
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓███████▓▒░░▒▓████████▓▒░▒▓██▓▒░▒▓█▓▒░         ░▒▓█▓▒░""")

try:
	target_url = arguments[1]
	num_of_requests = int(arguments[2])
	delay_between_requests = float(arguments[3])
	persistence = False
	auto_persistence = False
except IndexError:
	print("WELCOME!")
	print("\33[1;37mFormat: maybe {target_url} {num_of_requests} {delay_between_requests} [--persistence | --auto-persistence]")
	print("- target_url\t\t\t the website url that you want to target")
	print("- num_of_requests\t\t how many requests you want to go before the it get killed (give 0 for infinite requests)")
	print("- delay_between_requests\t how much the delay between requests in second (the higher the delay, the less a chance of you getting suspicious)")
	print("- --persistence\t\t\t include this to make the program keeps running even the website blocking our requests (and wait until you press a key and then run the request again)")
	print("- --auto-persistence\t\t this is the same as --persistence but it will automatically check if the server has already unblock you by wait for several seconds before requesting again")
	exit(0)

if "--persistence" in arguments:
	persistence = True
if "--auto-persistence" in arguments:
	persistence = True
	auto_persistence = True

print(f"{ORANGE_COLOR}Just to make sure..")
print(f"{ORANGE_COLOR}Target\t\t\t: {WHITE_COLOR}{target_url}")
print(f"{ORANGE_COLOR}Number of Requests\t: {WHITE_COLOR}{num_of_requests}")
print(f"{ORANGE_COLOR}Delay between requests\t: {WHITE_COLOR}{delay_between_requests} second{'s' if delay_between_requests > 1 else ''}")
print(f"{ORANGE_COLOR}Persistence?\t\t: {WHITE_COLOR}{persistence}", end=" ")
if persistence:
	print('(auto' if auto_persistence else '(manual', end=")\n")
print()

if input("continue? [y/n] ") == 'y':
	num_of_getting_limited = 0
	i = 0
	while (i < num_of_requests) if num_of_requests > 0 else (True):
		print(f"{WHITE_COLOR}Requesting..", end="\r")
		response = requests.get(target_url)
		print("Request Done!")
		status_code = response.status_code
		print(f"{WHITE_COLOR}Request number-{RED_COLOR}{i+1}{WHITE_COLOR}.", end=" ")
		if status_code == 200:
			print(f"{GREEN_COLOR}Status Code: {status_code}")
			num_of_getting_limited = 0
		elif status_code == 429:
			print(f"{ORANGE_COLOR}Status Code: {status_code}")
			num_of_getting_limited += 1
			if not persistence:
				print("ENDED BECAUSE OF LIMITED (if you want to go even after get limit put '--persistence' parameter)")
				exit(0)
			if not auto_persistence:
				print("You've got limited..")
				input(f"{WHITE_COLOR}press any key to check again.. (and automatically continue if you freed from the limit)")
			else:
				print(f"You've got limited warning for {num_of_getting_limited} times!")
				print(f"Wait {5*num_of_getting_limited} seconds for the next requests..")
				sleep(5*num_of_getting_limited)
		else:
			print(f"{ORANGE_COLOR}Error http code: {status_code}")

		i += 1
		sleep(delay_between_requests)

else:
	print("aight bro.")
