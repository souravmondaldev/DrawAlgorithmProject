			#-----Created By: Sourav Mondal-------#
			

import random

def sortDrawList(studentChoice):						#Used for sorting choice list by draw number
	for i in range(len(studentChoice)):
		for j in range(i+1,len(studentChoice)):
			if studentChoice[i][11]>studentChoice[j][11]:
				tempVar=studentChoice[j]
				studentChoice[j]=studentChoice[i]
				studentChoice[i]=tempVar

def drawAlgoithm(studentChoice, finalAllotmentList):
	drawNumList=[]
	allotedHostels=[]
	while(len(drawNumList)!=len(studentChoice)):
		r=random.randint(1,10)
		if r not in drawNumList:
			drawNumList.append(r)
	for i in range(len(studentChoice)):					#Inserting draw number to the choice list
		studentChoice[i].append(drawNumList[i])
		
	print("After inserting draw numbers to the choice list:")
	print(studentChoice)
	print("-----")
	sortDrawList(studentChoice)
	print("Choice list after sorting according to the draw number:")
	print(studentChoice)
	print("-----")
	for i in range(len(studentChoice)):
		allotment=[]
		allotment.append(studentChoice[i][0])
		for j in range(1,len(studentChoice)-1):			#Alloting vacent room to the students
			if studentChoice[i][j] not in allotedHostels:
				allotedHostels.append(studentChoice[i][j])
				allotment.append(studentChoice[i][j])
				break
			else:
				continue
		finalAllotmentList.append(allotment)
			

def main():
	print("---Implimentation of a Draw Algorithm for allotment of hostel room----")
	print("Total number of rooms in hostel is:10")
	print("Total number of student needs room:10")
	print("Room numbers are '1', '2', '3', '4', '5','6', '7', '8','9', '10'.")
	print("Each student has to enter their name first and then their choices of room number according to their preference")
	studentChoice=[];
	for i in range(0,10):
		arrStudent=[]
		ch=input("Enter Student Name: ")
		arrStudent.append(ch)
		for j in range(0,10):
			print("Enter room choice: ")
			x=int(input())
			arrStudent.append(x)
		studentChoice.append(arrStudent)
		print(ch+" Filled hostel allotment form.")
	finalAllotmentList=[]
	
	drawAlgoithm(studentChoice,finalAllotmentList);
	print("Final List of Allotment: ")
	print(finalAllotmentList)

if __name__=="__main__":
	main()
