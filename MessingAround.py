# messing-around

from tkinter import *


def init(data):
	data.points = list()
	data.userPoints = list()


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
			data.points.append([currentPx,currentPy])
		if type == 2 or type == 3 or type == 4:
			canvas.create_line(currentPx,currentOy, currentPx+1,currentOy + 1) #1st quadrant
			data.points.append([currentPx,currentOy])
		if type == 0 or type == 1 or type == 3 or type == 6:
			canvas.create_line(currentOx,currentPy,currentOx+1,currentPy + 1)  #3rd quadrant
			data.points.append([currentOx,currentPy])
		if type == 1 or type == 3:
			canvas.create_line(currentOx,currentOy,currentOx+1,currentOy + 1) #2nd quadrant
			data.points.append([currentOx,currentOy])
			
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
	
	
def mousePressed(event, data):
	data.userPoints = data.userPoints + [[event.x,event.y]]

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
	data.points = []
	"""
	generateLine(canvas, data, 200,400,1.5,100, 0)
	generateLine(canvas,data, 300,252,-1.5,100, 0)
	generateLine(canvas, data, 250,325,0,100, 0)
	"""
	#generateLine(canvas, data, 250,325,0,100, 1)
	#generateEllipse(canvas,data, 200, 200, 4, 50, 75)
	#makeLetter(canvas, data, 0)
	#makeLetter(canvas, data, 1)
	#makeLetter(canvas,data, 2)
	#makeLetter(canvas,data, 3)
	#makeLetter(canvas,data, 0)
	makeLetter(canvas,data,1)
	
	for i in range(len(data.userPoints)):
		#print(data.userPoints[i])
		if i > 1:
			canvas.create_line(data.userPoints[i-1][0],data.userPoints[i-1][1],data.userPoints[i][0],data.userPoints[i][1])
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
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1300, 600)