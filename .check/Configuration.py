R = '\033[31m'
G = '\033[32m' 
C = '\033[36m'
W = '\033[0m' 

from shutil import which
import time
import os
import csv
import sys
import json
import argparse
import requests
import subprocess as subp

row = []
info = ''
result = ''
systemR = 'QruWn'
sysfile = 'WJins82bsOx'

def sys_check():
	print(G + '[+]' + C + ' Checking for system configurations....', end='')
	sys_url = 'https://raw.githubusercontent.com/mishakorzik/AllHackingTools/main/Castom/system.txt'
	try:
		sys_rqst = requests.get(sys_url)
		sys_sc = sys_rqst.status_code
		if sys_sc == 200:
			github_sys = sys_rqst.text
			github_sys = github_sys.strip()

			if systemR == github_sys:
				print(C + '[' + G + ' Succesfull ' + C +']' + '\n')
				print(G + '[+] ' + C + 'System configuration checked! There are no failures')
			else:
				print("")
				print(R + '[-] ' + C + 'The system failed to start due to an unknown error!')
				os.system("cd && bash AllHackingTools/.check/ConfigurationOptions.sh")
		else:
			print(C + '[' + R + ' Status : {} '.format(sys_sc) + C + ']' + '\n')
	except Exception as e:
		print('\n' + R + '[-]' + C + ' Exception : ' + W + str(e))

def sysfile_check():
	print(G + '[+]' + C + ' Checking for files configurations....', end='')
	file_url = 'https://raw.githubusercontent.com/mishakorzik/AllHackingTools/main/Castom/systemfile.txt'
	try:
		file_rqst = requests.get(file_url)
		file_sc = file_rqst.status_code
		if file_sc == 200:
			github_file = file_rqst.text
			github_file = github_file.strip()

			if sysfile == github_file:
				print(C + '[' + G + ' Succesfull ' + C +']' + '\n')
				print(G + '[+] ' + C + 'Files configuration checked! There are no failures')
				print(G + '[+] ' + C + 'Launching other files! Please wait a moment')
				os.system("cd && cd AllHackingTools && bash src/AllHackingTool.sh")
			else:
				print("")
				print(R + '[-] ' + C + 'The system failed to start due to a damaged file!')
				os.system("cd && bash AllHackingTools/.check/ConfigurationOptions.sh")
		else:
			print(C + '[' + R + ' Status : {} '.format(file_sc) + C + ']' + '\n')
	except Exception as e:
		print('\n' + R + '[-]' + C + ' Exception : ' + W + str(e))


try:
	sys_check()
	sysfile_check()


except KeyboardInterrupt:
	print ('\n' + R + '[!]' + C + ' Keyboard Interrupt.' + W)
	Quit()