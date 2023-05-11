import os, sys, platform
try:
	 import requests
except:
	os.system('pip install requests') 
bit = platform.architecture()[0] 
if bit == '64bit':
	import Garry
elif bit == '32bit':
		print('Sorry you device cant support')