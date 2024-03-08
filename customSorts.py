# @author Daniel Pavenko
# @date 03/08/24
# A python program that reads text files, sorts them using custom quicksort, mergesort & heapsort, 
# and calculates the efficiency via execution time for each sort.

import os
import time

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
            for i in range(1, 31):
                file_name = f"{size}_{sortType}_{i}.txt"
                file_path = os.path.join(readDir, size, sortType, file_name)
                with open(file_path, 'r') as file:
                    integers = [int(num) for num in file.read().split()]
                
                start_time = time.time()
                quickSort(integers)
                duration = time.time() - start_time
                # -- write to file logic here, method call maybe? --     
                start_time = time.time()
                mergeSort(integers)
                duration = time.time() - start_time
                # -- write to file logic here, method call maybe? --   
                start_time = time.time()
                heapSort(integers)
                duration = time.time() - start_time
                # -- write to file logic here, method call maybe? --  

# Sorts a list of integers using quicksort
def quickSort(integers):
  print("Quicksort")

# Sorts a list of integers using mergesort
def mergeSort(integers):
  print("Mergesort")

# Sorts a list of integers using heapsort
def heapSort(integers):
  print("Heapsort")

# Check if being run directly or imported
if __name__ == "__main__":
    createResultsDirectories()
    processTextFiles()