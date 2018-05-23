import tkinter as tk
import time
import matplotlib.pyplot as plt


window = tk.Tk()
window.title("Time Tracker")
window.geometry("400x400")


#---global varialbles --#
timeLine = time.time()
timeStamps = [timeLine]

workSeg = []
leisureSeg = []
breakSeg = []

workStat = False
leisureStat = False
breakStat = False

#--funcitons--#
def startWork():
    global leisureStat
    global leisureSeg
    global breakStat
    global breakSeg
    global workStat
    global workSeg
    global timeStamps
    global timeLine

    newTime = time.time()
    #time it took
    resultTime = newTime - timeStamps[len(timeStamps)-1]
    testLabel.config(text= resultTime)

    timeStamps.append(newTime)

    if leisureStat == True:
        leisureSeg.append(resultTime)
        leisureStat = False
    elif breakStat == True:
        breakSeg.append(resultTime)
        breakStat = False
    elif workStat == True:
        workSeg.append(resultTime)
        workStat = True
    
    if workStat == False:
        workStat = True

def startLeisure():
    global leisureStat
    global leisureSeg
    global breakStat
    global breakSeg
    global workStat
    global workSeg
    global timeStamps
    global timeLine

    newTime = time.time()
    #time it took
    resultTime = newTime - timeStamps[len(timeStamps)-1]
    testLabel.config(text= resultTime)

    timeStamps.append(newTime)

    if leisureStat == True:
        leisureSeg.append(resultTime)
        leisureStat = True
    elif breakStat == True:
        breakSeg.append(resultTime)
        breakStat = False
    elif workStat == True:
        workSeg.append(resultTime)
        workStat = False
    
    if leisureStat == False:
        leisureStat = True

def startBreak():
    global leisureStat
    global leisureSeg
    global breakStat
    global breakSeg
    global workStat
    global workSeg
    global timeStamps
    global timeLine

    newTime = time.time()
    #time it took
    resultTime = newTime - timeStamps[len(timeStamps)-1]
    testLabel.config(text= resultTime)

    timeStamps.append(newTime)

    if leisureStat == True:
        leisureSeg.append(resultTime)
        leisureStat = False
    elif breakStat == True:
        breakSeg.append(resultTime)
        breakStat = True
    elif workStat == True:
        workSeg.append(resultTime)
        workStat = False
    
    if breakStat == False:
        breakStat = True

def endSession():
    global leisureStat
    global leisureSeg
    global breakStat
    global breakSeg
    global workStat
    global workSeg
    global timeStamps
    global timeLine

    finalTime = time.time()
    totalTime = finalTime - timeLine
    totalWork = 0
    for i in workSeg:
        totalWork += i
    totalLeisure = 0
    for l in leisureSeg:
        totalLeisure += l
    totalBreak = 0
    for e in breakSeg:
        totalBreak += e

    print(workSeg)
    
    workPercent = (totalWork/totalTime)*100
    leisurePercent = (totalLeisure/totalTime)*100
    breakPercent = 100-workPercent-leisurePercent
    
    print("work percentage {}, leisure percentage {}, break percentage{}".format(workPercent,leisurePercent,breakPercent))

    testLabel.config(text='Session Total time = {} \
    \n Total working hours = {} \n Total Leisure hours = {} \
    \n Total Break hours = {}'.format(totalTime,totalWork,totalLeisure,totalBreak))

    labels = ['Work','Leisure','Break']
    sizes = [workPercent,leisurePercent,breakPercent]
    fig1,ax1 =plt.subplots()
    ax1.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
    ax1.axis('equal')
    plt.show()


#--test label --#
testLabel = tk.Label(text= "time display")
testLabel.pack()

#--Work Button --#
workButton = tk.Button(text="Work", command=startWork)
workButton.pack()

#--Leisure Button --#
leisureButton = tk.Button(text="Lesiure", command=startLeisure)
leisureButton.pack()


#--Break Button --#
breakButton = tk.Button(text="Break",command= startBreak)
breakButton.pack()

#--End Session--#
endSessionButton = tk.Button(text="End today's Session", command=endSession)
endSessionButton.pack()



window.mainloop()