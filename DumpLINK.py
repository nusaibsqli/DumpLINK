try:
	import sys
	import os
	import time
	from bs4 import BeautifulSoup
	import requests
	from colorama import Back, Fore, Style
except ImportError as ie:
	print(ie)

print(Style.BRIGHT + "")

os.system("clear")

print(Fore.CYAN + "___________              .__         .__  __            __________                    ")
print(Fore.GREEN + "\_   _____/__  _________ |  |   ____ |__|/  |_          \____    /____   ____   ____  ")
print(Fore.CYAN + " |    __)_\  \/  /\____ \|  |  /  _ \|  \   __\  ______   /     //  _ \ /    \_/ __ \ ")
print(Fore.GREEN +" |        \>    < |  |_> >  |_(  <_> )  ||  |   /_____/  /     /(  <_> )   |  \  ___/ ")
print(Fore.CYAN + "/_______  /__/\_ \|   __/|____/\____/|__||__|           /_______ \____/|___|  /\___  >")
print(Fore.GREEN + "        \/      \/|__|                                          \/          \/     \/ ")

print(Fore.CYAN + """ 
 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
 #				User It Responsibly				    #
 #				Made By ghosthub (b@b@y)				    #
 #                              visit: https://iconicbabay.simdif.com				    #
 #    		I Hold No Responsibility For Any Comprimisation Done By My Tool	    #
 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

mmmm                        m      mmmmm  mm   m m    m
 #   "m m   m  mmmmm  mmmm   #        #    #"m  # #  m"
 #    # #   #  # # #  #" "#  #        #    # #m # #m#
 #    # #   #  # # #  #   #  #        #    #  # # #  #m
 #mmm"  "mm"#  # # #  ##m#"  #mmmmm mm#mm  #   ## #   "m
                      #
                      "

""")


try:

	url = input("Enter Website: ")

	start1 = url.startswith('http')
	start2 = url.startswith('https')
	if(start1 == False or start2 == False):
		new_Url = ("http://" + url)
		if(len(url) == 0):
			print(Fore.RED + ">> [!] No Valid Url Has Been Inserted!")
			time.sleep(2)
			print(Fore.RED + ">> [!] Exiting....")
			time.sleep(3)
			sys.exit()
		else:
			response = requests.get(new_Url)
			content = response.content
			soup = BeautifulSoup(content, "lxml")
			links = soup.find_all('a')
			for link in links:
				href = link.get('href')
				print(Fore.CYAN + ">> [+] Link: " + str(href))
				time.sleep(1)

	else:
		if(len(url) == 0):
			print(Fore.RED + ">> [!] No Valid Url Has Been Inserted!")
			time.sleep(2)
			print(Fore.RED + ">> [!] Exiting....")
			time.sleep(3)
			sys.exit()
		else:
			response = requests.get(url)
			content = response.content
			soup = BeautifulSoup(content, "lxml")
			links = soup.find_all('a')
			for link in links:
				href = link.get('href')
				print(Fore.CYAN + ">> [+] Link: " + str(href))
				time.sleep(1)
except KeyboardInterrupt as ki:
		print(Fore.RED + ">> [!] Exiting....")
		time.sleep(3)
		sys.exit()

    
