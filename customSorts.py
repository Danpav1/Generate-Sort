# @author Daniel Pavenko
# @date 03/08/24
# A python program that reads text files, sorts them using custom quicksort, mergesort & heapsort, 
# and calculates the efficiency via execution time for each sort.

import os

# Main method
def main():
  run()
  return

# Starts the process of reading each of the 270 text files
def run():
  # Creates the test files
  createResultsFiles()
  
  # Starts the test process
  handleTextFiles()

# Creates the results folder heirarchy
def createResultsFiles():
  resultsDir = "/Users/danielpavenko/university/SPRING2024/Algo/P1/results"
  folders = ["small", "medium", "large"]
  subFolders = ["unsorted", "sorted", "reverse_sorted"]
  
  # Check if results exist, create it if not
  if not os.path.exists(resultsDir):
    os.makedirs(resultsDir)
  
  # Checks and creates all folders in results
  for folder in folders:
    folderPath = os.path.join(resultsDir, folder)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    for subFolder in subFolders:
      subFolderPath = os.path.join(folderPath, subFolder)
      if not os.path.exists(subFolderPath):
        os.makedirs(subFolderPath)
    
# Reads the input text files and puts all data into list, calls appropriate sorts with list as param, then writes
# execution times of said sorts into respective results file
def handleTextFiles():
  readDir = "/Users/danielpavenko/university/SPRING2024/Algo/P1/dataset"
  writeDir = "/Users/danielpavenko/university/SPRING2024/Algo/P1/results"
  folders = ["small", "medium", "large"]
  subFolders = ["unsorted", "sorted", "reverse_sorted"]
  fileSizeName = ["sm", "md", "lg"]
  
  # Reads
  for idx, folder in enumerate(folders):
    folderPath = os.path.join(readDir, folder)
    for subFolder in subFolders:
      subFolderPath = os.path.join(folderPath, subFolder)
      for i in range(30):
        fileName = f"{fileSizeName[idx]}_{subFolder}_{i + 1}.txt"
        filePath = os.path.join(subFolderPath, fileName)
        with open(filePath, 'r') as file:
          content = file.read()
          integers = [int(i) for i in content.split()]
          quickSort(integers)
          mergeSort(integers)
          heapSort(integers)

# Sorts a list of integers using quicksort and returns execution time.
def quickSort(integers):
  print("Quicksort")
  return 0

# Sorts a list of integers using mergesort and returns execution time.
def mergeSort(integers):
  print("Mergesort")
  return 0

# Sorts a list of integers using heapsort and returns execution time.
def heapSort(integers):
  print("Heapsort")
  return 0

# Check if being run directly or imported while calculating execution time.
if __name__ == "__main__":
    main()