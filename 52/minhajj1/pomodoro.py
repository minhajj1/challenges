#!/usr/local/bin/python3

from datetime import datetime, date, timedelta

def createTimeDelta(type):
	timer = input(f"How many {type} would you like to set the timer for: ")
	if str(type).lower() == "minutes":
		delta = timedelta(minutes=int(timer))
	if str(type).lower() == "seconds":
		delta = timedelta(seconds=int(timer))
	return delta

def userInterface(type):
	choiceString = """Specify which timer you'd like to set:
			1. in Minutes
			2. in Seconds
			"""
	choice = input(choiceString + f"\nFor your {type} Session\n>")
	return choice

def createEndTime(deltaTime):
	now = datetime.today().replace(microsecond=0)
	endTime = now + deltaTime
	return endTime.replace(microsecond=0)

def choices(choice):
	timeType = ""
	if(choice == "1"):
        	delta = createTimeDelta("minutes")
        	timeType = "minutes"
	elif(choice == "2"):
        	delta = createTimeDelta("seconds")
        	timeType = "seconds"
	else:
		print("You need to select a proper choice")
		choices(choice)
	return delta, timeType

def createBreak():
	getBreak = userInterface("break")
	breakDelta, timeType = choices(getBreak)
	breakEndTime = createEndTime(breakDelta)
	print(f"Your break will be {breakDelta} {timeType} and will end at {breakEndTime}")
	now = datetime.today().replace(microsecond=0)
	while(now != breakEndTime):
		if(now != datetime.today().replace(microsecond=0)):
			print(now)
		now = datetime.today().replace(microsecond=0)
		

def main():
	print("\n\n\nWelcome to the Pomodoro Timer")
	choice = userInterface("study")
	onBreak = False
	delta, timeType = choices(choice)	
	endTime = createEndTime(delta)
	print(timeType)
	while(True):
		now = datetime.today().replace(microsecond=0)
		while(now != endTime):
			if(now != datetime.today().replace(microsecond=0)):
				print(now)

			now = datetime.today().replace(microsecond=0)
		if(now == endTime):
			onBreak = True
			print(f"You have studied for {delta} {timeType}")
			createBreak()
			print("break is over")
			main()
main()
