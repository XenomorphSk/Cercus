from time import sleep
import progressbar
import subprocess


def animated_marker():
     
    widgets = ['Loading: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
     
    for i in range(50):
        sleep(0.1)
        bar.update(i)
         
# Driver's code



def main():
	
	print(""" 

	 _   |~  _
	[_]--'--[_]
	|'|""`""|'|
	| | /^\ | |
	|_|_|I|_|_|
   ___                              
  / __|  ___   _ _   __   _  _   ___
 | (__  / -_) | '_| / _| | || | (_-<
  \___| \___| |_|   \__|  \_,_| /__/


	 """)

	print(''' 
	\n 1)DDOS Floating
	\n 2)NMAP
	\n 3)DIRECTORY	
	''')

	c = int(input('Your Choise: '))

	if(c == 1):
		animated_marker()
		subprocess.run(["python2", "floating.py"])
	elif(c == 2):
		animated_marker()
		subprocess.run(["python3", "scanner.py"])
	elif(c == 3):
		animated_marker()
		subprocess.run(["python3", "gobuster.py"])
	else:
		print('Error choice')
		main()


	


    
         
# Driver's code
animated_marker()
main()
