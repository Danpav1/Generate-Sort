# @author Daniel Pavenko
# @date 03/08/24
# A python program that reads text files, sorts them using custom quicksort, mergesort & heapsort, 
# and calculates the efficiency via execution time for each sort.

import os
import time
import statistics

# Creates the results directory hierarchy
def createResultsDirectories():
    baseDir = "results"
    sizes = ["small", "medium", "large"]
    types = ["unsorted", "sorted", "reverse_sorted"]
  
    for size in sizes:
        for sortType in types:
            dirPath = os.path.join(baseDir, size, sortType)
            os.makedirs(dirPath, exist_ok=True)

# Processes text files by sorting them, measuring their efficiency, and writing that measurment to a results file
def processTextFiles():
    readDir = "dataset"
    writeDir = "results"
    sizes = ["small", "medium", "large"]
    types = ["unsorted", "sorted", "reverse_sorted"]
    sortFunctions = {'quickSort': quickSort, 'mergeSort': mergeSort, 'heapSort': heapSort}

    for size in sizes:
        for sortType in types:
            # Dups all keys from sortFunctions and makes values empty lists
            runTimes = {sortName: [] for sortName in sortFunctions.keys()}
            # To minimze I/O, we put data into resultContent (instead of writing right as we get the data) and 
            # write resultContent into the file at the end
            resultContent = []

            # Read and put input data into integer list
            for i in range(1, 31):
                fileName = f"{size}_{sortType}_{i}.txt"
                readFilePath = os.path.join(readDir, size, sortType, fileName)
                with open(readFilePath, 'r') as file:
                    integers = [int(num) for num in file.read().split()]

                # Calls sortAndMeasure on integer list, gets return val (runTime) and puts it into the correct key value
                # pair in runTimes, adds result data line corrresponding to the sort just ran and runTime of that sort 
                for sortName, sortFunc in sortFunctions.items():
                    runTimeMS = sortAndMeasure(list(integers), sortFunc)
                    runTimes[sortName].append(runTimeMS)
                    if (sortFunc == heapSort):
                        resultContent.append(f"{sortName} - {fileName} - {runTimeMS:.4f} ms\n\n")
                    else:
                      resultContent.append(f"{sortName} - {fileName} - {runTimeMS:.4f} ms\n")

            # Calculate and append statistics to the end of the file
            for sortName, times in runTimes.items():
                mean = statistics.mean(times)
                stdev = statistics.stdev(times)
                resultContent.append(f"{sortName} mean: {mean:.4f} ms, standard deviation: {stdev:.4f}\n")

            # Write results to file
            writeFilePath = os.path.join(writeDir, size, sortType, f"{size}_{sortType}_results.txt")
            with open(writeFilePath, 'w') as file:
                file.writelines(resultContent)
     
# Calls appropriate sort and measures execution time of said sort
def sortAndMeasure(integers, sortFunc):
    startTime = time.perf_counter()
    sortFunc(integers)
    endTime = time.perf_counter()
    return (endTime - startTime) * 1000

# Sorts a list of integers using quicksort
def quickSort(integers):
  sorted(integers) # Test implementation

# Sorts a list of integers using mergesort
def mergeSort(integers):
  sorted(integers) # Test implementation

# Sorts a list of integers using heapsort
def heapSort(integers):
  sorted(integers) # Test implementation

# Check if being run directly or imported
if __name__ == "__main__":
    createResultsDirectories()
    processTextFiles()