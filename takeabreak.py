import time, webbrowser, os

total_breaks = int(input("How many Breaks Do you Want? "))
break_count = 0
break_time = int(input("How long do you want the break to be?(in minutes) "))
work_time = int(input("How long to wait between work and break?(in minutes) "))
link = input("(optional) Specify a url you want to visit during the break: ")
quote = '"' + link + '"'							#put url inside double quotes
print("You can now minimize this Window")

while break_count < total_breaks:
	time.sleep(work_time*60)						#wait for specified time
	if link:								#check if url is specified
		webbrowser.open(quote)
	else:
		webbrowser.open("https://www.youtube.com/watch?v=ApgNm4Bu-Lw")	#open browser with the specified link
	time.sleep(break_time*60)						#wait for specified time
	# os.system("taskkill /im firefox.exe /f")
	# os.system("taskkill /im opera.exe /f")
	# os.system("taskkill /im chrome.exe /f")				#autokill task after few seconds to get back to work
	webbrowser.open("http://novascjj.com/wp-content/uploads/2014/12/back-to-work.jpg")
	break_count += 1							#increment break_count by 1
