import time
import webbrowser

total_breaks = int(input("How many Breaks Do you Want? "))
break_count = 0

while break_count < total_breaks:
	time.sleep(3600)	#wait 1 hour 
	webbrowser.open("https://www.youtube.com/watch?v=ApgNm4Bu-Lw")	#open browser with the specified link
	break_count += 1	#increment break_count by 1