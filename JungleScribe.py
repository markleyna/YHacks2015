# messing-around


from tkinter import *
#from tkinter import Tk, Canvas
import random
import copy
from scipy.stats import norm
from PIL import ImageTk, Image

width = 1300
height = 500
####################################
# init
####################################
def isInRectangle(L, userx,usery):
	x1 = L[0]
	y1 = L[1]
	x2 = L[2]
	y2 = L[3]
	if (userx <= x2) and (userx >= x1) and (usery >= y1) and (usery <= y2):
		#print("yes")
		return True
	else:
		return False
def init(data):
	data.points = list()
	data.userPoints = list()
	data.score = None
	data.letterType = 0
	data.letterIndex = 0
	data.mode = "splashScreen"
	data.image = None
	data.buttonList = list()
	data.buttonList.append([700,200,1100,250])
	data.buttonList.append([700,300,1100,350])
	data.buttonList.append([700,400,1100,450])
	data.letterScores =  [ ([None] * 2) for row in range(26) ]
	data.submitted = False

####################################
# mode dispatcher
####################################

def mousePressed(event, data):
	if (data.mode == "splashScreen"): splashScreenMousePressed(event, data)
	if (data.mode == "Game"): gameMousePressed(event,data)
	if (data.mode == "Instructions"): instructionMousePressed(event,data)
	if (data.mode == "Extension"): extensionMousePressed(event,data) 
def keyPressed(event, data):
	if (data.mode == "splashScreen"): splashScreenKeyPressed(event, data)
	if (data.mode == "Instructions"): instructionKeyPressed(event,data)
	
def timerFired(data):
	if (data.mode == "splashScreen"): splashScreenTimerFired(data)
	

def redrawAll(canvas, data):
	if (data.mode == "splashScreen"): splashScreenRedrawAll(canvas,data)
	if (data.mode == "Game"): gameRedrawAll(canvas,data)
	if (data.mode == "Instructions"): instructionRedrawAll(canvas,data)
	if (data.mode == "Extension"): extensionRedrawAll(canvas,data)
####################################
# splashScreen mode
####################################

def splashScreenMousePressed(event, data):
	if isInRectangle(data.buttonList[0],event.x,event.y): data.mode = "Game"
	if isInRectangle(data.buttonList[1],event.x,event.y): data.mode = "Instructions"
	if isInRectangle(data.buttonList[2],event.x,event.y): data.mode = "Extension"
def splashScreenKeyPressed(event, data):
	pass
def splashScreenTimerFired(data):
    pass

def splashScreenRedrawAll(canvas, data):
	global width
	global height
	width = 700
	height = 700
	img = PhotoImage(file ="junglescribe.gif")
	canvas.img = img
	canvas.create_rectangle(0,0,data.width,data.height,fill = "black")
	canvas.create_text(900,100, text = "Jungle Scribe", font = "Script 100 bold", fill = "white")
	canvas.create_image(20,20,image=canvas.img,anchor = 'nw')
	canvas.create_rectangle(700,200,1100,250,fill = "gold")
	canvas.create_rectangle(700,240,1100,250,fill = "orange")
	canvas.create_rectangle(700,300,1100,350,fill = "gold")
	canvas.create_rectangle(700,340,1100,350,fill = "orange")
	#canvas.create_rectangle(700,400,1100,450,fill = "gold")
	#canvas.create_rectangle(700,440,1100,450,fill = "orange")	
	canvas.create_text(900,215,text = "Begin Gameplay", font = "Cambria 20", fill = "black")
	canvas.create_text(900,315,text = "Instructions", font = "Cambria 20", fill = "black")
	#canvas.create_text(900,415,text = "Handwriting to Text", font = "Cambria 20", fill = "black")
####################################
# Instruction mode
####################################	
def instructionRedrawAll(canvas,data):
	canvas.create_rectangle(0,0,data.width,data.height,fill = "black")
	canvas.create_text(500,200,text = "On the left of the screen letters will appear.\nDo your best to trace over the lines accurately as possible.\nWhen you have traced the letter completely hit the submit button.\nYour score will be presented on the right side of the screen.\nThis game will take you through all 26 capital letters.\nYou can exit at any time by hitting the 'X' button at the top of the screen.\nHave fun and be the best jungle scribe ever!\n\n", fill = "white", font = "Cambria 18")
	canvas.create_rectangle(700,400,1100,450,fill = "gold")
	canvas.create_rectangle(700,440,1100,450,fill = "orange")
	canvas.create_text(900,415,text = "Return", font = "Cambria 20", fill = "black")
	
def instructionKeyPressed(event,data):
	pass

def instructionMousePressed(event,data):
	if isInRectangle(data.buttonList[2],event.x,event.y): data.mode = "splashScreen"
	
####################################
# Extension mode
####################################
def generateLine2(canvas, data, startx,starty,slope,length, type): #add in parameters initialx, initialy, slope
	initialx = startx
	initialy = starty
	for i in range(0, length):
		currentx = initialx + i
		currenty = initialy - (slope * i)
		data.points.append([currentx,currenty])
		if type == 0:
			pass
			#canvas.create_line(currentx,currenty,currentx+1,currenty+1)
		elif type == 1: #vertical
			#canvas.create_line(currenty,currentx,currenty+1,currentx+1)
			pass
	
def generateEllipse2(canvas,data,centerx,centery,type, a, b):
	initialy = 0 
	initialx =  b
	k = 0
	growthFactor = .01
	while(k < b):
		k += growthFactor
		growthFactor += .1
		currentx = initialx - k
		currenty = ((a **2) - ((a**2)/(b**2))*(currentx**2)) ** .5
		currentPx = currentx + centerx
		currentOx = centerx - currentx
		currentPy = currenty + centery
		currentOy = centery - currenty
		if type == 0 or type == 2 or type == 3 or type == 5:
			#canvas.create_line(currentPx,currentPy,currentPx+1,currentPy+1) #4th quadrant
			data.points.append([int(currentPx),int(currentPy)])
		if type == 2 or type == 3 or type == 4:
			#canvas.create_line(currentPx,currentOy, currentPx+1,currentOy + 1) #1st quadrant
			data.points.append([int(currentPx),int(currentOy)])
		if type == 0 or type == 1 or type == 3 or type == 6:
			#canvas.create_line(currentOx,currentPy,currentOx+1,currentPy + 1)  #3rd quadrant
			data.points.append([int(currentOx),int(currentPy)])
		if type == 1 or type == 3:
			#canvas.create_line(currentOx,currentOy,currentOx+1,currentOy + 1) #2nd quadrant
			data.points.append([int(currentOx),int(currentOy)])
			
def extensionMousePressed(event,data):
	if (isInRectangle(data.buttonList[0],event.x,event.y)): data.submitted = True
	try: data.userPoints = data.userPoints + [[(event.x),(event.y)]]
	except: print("Failed")
	
def regression2(data,type):
	#print(data.userPoints)
	sortedUserPoints = copy.deepcopy(data.userPoints)
	sortedPoints = copy.deepcopy(data.points)
	sortedUserPoints.sort()
	sortedPoints.sort()
	#print(sortedUserPoints)
	
	#print(sortedUserPoints)
	if type == 1:
		epsilonx = 5
		epsilony = 5
	else:
		epsilonx = 5
		epsilony = 5
	sumErrorx = 0
	sumErrory = 0
	for i in range(0,len(data.points),1): 
		bigger = None
		biggerIndex = None
		smaller = None
		smallerIndex = None
		for j in range(len(data.userPoints)):
			if sortedUserPoints[j][0] > sortedPoints[i][0] and bigger == None:
				bigger = sortedUserPoints[j][0]
				biggerIndex = j
				smaller = sortedUserPoints[j-1][0]
				smallerIndex = j -1
				break
		if (bigger == None):
			closestIndex = len(sortedUserPoints) - 1
		elif (smallerIndex == -1):
			closestIndex = 0
		elif (bigger - sortedPoints[i][1]) < (sortedPoints[i][1]-smaller):
			closestIndex = biggerIndex
		else: closestIndex = smallerIndex
		#print(len(sortedPoints),i,len(sortedUserPoints),closestIndex)
		if abs(sortedPoints[i][0] - sortedUserPoints[closestIndex][0]) < epsilonx:
			pass
			
		else:
			print(sortedUserPoints[closestIndex][0])
			sumErrorx += 1
			continue
		bigger = None
		biggerIndex = None
		smaller = None
		smallerIndex = None
		possibleYs = list()
		closestYIndex = None
		for j in range(len(sortedUserPoints)):
			if sortedUserPoints[closestIndex][0] == sortedUserPoints[j][0]:
				possibleYs.append(sortedUserPoints[closestIndex][1])
		possibleYs.sort()	
		for k in range(len(possibleYs) - 1):
			if possibleYs[k + 1] > possibleYs[k] and bigger == None:
				bigger = possibleYs[k+1]
				biggerIndex = k + 1
				smaller = possibleYs[k]
				smallerIndex = k
				break
		if (bigger == None):
			closestYIndex = len(possibleYs) - 1
		elif ((bigger - possibleYs[biggerIndex]) < (possibleYs[smallerIndex]-smaller)):
			closestYIndex = biggerIndex
		else: closestYIndex = smallerIndex
		if (abs(sortedPoints[i][1] - possibleYs[closestYIndex]) < epsilony):
			pass
		else:
			sumErrory += 1
	denom = len(sortedPoints)
	data.score = (110 - (((sumErrory + sumErrorx )/(denom)) * 100))
	if data.score < 0:
		data.score = 0
	elif data.score > 100:
		data.score = 100
	
	if data.letterType == 1:	
		mean = 19.003
		stdev = 6.14868
	else: 
		mean = 14.4310
		stdev = 3.8143
	zscore = (data.score - mean)/stdev
	data.score = round((norm.cdf(zscore)) * 100, 2)
	data.letterScores[data.letterIndex] = [data.score, data.letterIndex]
def makeLetter2(canvas, data, n):
	data.points = list()
	#data.userPoints = list()
	if n == 0: 
		generateLine2(canvas, data, 200,400,4,50, 0)
		generateLine2(canvas,data, 250,200,-4,50, 0)
		generateLine2(canvas, data, 225,300,0,50, 0)
	elif n == 1:
		generateLine2(canvas,data,200,200,0,200, 1)
		generateEllipse2(canvas,data,200,350,2,50,125) #bottom bubble of the b
		generateEllipse2(canvas,data,200,250,2,50,100) #top bubble of the b	
	elif n == 2:
		generateEllipse2(canvas,data,300,300,1,75,80)
		generateEllipse2(canvas,data, 300, 250, 4, 25, 80)
		generateEllipse2(canvas,data, 300, 350, 5, 25, 80)
	elif n == 3:
		generateLine2(canvas,data,200,200,0,200,1)
		generateEllipse2(canvas,data,200,300,2,100,125)
	elif n == 4:
		generateLine2(canvas,data,200,200,0,200,1)
		generateLine2(canvas,data,200, 200, 0,150,0)
		generateLine2(canvas,data,200,300,0,150,0)
		generateLine2(canvas,data,200,400,0,150,0)
	elif n == 5:
		generateLine2(canvas,data,200,200,0,200,1)
		generateLine2(canvas,data,200, 200, 0,150,0)
		generateLine2(canvas,data,200,300,0,100,0)
	elif n == 6:
		generateEllipse2(canvas, data, 300, 300, 1, 75, 80)
		generateEllipse2(canvas, data, 300, 250, 4, 25, 80)
		generateEllipse2(canvas, data, 300, 325, 5, 50, 80)
		generateLine2(canvas, data, 300, 325, 0, 80, 0)
	elif n == 7:
		generateLine2(canvas,data,200,300, 0, 200, 1)
		generateLine2(canvas,data,200,200,0, 200, 1)
		generateLine2(canvas, data,200,300, 0, 100, 0)
	elif n == 8:
		generateLine2(canvas,data,200,300, 0, 200, 1)
		generateLine2(canvas,data,250,200,0,100,0)
		generateLine2(canvas,data,250,400,0,100,0)
	elif n == 9:
		generateLine2(canvas,data,200,300, 0, 125, 1)
		generateEllipse2(canvas, data,250,325,0,75,50)
		generateLine2(canvas,data,250,200,0,100,0)
	elif n == 10:
		generateLine2(canvas,data,200,200,0,200,1)
		generateLine2(canvas,data,200,300,1.5,68,0)
		generateLine2(canvas,data,200,300,-1.5,68,0)
	elif n == 11:
		generateLine2(canvas,data,200,200,0,200,1)
		generateLine2(canvas,data,200,400,0,100,0)
	elif n == 12:
		generateLine2(canvas,data,200,400, 0, 200, 1)
		generateLine2(canvas,data,200,200,0, 200, 1)
		generateLine2(canvas,data,200,200,-.75,100,0)
		generateLine2(canvas,data,300,275,.75,100,0)
	elif n == 13:
		generateLine2(canvas,data,200,330, 0, 200, 1)
		generateLine2(canvas,data,200,200,0, 200, 1)
		generateLine2(canvas,data,200,200,-1.54,130,0)
	elif n == 14:
		generateEllipse2(canvas,data,300,300,3,100,75)
	elif n == 15:
		generateLine2(canvas,data,200,200,0,200, 1)
		generateEllipse2(canvas,data,200,250,2,50,100)
	elif n == 16:
		generateEllipse2(canvas,data,300,300,3,100,75)
		generateLine2(canvas,data, 325, 325, -1.8, 50, 0 )
	elif n == 17:
		generateLine2(canvas,data,200,200,0,200, 1)
		generateEllipse2(canvas,data,200,250,2,50,100)
		generateLine2(canvas, data, 200, 300, -1, 100, 0)
	elif n == 18:
		generateEllipse2(canvas,data,300,250,1,50,75)
		generateEllipse2(canvas,data,300,350,2,50,75)
		generateEllipse2(canvas,data,300,225,4,25,75)
		generateEllipse2(canvas,data,300,375,6,25,75)
	elif n == 19:
		generateLine2(canvas,data,200,300, 0, 200, 1)
		generateLine2(canvas,data,200,200,0,200,0)
	elif n == 20:
		generateEllipse2(canvas,data,300,200,0,200,100)
	elif n == 21:
		generateLine2(canvas,data,200,200,-2,100,0)
		generateLine2(canvas,data,300,400,2,100,0)
	elif n == 22:
		generateLine2(canvas,data,200,200,-4,50,0)
		generateLine2(canvas,data,350,400,4,50,0)
		generateLine2(canvas,data,250,400,2,50,0)
		generateLine2(canvas,data,300,300,-2,50,0)
	elif n == 23:
		generateLine2(canvas,data,200,200,-1,200,0)
		generateLine2(canvas,data,200,400,1,200,0)
	elif n == 24:
		generateLine2(canvas,data,250,250,-1,50,0)
		generateLine2(canvas,data,300,300,1,50,0)
		generateLine2(canvas,data,300,300,0,100,1)
	elif n == 25:
		generateLine2(canvas,data,200,200,0,125,0)
		generateLine2(canvas,data,200,300,0,125,0)
		generateLine2(canvas,data,200,300,.8,125,0)
		
	
def extensionRedrawAll(canvas,data):

	canvas.create_rectangle(0,0,data.width,data.height,fill = "black")
	canvas.create_rectangle(150,150,450,450,fill = "white")
	canvas.create_rectangle(700,200,1100,250,fill = "gold")
	canvas.create_rectangle(700,240,1100,250,fill = "orange")
	canvas.create_text(900,215,text = "Submit", font = "Cambria 20", fill = "black")
	if data.submitted == True:
		data.letterIndex = -1
		while(data.letterIndex < 25):
			data.letterIndex +=1
			makeLetter2(canvas,data,data.letterIndex)
			regression2(data,type)
		#print(data.letterScores)
		data.letterScores.sort()
		#print(data.letterScores[25][1])
	for i in range(len(data.userPoints)):
		#print(data.userPoints[i])
		if i > 1:
			if data.userPoints[i-1][0] != -1 and data.userPoints[i][0] != -1:
				canvas.create_line(data.userPoints[i-1][0],data.userPoints[i-1][1],data.userPoints[i][0],data.userPoints[i][1])
	canvas.update()
####################################
# Game mode
####################################
def generateLine(canvas, data, startx,starty,slope,length, type): #add in parameters initialx, initialy, slope
	initialx = startx
	initialy = starty
	for i in range(0, length):
		currentx = initialx + i
		currenty = initialy - (slope * i)
		data.points.append([currentx,currenty])
		if type == 0:
			canvas.create_line(currentx,currenty,currentx+1,currenty+1)
		elif type == 1: #vertical
			canvas.create_line(currenty,currentx,currenty+1,currentx+1)
	
	
def generateEllipse(canvas,data,centerx,centery,type, a, b):
	initialy = 0 
	initialx =  b
	k = 0
	growthFactor = .01
	while(k < b):
		k += growthFactor
		growthFactor += .1
		currentx = initialx - k
		currenty = ((a **2) - ((a**2)/(b**2))*(currentx**2)) ** .5
		currentPx = currentx + centerx
		currentOx = centerx - currentx
		currentPy = currenty + centery
		currentOy = centery - currenty
		if type == 0 or type == 2 or type == 3 or type == 5:
			canvas.create_line(currentPx,currentPy,currentPx+1,currentPy+1) #4th quadrant
			data.points.append([int(currentPx),int(currentPy)])
		if type == 2 or type == 3 or type == 4:
			canvas.create_line(currentPx,currentOy, currentPx+1,currentOy + 1) #1st quadrant
			data.points.append([int(currentPx),int(currentOy)])
		if type == 0 or type == 1 or type == 3 or type == 6:
			canvas.create_line(currentOx,currentPy,currentOx+1,currentPy + 1)  #3rd quadrant
			data.points.append([int(currentOx),int(currentPy)])
		if type == 1 or type == 3:
			canvas.create_line(currentOx,currentOy,currentOx+1,currentOy + 1) #2nd quadrant
			data.points.append([int(currentOx),int(currentOy)])
			
def makeLetter(canvas, data, n):
	data.points = list()
	#data.userPoints = list()
	if n == 0: 
		generateLine(canvas, data, 200,400,4,50, 0)
		generateLine(canvas,data, 250,200,-4,50, 0)
		generateLine(canvas, data, 225,300,0,50, 0)
	elif n == 1:
		generateLine(canvas,data,200,200,0,200, 1)
		generateEllipse(canvas,data,200,350,2,50,125) #bottom bubble of the b
		generateEllipse(canvas,data,200,250,2,50,100) #top bubble of the b	
	elif n == 2:
		generateEllipse(canvas,data,300,300,1,75,80)
		generateEllipse(canvas,data, 300, 250, 4, 25, 80)
		generateEllipse(canvas,data, 300, 350, 5, 25, 80)
	elif n == 3:
		generateLine(canvas,data,200,200,0,200,1)
		generateEllipse(canvas,data,200,300,2,100,125)
	elif n == 4:
		generateLine(canvas,data,200,200,0,200,1)
		generateLine(canvas,data,200, 200, 0,150,0)
		generateLine(canvas,data,200,300,0,150,0)
		generateLine(canvas,data,200,400,0,150,0)
	elif n == 5:
		generateLine(canvas,data,200,200,0,200,1)
		generateLine(canvas,data,200, 200, 0,150,0)
		generateLine(canvas,data,200,300,0,100,0)
	elif n == 6:
		generateEllipse(canvas, data, 300, 300, 1, 75, 80)
		generateEllipse(canvas, data, 300, 250, 4, 25, 80)
		generateEllipse(canvas, data, 300, 325, 5, 50, 80)
		generateLine(canvas, data, 300, 325, 0, 80, 0)
	elif n == 7:
		generateLine(canvas,data,200,300, 0, 200, 1)
		generateLine(canvas,data,200,200,0, 200, 1)
		generateLine(canvas, data,200,300, 0, 100, 0)
	elif n == 8:
		generateLine(canvas,data,200,300, 0, 200, 1)
		generateLine(canvas,data,250,200,0,100,0)
		generateLine(canvas,data,250,400,0,100,0)
	elif n == 9:
		generateLine(canvas,data,200,300, 0, 125, 1)
		generateEllipse(canvas, data,250,325,0,75,50)
		generateLine(canvas,data,250,200,0,100,0)
	elif n == 10:
		generateLine(canvas,data,200,200,0,200,1)
		generateLine(canvas,data,200,300,1.5,68,0)
		generateLine(canvas,data,200,300,-1.5,68,0)
	elif n == 11:
		generateLine(canvas,data,200,200,0,200,1)
		generateLine(canvas,data,200,400,0,100,0)
	elif n == 12:
		generateLine(canvas,data,200,400, 0, 200, 1)
		generateLine(canvas,data,200,200,0, 200, 1)
		generateLine(canvas,data,200,200,-.75,100,0)
		generateLine(canvas,data,300,275,.75,100,0)
	elif n == 13:
		generateLine(canvas,data,200,330, 0, 200, 1)
		generateLine(canvas,data,200,200,0, 200, 1)
		generateLine(canvas,data,200,200,-1.54,130,0)
	elif n == 14:
		generateEllipse(canvas,data,300,300,3,100,75)
	elif n == 15:
		generateLine(canvas,data,200,200,0,200, 1)
		generateEllipse(canvas,data,200,250,2,50,100)
	elif n == 16:
		generateEllipse(canvas,data,300,300,3,100,75)
		generateLine(canvas,data, 325, 325, -1.8, 50, 0 )
	elif n == 17:
		generateLine(canvas,data,200,200,0,200, 1)
		generateEllipse(canvas,data,200,250,2,50,100)
		generateLine(canvas, data, 200, 300, -1, 100, 0)
	elif n == 18:
		generateEllipse(canvas,data,300,250,1,50,75)
		generateEllipse(canvas,data,300,350,2,50,75)
		generateEllipse(canvas,data,300,225,4,25,75)
		generateEllipse(canvas,data,300,375,6,25,75)
	elif n == 19:
		generateLine(canvas,data,200,300, 0, 200, 1)
		generateLine(canvas,data,200,200,0,200,0)
	elif n == 20:
		generateEllipse(canvas,data,300,200,0,200,100)
	elif n == 21:
		generateLine(canvas,data,200,200,-2,100,0)
		generateLine(canvas,data,300,400,2,100,0)
	elif n == 22:
		generateLine(canvas,data,200,200,-4,50,0)
		generateLine(canvas,data,350,400,4,50,0)
		generateLine(canvas,data,250,400,2,50,0)
		generateLine(canvas,data,300,300,-2,50,0)
	elif n == 23:
		generateLine(canvas,data,200,200,-1,200,0)
		generateLine(canvas,data,200,400,1,200,0)
	elif n == 24:
		generateLine(canvas,data,250,250,-1,50,0)
		generateLine(canvas,data,300,300,1,50,0)
		generateLine(canvas,data,300,300,0,100,1)
	elif n == 25:
		generateLine(canvas,data,200,200,0,125,0)
		generateLine(canvas,data,200,300,0,125,0)
		generateLine(canvas,data,200,300,.8,125,0)
	
def regression(data, type):
	#print(data.userPoints)
	sortedUserPoints = copy.deepcopy(data.userPoints)
	sortedPoints = copy.deepcopy(data.points)
	sortedUserPoints.sort()
	sortedPoints.sort()
	#print(sortedUserPoints)
	
	#print(sortedUserPoints)
	if type == 1:
		epsilonx = 5
		epsilony = 5
	else:
		epsilonx = 5
		epsilony = 5
	sumErrorx = 0
	sumErrory = 0
	for i in range(0,len(data.points),1): 
		bigger = None
		biggerIndex = None
		smaller = None
		smallerIndex = None
		for j in range(len(data.userPoints)):
			if sortedUserPoints[j][0] > sortedPoints[i][0] and bigger == None:
				bigger = sortedUserPoints[j][0]
				biggerIndex = j
				smaller = sortedUserPoints[j-1][0]
				smallerIndex = j -1
				break
		if (bigger == None):
			closestIndex = len(sortedUserPoints) - 1
		elif (smallerIndex == -1):
			closestIndex = 0
		elif (bigger - sortedPoints[i][1]) < (sortedPoints[i][1]-smaller):
			closestIndex = biggerIndex
		else: closestIndex = smallerIndex
		#print(len(sortedPoints),i,len(sortedUserPoints),closestIndex)
		if abs(sortedPoints[i][0] - sortedUserPoints[closestIndex][0]) < epsilonx:
			pass
			
		else:
			print(sortedUserPoints[closestIndex][0])
			sumErrorx += 1
			continue
		bigger = None
		biggerIndex = None
		smaller = None
		smallerIndex = None
		possibleYs = list()
		closestYIndex = None
		for j in range(len(sortedUserPoints)):
			if sortedUserPoints[closestIndex][0] == sortedUserPoints[j][0]:
				possibleYs.append(sortedUserPoints[closestIndex][1])
		possibleYs.sort()	
		for k in range(len(possibleYs) - 1):
			if possibleYs[k + 1] > possibleYs[k] and bigger == None:
				bigger = possibleYs[k+1]
				biggerIndex = k + 1
				smaller = possibleYs[k]
				smallerIndex = k
				break
		if (bigger == None):
			closestYIndex = len(possibleYs) - 1
		elif ((bigger - possibleYs[biggerIndex]) < (possibleYs[smallerIndex]-smaller)):
			closestYIndex = biggerIndex
		else: closestYIndex = smallerIndex
		if (abs(sortedPoints[i][1] - possibleYs[closestYIndex]) < epsilony):
			pass
		else:
			sumErrory += 1
	denom = len(sortedPoints)
	data.score = (110 - (((sumErrory + sumErrorx )/(denom)) * 100))
	if data.score < 0:
		data.score = 0
	elif data.score > 100:
		data.score = 100
	
	if data.letterType == 1:	
		mean = 19.003
		stdev = 6.14868
	else: 
		mean = 14.4310
		stdev = 3.8143
	zscore = (data.score - mean)/stdev
	data.score = round((norm.cdf(zscore)) * 100, 2)
	print(data.score)
					
		
def gameMousePressed(event, data):
	if isInRectangle(data.buttonList[0],event.x,event.y): 
		regression(data, data.letterType)
	if isInRectangle(data.buttonList[1],event.x,event.y):
		data.letterIndex += 1
		data.userPoints = list()
	try: data.userPoints = data.userPoints + [[(event.x),(event.y)]]
	except: print("Failed")
	
	

def mouseRelease(event,data):
	data.userPoints = data.userPoints + [[-1,-1]]
def keyPressed(event, data):
	if event.keysym == "d":
		regression(data, data.letterType)
	if event.keysym == "c":
		data.userPoints = list()
def timerFired(data):
    pass

def gameRedrawAll(canvas, data):
	data.points = []

	#data.letterIndex += 1
	img = PhotoImage(file ="jungle.gif")
	canvas.img = img
	
	canvas.create_rectangle(0,0,data.width,data.height,fill = "black")
	img = PhotoImage(file ="jungle.gif")
	canvas.img = img
	canvas.create_rectangle(30,30,450,450,fill = "white")
	makeLetter(canvas,data,data.letterIndex)
	canvas.create_rectangle(700,200,1100,250,fill = "gold")
	canvas.create_rectangle(700,240,1100,250,fill = "orange")
	canvas.create_rectangle(700,300,1100,350,fill = "gold")
	canvas.create_rectangle(700,340,1100,350,fill = "orange")
	canvas.create_text(900,315,text = "Next", font = "Cambria 20", fill = "black")
	canvas.create_text(900,215,text = "Submit", font = "Cambria 20", fill = "black")
	canvas.create_rectangle(700,100,1100,150, fill = "yellow")
	if (data.score == None):
		scoreEntity = "uncomputed"
	else:
		scoreEntity = data.score
	canvas.create_text(900,125, text = "Your score was:" + str(scoreEntity)+ "%", fill = "black", font = "Cambria 20")
	
	for i in range(len(data.userPoints)):
		#print(data.userPoints[i])
		if i > 1:
			if data.userPoints[i-1][0] != -1 and data.userPoints[i][0] != -1:
				canvas.create_line(data.userPoints[i-1][0],data.userPoints[i-1][1],data.userPoints[i][0],data.userPoints[i][1])
	canvas.update()
####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
		
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)
    def mouseReleaseWrapper(event, canvas, data):
        mouseRelease(event, data)
        redrawAllWrapper(canvas, data)
		
    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<B1-Motion>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    root.bind("<Button-1>", lambda event:
                            mouseReleaseWrapper(event, canvas, data))							
    timerFiredWrapper(canvas, data)
    root.mainloop()  # blocks until window is closed	
    print("bye!")

run(width, height)