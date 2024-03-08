# @author Daniel Pavenko
# @date 03/07/24
# A python program that generates 270 text files (90 - 10,000 nums, 90, - 100,000 nums,
# 90 - 1,000,000 nums) which are filled with random numbers in range 0 <= x <= 9,999.

import os
import random
import time

from multiprocessing import Process

# Main method
def main():
  runGenerator()
  return

# Calls generateSmall, generateMedium and generateLarge in parallel to create a total of
# 270 text files.
def runGenerator():
  print("Generating...")
  
  # Record the start time
  startTime = time.perf_counter()
    
  # Create processes 
  generateSmallProcess = Process(target=generateSmallUnsorted)
  generateMediumProcess = Process(target=generateMediumUnsorted)
  generateLargeProcess = Process(target=generateLargeUnsorted)
  
  # Start processes
  generateSmallProcess.start()
  generateMediumProcess.start()
  generateLargeProcess.start()
  
  # Wait for processes to complete
  generateSmallProcess.join()
  generateMediumProcess.join()
  generateLargeProcess.join()
  
  # Record the end time
  endTime = time.perf_counter()
  
  # Calculate the difference in time in milliseconds
  runTimeS = (endTime - startTime)
  runTimeMS = runTimeS * 1000
  print("All files done.")
  print(f"Execution time: {runTimeMS:.2f} ms or {runTimeS:.2f} sec")

# Generates unsorted text files in our directory and fills them with 10,000 numbers in range
# 0 <= x <= 9,999.
def generateSmallUnsorted():
    smallDirUnsorted = "/Users/danielpavenko/university/SPRING2024/Algo/P1/text_files/small/unsorted"
    
    if not os.path.exists(smallDirUnsorted):
        os.makedirs(smallDirUnsorted)
    
    for i in range(30):
        fileName = f"sm_unsorted_{i + 1}.txt"
        filePath = os.path.join(smallDirUnsorted, fileName)
        with open(filePath, 'w') as file:
            integers = [str(random.randint(0, 9999)) for _ in range(10000)]
            file.write(" ".join(integers))
            
    print("\tUnsorted small files done.")
    
    generateSmallSorted(smallDirUnsorted)
    
# Duplicates, sorts and places the now sorted files into new directory
def generateSmallSorted(smallDirUnsorted):
    smallDirSorted = "/Users/danielpavenko/university/SPRING2024/Algo/P1/text_files/small/sorted"
    
    if not os.path.exists(smallDirSorted):
        os.makedirs(smallDirSorted)
    
    for i in range(30):
        fileName = f"sm_unsorted_{i + 1}.txt"
        filePath = os.path.join(smallDirUnsorted, fileName)
        with open(filePath, 'r') as file:
          content = file.read()
          
        integers = [int(i) for i in content.split()]
        
        sortedIntegers = sorted(integers)
        
        fileName = f"sm_sorted_{i + 1}.txt"
        filePath = os.path.join(smallDirSorted, fileName)
        
        with open(filePath, 'w') as file:
            file.write(' '.join(map(str, sortedIntegers)))
          
    print("\tSorted small files done.")  
  
    generateSmallReverseSorted(smallDirSorted)
    
# Duplicates, reverse sorts and places the now reverse sorted files into new directory
def generateSmallReverseSorted(smallDirSorted):
    smallDirReverseSorted = "/Users/danielpavenko/university/SPRING2024/Algo/P1/text_files/small/reverse_sorted"
    
    if not os.path.exists(smallDirReverseSorted):
        os.makedirs(smallDirReverseSorted)
    
    for i in range(30):
        fileName = f"sm_sorted_{i + 1}.txt"
        filePath = os.path.join(smallDirSorted, fileName)
        with open(filePath, 'r') as file:
          content = file.read()
          
        integers = [int(i) for i in content.split()]
        
        reverseSortedIntegers = sorted(integers, reverse = True)
        
        fileName = f"sm_reverseSorted_{i + 1}.txt"
        filePath = os.path.join(smallDirReverseSorted, fileName)
        
        with open(filePath, 'w') as file:
            file.write(' '.join(map(str, reverseSortedIntegers)))
           
    print("\tReverse sorted small files done.\n")

# Generates unsorted text files in our directory and fills them with 100,000 numbers in range
# 0 <= x <= 9,999.
def generateMediumUnsorted():
    mediumDirUnsorted = "/Users/danielpavenko/university/SPRING2024/Algo/P1/text_files/medium/unsorted"
    
    if not os.path.exists(mediumDirUnsorted):
        os.makedirs(mediumDirUnsorted)
    
    for i in range(30):
        fileName = f"md_unsorted_{i + 1}.txt"
        filePath = os.path.join(mediumDirUnsorted, fileName)
        with open(filePath, 'w') as file:
            integers = [str(random.randint(0, 9999)) for _ in range(100000)]
            file.write(" ".join(integers))
            
    print("\tUnsorted medium files done.")
    
    generateMediumSorted(mediumDirUnsorted)
    
# Duplicates, sorts and places the now sorted files into new directory
def generateMediumSorted(mediumDirUnsorted):
    mediumDirSorted = "/Users/danielpavenko/university/SPRING2024/Algo/P1/text_files/medium/sorted"
    
    if not os.path.exists(mediumDirSorted):
        os.makedirs(mediumDirSorted)
    
    for i in range(30):
        fileName = f"md_unsorted_{i + 1}.txt"
        filePath = os.path.join(mediumDirUnsorted, fileName)
        with open(filePath, 'r') as file:
          content = file.read()
          
        integers = [int(i) for i in content.split()]
        
        sortedIntegers = sorted(integers)
        
        fileName = f"md_sorted_{i + 1}.txt"
        filePath = os.path.join(mediumDirSorted, fileName)
        
        with open(filePath, 'w') as file:
            file.write(' '.join(map(str, sortedIntegers)))
          
    print("\tSorted medium files done.")  
  
    generateMediumReverseSorted(mediumDirSorted)
    
# Duplicates, reverse sorts and places the now reverse sorted files into new directory
def generateMediumReverseSorted(mediumDirSorted):
    mediumDirReverseSorted = "/Users/danielpavenko/university/SPRING2024/Algo/P1/text_files/medium/reverse_sorted"
    
    if not os.path.exists(mediumDirReverseSorted):
        os.makedirs(mediumDirReverseSorted)
    
    for i in range(30):
        fileName = f"md_sorted_{i + 1}.txt"
        filePath = os.path.join(mediumDirSorted, fileName)
        with open(filePath, 'r') as file:
          content = file.read()
          
        integers = [int(i) for i in content.split()]
        
        reverseSortedIntegers = sorted(integers, reverse = True)
        
        fileName = f"md_reverseSorted_{i + 1}.txt"
        filePath = os.path.join(mediumDirReverseSorted, fileName)
        
        with open(filePath, 'w') as file:
            file.write(' '.join(map(str, reverseSortedIntegers)))
           
    print("\tReverse sorted medium files done.\n")
    
# Generates unsorted text files in our directory and fills them with 1,000,000 numbers in range
# 0 <= x <= 9,999.
def generateLargeUnsorted():
    largeDirUnsorted = "/Users/danielpavenko/university/SPRING2024/Algo/P1/text_files/large/unsorted"
    
    if not os.path.exists(largeDirUnsorted):
        os.makedirs(largeDirUnsorted)
    
    for i in range(30):
        fileName = f"lg_unsorted_{i + 1}.txt"
        filePath = os.path.join(largeDirUnsorted, fileName)
        with open(filePath, 'w') as file:
            integers = [str(random.randint(0, 9999)) for _ in range(1000000)]
            file.write(" ".join(integers))
            
    print("\tUnsorted large files done.")
    
    generateLargeSorted(largeDirUnsorted)
    
# Duplicates, sorts and places the now sorted files into new directory
def generateLargeSorted(largeDirUnsorted):
    largeDirSorted = "/Users/danielpavenko/university/SPRING2024/Algo/P1/text_files/large/sorted"
    
    if not os.path.exists(largeDirSorted):
        os.makedirs(largeDirSorted)
    
    for i in range(30):
        fileName = f"lg_unsorted_{i + 1}.txt"
        filePath = os.path.join(largeDirUnsorted, fileName)
        with open(filePath, 'r') as file:
          content = file.read()
          
        integers = [int(i) for i in content.split()]
        
        sortedIntegers = sorted(integers)
        
        fileName = f"lg_sorted_{i + 1}.txt"
        filePath = os.path.join(largeDirSorted, fileName)
        
        with open(filePath, 'w') as file:
            file.write(' '.join(map(str, sortedIntegers)))
          
    print("\tSorted large files done.")  
  
    generateLargeReverseSorted(largeDirSorted)
    
# Duplicates, reverse sorts and places the now reverse sorted files into new directory
def generateLargeReverseSorted(largeDirSorted):
    largeDirReverseSorted = "/Users/danielpavenko/university/SPRING2024/Algo/P1/text_files/large/reverse_sorted"
    
    if not os.path.exists(largeDirReverseSorted):
        os.makedirs(largeDirReverseSorted)
    
    for i in range(30):
        fileName = f"lg_sorted_{i + 1}.txt"
        filePath = os.path.join(largeDirSorted, fileName)
        with open(filePath, 'r') as file:
          content = file.read()
          
        integers = [int(i) for i in content.split()]
        
        reverseSortedIntegers = sorted(integers, reverse = True)
        
        fileName = f"lg_reverseSorted_{i + 1}.txt"
        filePath = os.path.join(largeDirReverseSorted, fileName)
        
        with open(filePath, 'w') as file:
            file.write(' '.join(map(str, reverseSortedIntegers)))
           
    print("\tReverse sorted large files done.")

# Check if being run directly or imported
if __name__ == "__main__":
    main()
      