# Progamming assignment 1:

## Introduction

This project is part of the Design and Analysis of Algorithms course and focuses on
generating a dataset to analyze the efficiency of various sorting algorithms. 
The primary objective is to create 270 text files populated with random integers within
the range [0 - 10,000), and then apply different sorting techniques to evaluate their
performance under various conditions.

## Dataset Overview

All files in the dataset are text files (.txt)

- Small files: Each containing 10,000 random integers.
- Medium files: Each containing 100,000 random integers.
- Large files: Each containing 1,000,000 random integers.

In total, each category consists of 90 files (total 270), split into three equal parts based on their
sorting order:

- Unsorted: Files in their original, unsorted state.
- Sorted (High to Low): Files sorted in descending order.
- Sorted (Low to High): Files sorted in ascending order.

The files within this dataset will be used as input for the custom sort implementations.

## Sorting Algorithms

The files generated will be sorted using the following custom algorithms to benchmark their
efficiency:

- Quicksort
- Mergesort
- Heapsort

NOTE: When sorted, the sorted order is considered (Low to High)

## Usage

Step by step process on how to run this program.

###### Change directory to the desired repository location:
	cd desired-dir-here

###### Clone the repository:
	git clone https://github.com/Danpav1/Generate-Sort.git

 ###### Change directory to be inside the newly cloned repository:
	cd project-dir-here

###### Create virtual environment and activate it:
	# For macOS and Linux
 	python3 -m venv .venv
	source .venv/bin/activate
###### 
	# For Windows
	python -m venv .venv
	.\.venv\Scripts\activate

###### Generate the dataset:
	python3 ./datasetGenerator.py

This will create and fill the dataset folder heirarchy (270 generated text files).

The dataset folder can be found at: General-Sort/dataset. The datasets are sorted in size (small, medium, large) and type (unsorted, sorted, reverseSorted).

NOTE: Everytime you generate a new dataset, the old dataset is overwritten.

###### Then sort the files and measure their time efficiency:
	python3 ./customSorts.py

This will create and fill the results folder heirarchy with the results of the tests run against the dataset.

The results folder can be found at: General-Sort/results. The results are sorted in dataset input size (small, medium, large) and dataset input type (unsorted, sorted, reverseSorted).

All of the run time data for each test as well as the overall run time mean and standard deviation is stored at the end of any given results file.

NOTE: Everytime you generate a new dataset and run customSorts, the old results are overwritten.

