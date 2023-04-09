from tkinter import *
from functools import partial

def findWaitingTimef(processes, n, bt, wt, at):
    service_time = [0] * n
    service_time[0] = 0
    wt[0] = 0
    for i in range(1, n):
        service_time[i] = (service_time[i - 1] + bt[i - 1])
        wt[i] = service_time[i] - at[i]
        if (wt[i] < 0):
            wt[i] = 0
        

def findTurnAroundTimef(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]



def findavgTimef(processes, np, bt, at):
    n = int(np.get())

    wt = [0] * n
    tat = [0] * n


    findWaitingTimef(processes, n, bt, wt, at)

    findTurnAroundTimef(processes, n, bt, wt, tat)
    Label(window,text="Process BT AT WT TAT CT ").pack()

    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        compl_time = tat[i] + at[i]
        Label(window,text=""+ str(i + 1)+"    "+str(bt[i])+"     "+str(at[i])+"     "+str(wt[i])+"     "+str(tat[i])+"       "+str(compl_time)).pack()

    Label(window,text="Average waiting time =  "+str(total_wt /n)).pack()
    Label(window,text="Average turn around time = "+str(total_tat / n)).pack()

def findWaitingTimer(processes, n, bt,wt, quantum):
    rem_bt = [0] * n
    for i in range(n):
        rem_bt[i] = bt[i]
    t = 0 

    while(1):
        done = True
        for i in range(n):
            if (rem_bt[i] > 0) :
                done = False
                if (rem_bt[i] > quantum) :
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t = t + rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0
        if (done == True):
            break
			

def findTurnAroundTimer(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]


def findavgTimer(processes, np_entry, bt, quantum):
    n = int(np_entry.get())
    
    wt = [0] * n
    tat = [0] * n

    findWaitingTimer(processes, n, bt,wt, quantum)

    findTurnAroundTimer(processes, n, bt,wt, tat)

    Label(window,text="Process  BT  WT  TAT  ").pack()

    total_wt = 0
    total_tat = 0

    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        Label(window,text=""+ str(i+1)+"   "+str(bt[i])+"      "+str(wt[i])+"        "+str(tat[i])).pack()
    Label(window,text="Average waiting time = "+str(total_wt/n)).pack()
    Label(window,text="Average turn around time = "+str(total_tat/n)).pack()

        
    '''print(" ", i + 1, "\t\t", bt[i],"\t\t", wt[i], "\t\t", tat[i])

	print("\nAverage waiting time = %.5f "%(total_wt /n) )
	print("Average turn around time = %.5f "% (total_tat / n))'''




def proc():
    p = int(np_entry.get())
    for i in range(p):
        process.append(i)

def appendbt(en):
    e = int(en.get())
    burst_time.append(e)        

def appendat(en1):
    e1 = int(en1.get())
    arrival_time.append(e1)
    
def addbt():
    en = StringVar()
    Label(window,text="Enter the bt:").pack()
    en_entry = Entry(window,textvariable=en)
    en_entry.pack()
    bt = Button(window,text="Append BT",command=partial(appendbt,en_entry)).pack()

def addat():
    en1 = StringVar()
    Label(window,text="Enter the at:").pack()
    en1_entry = Entry(window,textvariable=en1)
    en1_entry.pack()
    at = Button(window,text="Append AT",command=partial(appendat,en1_entry)).pack()

window = Tk(screenName=None,  baseName=None,  className="FCFS",  useTk=1)

np = StringVar()
Label(window, text= "Number of processes:").pack()
np_entry = Entry(window,textvariable=np)
np_entry.pack()
process = []

pro = Button(window,text="Add process numbers",command=proc).pack()

burst_time = []
add = Button(window,text="Add BT",command=addbt).pack()

arrival_time = []
add = Button(window,text="Add AT",command=addat).pack()

quat = 2
calc = Button(window,text="FCFS",command=partial(findavgTimef,process,np_entry,burst_time,arrival_time)).pack()

cal = Button(window,text="RR",command=partial(findavgTimer,process,np_entry,burst_time,quat)).pack()
window.mainloop()
