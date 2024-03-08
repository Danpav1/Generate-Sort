# @author Daniel Pavenko
# @date 03/07/24
# A python program that generates 90 text files (30 - 10,000 nums, 30, - 100,000 nums,
# 30 - 1,000,000 nums) which are filled with random numbers in range 0 <= x <= 9,999.

import os
import random
import sys
from multiprocessing import Process

# Main method
def main():
  runGenerator()
  return

# Calls generateSmall, generateMedium and generateLarge in parallel to create a total of
# 90 text files.
def runGenerator():
  print("Generating...")
    
  # Create processes 
  generateSmallProcess = Process(target=generateSmall)
  generateMediumProcess = Process(target=generateMedium)
  generateLargeProcess = Process(target=generateLarge)
  
  # Start processes
  generateSmallProcess.start()
  generateMediumProcess.start()
  generateLargeProcess.start()
  
  # Wait for processes to complete
  generateSmallProcess.join()
  generateMediumProcess.join()
  generateLargeProcess.join()
  
  print("All files done.")
  return

# Generates 30 text files in our directory and fills them with 10,000 numbers in range
# 0 <= x <= 9,999.
def generateSmall():
    smallDir = "/Users/danielpavenko/university/SPRING2024/Algo/P1/text_files/small"
    
    if not os.path.exists(smallDir):
        os.makedirs(smallDir)
    
    for i in range(30):
        fileName = f"md_{i + 1}.txt"
        filePath = os.path.join(smallDir, fileName)
        with open(filePath, 'w') as file:
            numbers = [str(random.randint(0, 9999)) for _ in range(10000)]
            file.write(" ".join(numbers))
    print("\tSmall files done.")

# Generates 30 text files in our directory and fills them with 100,000 numbers in range
# 0 <= x <= 9,999.
def generateMedium():
    mediumDir = "/Users/danielpavenko/university/SPRING2024/Algo/P1/text_files/medium"
    
    if not os.path.exists(mediumDir):
        os.makedirs(mediumDir)
    
    for i in range(30):
        fileName = f"md_{i + 1}.txt"
        filePath = os.path.join(mediumDir, fileName)
        with open(filePath, 'w') as file:
            numbers = [str(random.randint(0, 9999)) for _ in range(100000)]
            file.write(" ".join(numbers))
    print("\tMedium files done.")


# Generates 30 text files in our directory and fills them with 1,000,000 numbers in range
# 0 <= x <= 9,999.
def generateLarge():
    largeDir = "/Users/danielpavenko/university/SPRING2024/Algo/P1/text_files/large"
    
    if not os.path.exists(largeDir):
        os.makedirs(largeDir)
    
    for i in range(30):
        fileName = f"lg_{i + 1}.txt"
        filePath = os.path.join(largeDir, fileName)
        with open(filePath, 'w') as file:
            numbers = [str(random.randint(0, 9999)) for _ in range(1000000)]
            file.write(" ".join(numbers))
    print("\tLarge files done.")


# Check if being run directly or imported
if __name__ == "__main__":
    main()
      