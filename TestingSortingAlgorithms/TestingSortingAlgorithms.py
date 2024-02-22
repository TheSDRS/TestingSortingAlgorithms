import mySorting, time, random, matplotlib.pyplot as plt
from tkinter import *


def testSortingSpeedRandom(algorithm: str):
    durationTime = []
    unsortedList = []
    for i in range(1, int(txt.get())):
        unsortedList.append(random.randint(1, 1000))
        prevTime = time.perf_counter_ns()
        if algorithm == "quicksort":
            mySorting.quickSort(unsortedList)
        elif algorithm == "heapsort":
            mySorting.heapSort(unsortedList)
        elif algorithm == "mergesort":
            mySorting.mergeSort(unsortedList)
        elif algorithm == "stable":
            mySorting.stable(unsortedList)
        durationTime.append(time.perf_counter_ns() - prevTime)
    return durationTime


def testSortingSpeedList(algorithm: str, aList: list):
    durationTime = []
    unsortedList = []
    for i in aList:
        unsortedList.append(i)
        prevTime = time.perf_counter_ns()
        if algorithm == "quicksort":
            mySorting.quickSort(unsortedList)
        elif algorithm == "heapsort":
            mySorting.heapSort(unsortedList)
        elif algorithm == "mergesort":
            mySorting.mergeSort(unsortedList)
        elif algorithm == "stable":
            mySorting.stable(unsortedList)
        durationTime.append(time.perf_counter_ns() - prevTime)
    return durationTime
def plotRandom():
    plt.close()
    plt.plot(testSortingSpeedRandom("quicksort"), label="quicksort")
    plt.plot(testSortingSpeedRandom("heapsort"), label="heapsort")
    plt.plot(testSortingSpeedRandom("mergesort"), label="mergesort")
    plt.plot(testSortingSpeedRandom("stable"), label="stable")
    plt.legend()
    plt.title("Random Plot")
    plt.show()


def plotList():
    plt.close()
    rndList = []
    for i in range(1, int(txt.get())):
        rndList.append(random.randint(1, 1000))
    plt.plot(testSortingSpeedList("quicksort", rndList), label="quicksort")
    plt.plot(testSortingSpeedList("heapsort", rndList), label="heapsort")
    plt.plot(testSortingSpeedList("mergesort", rndList), label="mergesort")
    plt.plot(testSortingSpeedList("stable", rndList), label="stable")
    plt.legend()
    plt.title("List Plot")
    plt.show()


root = Tk()

root.title("Select Test")
root.geometry("350x200")

lbl = Label(root, text="Please Select a test")
lbl.place(relx=0.5, rely=0.1, anchor=CENTER)

lbl2 = Label(root, text="Iterations:")
lbl2.place(relx=0.3, rely=0.25, anchor=CENTER)
txt = Entry(root, width= 10)
txt.place(relx=0.5, rely=0.25, anchor=CENTER)

btn1 = Button(root, text="Test With Defined List", fg="black", command=plotList)
btn1.place(relx=0.25, rely=0.5, anchor=CENTER)

btn2 = Button(root, text="Test With Random List", fg="black", command=plotRandom)
btn2.place(relx=0.75, rely=0.5, anchor=CENTER)

root.mainloop()