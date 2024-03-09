# @author Daniel Pavenko
# @date 03/08/24
# A python program that reads text files, sorts them using custom quicksort, mergesort & heapsort, 
# and calculates the efficiency via execution time for each sort.

import os
import time
import statistics

# Creates the results directory hierarchy
def createResultsDirectories():
    base_dir = "results"
    sizes = ["small", "medium", "large"]
    types = ["unsorted", "sorted", "reverse_sorted"]
  
    for size in sizes:
        for sort_type in types:
            dir_path = os.path.join(base_dir, size, sort_type)
            os.makedirs(dir_path, exist_ok=True)

# Processes text files by sorting them, measuring their efficiency, and writing that measurment to a results file
def processTextFiles():
    readDir = "dataset"
    writeDir = "results"
    sizes = ["small", "medium", "large"]
    types = ["unsorted", "sorted", "reverse_sorted"]
    
    for size in sizes:
        for sortType in types:
            quickSortRunTimes, mergeSortRunTimes, heapSortRunTimes = [], [], []
            for i in range(1, 31):
                readFileName = f"{size}_{sortType}_{i}.txt"
                readFilePath = os.path.join(readDir, size, sortType, readFileName)
                writeFileName = f"{size}_{sortType}_results.txt"
                writeFilePath = os.path.join(writeDir, size, sortType, writeFileName)
                
                with open(readFilePath, 'r') as file:
                    integers = [int(num) for num in file.read().split()]
                
                # Overwrites old data
                if (i == 1):
                  with open(writeFilePath, 'w'):
                    pass
                
                # Quicksort
                startTime = time.perf_counter()
                quickSort(integers)
                endTime = time.perf_counter()
                runTimeMS = (endTime - startTime) * 1000
                quickSortRunTimes.append(runTimeMS)
                with open(writeFilePath, 'a') as file:
                  file.write(f"quickSort - {readFileName} - {runTimeMS:.4f} ms\n")
                    
                # Mergesort
                startTime = time.perf_counter()
                mergeSort(integers)
                endTime = time.perf_counter()
                runTimeMS = (endTime - startTime) * 1000
                mergeSortRunTimes.append(runTimeMS)
                with open(writeFilePath, 'a') as file:
                  file.write(f"mergeSort - {readFileName} - {runTimeMS:.4f} ms\n")  
                  
                # Heapsort
                startTime = time.perf_counter()
                heapSort(integers)
                endTime = time.perf_counter()
                runTimeMS = (endTime - startTime) * 1000
                heapSortRunTimes.append(runTimeMS)
                with open(writeFilePath, 'a') as file:
                  file.write(f"heapSort - {readFileName} - {runTimeMS:.4f} ms\n\n")
    
                if (i == 30): # Makes sure we're at the last iteration
                  # Calculate standard deviation and mean and put them into the results file
                  with open(writeFilePath, 'a') as file:
                    file.write(f"quickSort mean: {statistics.mean(quickSortRunTimes):.4f}\n")
                    file.write(f"mergeSort mean: {statistics.mean(mergeSortRunTimes):.4f}\n")
                    file.write(f"heapSort mean: {statistics.mean(heapSortRunTimes):.4f}\n")
                    file.write(f"quickSort stdev: {statistics.stdev(quickSortRunTimes):.4f}\n")
                    file.write(f"mergeSort stdev: {statistics.stdev(mergeSortRunTimes):.4f}\n")
                    file.write(f"heapSort stdev: {statistics.stdev(heapSortRunTimes):.4f}\n")

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