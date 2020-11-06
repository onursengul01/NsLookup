import os
import pyfiglet
class Nslookup:
	def __init__(self):
		pass
	 	
	def Scan(self):
		result = pyfiglet.figlet_format("NSlookup")
		print(result)
		global root
		root = input("Enter the domain name of the webstite\n")
		if root == "":
			os.system("cls")
			return s.Scan()
		os.system(f"nslookup {root}")
		while True:
			def Retry():
				retry = input("Would you like to scan more domains? [y] or [n]\n")
				if retry == "y":
					os.system("cls")
					return s.Scan()

				if retry == "n":
					print("ok bye...")
					exit()
			Retry()		
s = Nslookup()

s.Scan()
