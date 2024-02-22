import numpy as np

def quickSort(aList: list):
	aNumpyArray = np.array(aList)
	sortedArray = np.sort(aNumpyArray, -1, 'quicksort', None)
	returnList = list(sortedArray)
	return returnList

def heapSort(aList: list):
	aNumpyArray = np.array(aList)
	sortedArray = np.sort(aNumpyArray, -1, 'heapsort', None)
	returnList = list(sortedArray)
	return returnList

def mergeSort(aList: list):
	aNumpyArray = np.array(aList)
	sortedArray = np.sort(aNumpyArray, -1, 'mergesort', None)
	returnList = list(sortedArray)
	return returnList

def stable(aList: list):
	aNumpyArray = np.array(aList)
	sortedArray = np.sort(aNumpyArray, -1, 'stable', None)
	returnList = list(sortedArray)
	return returnList