from os import system,name
import sys
from time import sleep
from termcolor import colored,cprint

def clear():
	if name=='nt':
	    _=system('cls')
	else:
	  _=system('clear')

def banner():
	cprint("                                          Programmer Mubsshir Khan  ",'cyan',attrs=['bold'])
	print(colored("    __   ___   ____   __ __    ___  ____    _____ ____  ___   ____  ",'cyan','on_grey',attrs=['bold','blink']))
	print(colored("   /  ] /   \ |    \ |  |  |  /  _]|    \  / ___/|    |/   \ |    \ ",'cyan','on_grey',attrs=['bold','blink']))
	print(colored("  /  / |     ||  _  ||  |  | /  [_ |  D  )(   \_  |  ||     ||  _  |",'cyan','on_grey',attrs=['bold','blink']))
	print(colored(" /  /  |  O  ||  |  ||  |  ||    _]|    /  \__  | |  ||  O  ||  |  |",'cyan','on_grey',attrs=['bold','blink']))
	print(colored("/   \_ |     ||  |  ||  :  ||   [_ |    \  /  \ | |  ||     ||  |  |",'cyan','on_grey',attrs=['bold','blink']))
	print(colored("\     ||     ||  |  | \   / |     ||  .  \ \    | |  ||     ||  |  |",'cyan','on_grey',attrs=['bold','blink']))
	print(colored(" \____| \___/ |__|__|  \_/  |_____||__|\_|  \___||____|\___/ |__|__|",'cyan','on_grey',attrs=['bold','blink']))
	sleep(1)
                                                                    

def options():
	print(colored("*Digital Electronics Number Converting  command line application*",'green',attrs=['bold','dark']))
	print("")
	cprint("Choose your options \n",'blue',attrs=['bold'])
	cprint("[1]Decimal to Any other number system",'yellow')
	cprint("[2]Any to Decimal number",'yellow')
	cprint("[3]Any number system to Any number system",'yellow')
	cprint("[4]Exit",'yellow')

def D_B(a):
	if a==0:
		return
	else:
		D_B(a//2)
		print(a%2,end="")

def D_O(a):
	if a==0:
		return
	else:
		D_O(a//8)
		print(a%8,end="")


def D_H(a):
	if a==0:
		return
	else:
		D_H(a//16)
		c=a%16
		if c==10:
			cprint("A",'red',end='')
		elif c==11:
			cprint("B",'red',end='')
		elif c==12:
			cprint("C",'red',end='')
		elif c==13:
			cprint("D",'red',end='')
		elif c==14:
			cprint("E",'red',end='')
		elif c==15:
			cprint("F",'red',end='')
		else:
			cprint(a%16,'cyan',end="")

	
def main_program():
	cprint("Please select yout option ",'magenta',attrs=['bold'],end='')
	choice=input(colored(">",'magenta',attrs=['bold','blink']))
	while True:
		if choice=='1' or choice=='2' or choice=='3' or choice=='4':
			break
		else:
			clear()
			cprint('Plz enter correct choice','red',attrs=['bold','underline'])
			options()
			choice=input("Please select yout option > ")
	clear()
	banner()
	if choice=="1":
		cprint("Please select an option",'yellow')
		cprint("[1]Decimal to Binary",'yellow')
		cprint("[2]Decimal to Octel",'yellow')
		cprint("[3]Decimal to Hexadecimal",'yellow')
		cprint("[4]Go Back",'yellow')
		choice=input("> " )
		while True:
			if choice=='1' or choice=='2' or choice=='3' or choice=='4':
				break
			else:
				clear()
				print ("plz enter correct choice: ")
				cprint("Please select an option",'yellow')
				cprint("[1]Decimal to Binary",'yellow')
				cprint("[2]Decimal to Octel",'yellow')
				cprint("[3]Decimal to Hexadecimal",'yellow')
				cprint("[4]Go Back",'yellow')
				choice=input("Please select yout option > ")
		if choice=="1":
			a=eval(input("Enter a Dicimal Number: "))
			print("Binary Number is",end=" ")
			D_B(a)
			print()
		if choice=="2":
			a=eval(input("Enter a Dicimal Number: "))
			print("Octel Number is",end=" ")
			D_O(a)
			print()
		if choice=="3":
			a=eval(input("Enter a Dicimal Number: "))
			print("Hexadecimal Number is",end=" ")
			D_H(a)
			print()
		if choice=='4':
			main()
	if choice=="4":
		sys.exit("Exit by the User")
def main():
	clear()
	banner()
	options()
	main_program()
main()
