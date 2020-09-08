			#------Draw Algorithm Implimentation--#
			#-----Created By: Sourav Mondal-------#
			#-----Created at: 26/05/2020----------#
			#------ Roll No - 17IT8052------------#
			
			#One Sided selection only draw
import random

def randomNumbers(Numbers, size):         #Used For generating random number list used as draw numbers
	Num=Numbers
	random.shuffle(Num)
	return Num
def sortDrawList(choiceWithDrawNum):						#Used for sorting choice list by draw number,using bubble sort 
	choiceWithDrawNum.sort(key=lambda num:num[1])

		
def generateStudentChoice(n):
	subList=[]
	for i in range(0,n):
		tempList=[i+1 for i in range(n)]
		randomNum=randomNumbers(tempList,n)
		subList.append(randomNum)
	choiceList=[]
	for i in range(n):
		string=""
		for j in range(n):
			if j==0:
				string += str(subList[i][j])
			else:
				string += " "+str(subList[i][j])
		choiceList.append(string)
	print("Student Choice List:")
	for i in range(n):
		print(choiceList[i])
	print(" ")
	
	f=open('input.txt','w')
	for i in range(n):
		f.writelines(str(choiceList[i]))
		f.write("\n")
	
#Draw Algorithm Main part
def drawAlgoithm(studentChoice, finalAllotmentList,n):
	# #drawNumList will store the draw numbers
	generateStudentChoice(n)
	#choice=[]
	inputChoices=[]
	
	inputFromFile=open('input.txt','r')
	stringLine=inputFromFile.read()
	inputChoices.append(stringLine.splitlines())
	
	for i in range(0,n):
		tempVariable=[int(num) for num in inputChoices[0][i].split()]
		studentChoice.append(tempVariable)
	# drawNumList=[]
	drawNumbers=[i+1 for i in range(n)]
	drawNumbers=randomNumbers(drawNumbers,n)
	print("Draw Numbers are:",drawNumbers[0:])
	choiceWithDrawNum=[]
	for i in range(0,n):
		pair=(i,drawNumbers[i])
		choiceWithDrawNum.append(pair)
		
	sortDrawList(choiceWithDrawNum)
	alloted=[0]*(n+1)
	
	picked=0
	for i in range(0,n):
		roomNow=choiceWithDrawNum[i][0]
		for j in range(0,n):
			picked=studentChoice[roomNow][j]
			if alloted[picked]==0:
				finalAllotmentList[roomNow]=picked
				alloted[picked]=1
				break
				
	print("Alloted Rooms to the student are:", finalAllotmentList)

def main():
	print("---------Implimentation of a Draw Algorithm for allotment of hostel room--------")
	studentChoice=[]
	n=int(input("Enter the number of student to allot rooms:"))
	finalAllotmentList=[0]*n						#Final alloted list
	
	drawAlgoithm(studentChoice,finalAllotmentList,n);
	print("------End-----")

if __name__=="__main__":
	main()
