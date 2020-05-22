			#------Draw Algorithm Implimentation--#
			#-----Created By: Sourav Mondal-------#
			#-----Created at: 21/05/2020----------#
			#------ Roll No - 17IT8052------------#
import random

def generateDrawNumbers(drawNumList, size):         #Used For generating random number list used as draw numbers
	while(len(drawNumList)!=size):
		num=random.randint(1,size)
		if num not in drawNumList:
			#if not already exist then append else loop again
			drawNumList.append(num)
	print(drawNumList)
	return drawNumList
def sortDrawList(studentChoice, n):						#Used for sorting choice list by draw number,using bubble sort 
	for i in range(len(studentChoice)):					#Time Complexity : O(n^2)
		for j in range(i+1,len(studentChoice)):
			#Compareing draw numbers
			if studentChoice[i][n]>studentChoice[j][n]:
				tempVar=studentChoice[j]
				studentChoice[j]=studentChoice[i]
				studentChoice[i]=tempVar

def printList(studentChoice):							#Used for Printing Student choice list
	for i in range(len(studentChoice)):
		print(studentChoice[i])
		
		
def readStudentChoiceInputFile(studentChoice):			#This function Takes input from another file and stores it in the student choice list
	textFile= open('draw_algorithm_input.txt','r') 		#Opening the input File(Must be in same location)
	lineList=textFile.readlines()
	for subList in lineList:							#Spliting each space seperated lines and converting into integers list
		subList=subList.split()
		for i, v in enumerate(subList):
			if v.isdigit():
				subList[i]=int(v)
			else:
				subList[i]=v
		studentChoice.append(subList)

def drawAlgoithm(studentChoice, finalAllotmentList):	#The main draw algorithm function
	#drawNumList will store the draw numbers
	drawNumList=[]
	#allotedHostels will take care of how many hostels alloted so far
	allotedHostels=[]
	size=len(studentChoice)
	#n is total number of elememnt in each list
	n=len(studentChoice[0])
	#generating draw numbers and inserting them at the end of the student choice list
	generateDrawNumbers(drawNumList,size)
	for i in range(len(studentChoice)):			
		studentChoice[i].append(drawNumList[i])
		
	print("After inserting draw numbers to the choice list:")
	printList(studentChoice)
	print("-----")
	#Sorting the student choice list according to  the draw numbers
	sortDrawList(studentChoice,n)
	print("Choice list after sorting according to the draw number:")
	printList(studentChoice)
	print("-----")
	
	#alloting rooms to the student according to the draw number priority and vacent rooms availble
	for i in range(len(studentChoice)):
		allotment=[]
		allotment.append(studentChoice[i][0])
		for j in range(1,n):			
			#Alloting vacent room to the students and once they got a room break the loop
			if studentChoice[i][j] not in allotedHostels:
				allotedHostels.append(studentChoice[i][j])
				allotment.append(studentChoice[i][j])
				break
			else:
				continue
		finalAllotmentList.append(allotment)
			

def main():
	print("---------Implimentation of a Draw Algorithm for allotment of hostel room--------")
	print("Total number of rooms in hostel is:15")
	print("Total number of student needs room:15")
	studentChoice=[];
	readStudentChoiceInputFile(studentChoice)  #reading the input file
	print("Student Preference to the hostel rooms are:")
	printList(studentChoice)
	finalAllotmentList=[]						#Final alloted list
	
	drawAlgoithm(studentChoice,finalAllotmentList);
	print("Final List of Allotment: ")
	printList(finalAllotmentList)

if __name__=="__main__":
	main()
