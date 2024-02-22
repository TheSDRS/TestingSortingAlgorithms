import mySorting
import time

List = [5, 2, 1, 7, 10, 25, 23]



def testQuicksort(aList: list):
	prevTime = time.perf_counter_ns()
	print(mySorting.quickSort(aList))
	print(time.perf_counter_ns() - prevTime)

def testHeapSort(aList: list):
	prevTime = time.perf_counter_ns()
	print(mySorting.heapSort(aList))
	print(time.perf_counter_ns() - prevTime)

def testMergeSort(aList: list):
	prevTime = time.perf_counter_ns()
	print(mySorting.mergeSort(aList))
	print(time.perf_counter_ns() - prevTime)

def testStable(aList: list):
	prevTime = time.perf_counter_ns()
	print(mySorting.stable(aList))
	print(time.perf_counter_ns() - prevTime)
	
testQuicksort(List)
print("\n")
testHeapSort(List)
print("\n")
testMergeSort(List)
print("\n")
testStable(List)
print("\n")