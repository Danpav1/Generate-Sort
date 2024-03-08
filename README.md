# Progamming assignment 1:

###### Introduction

This project is part of the Design and Analysis of Algorithms course and focuses on
generating a comprehensive dataset to analyze the efficiency of various sorting algorithms. 
The primary objective is to create 180 text files populated with random integers within
the range [0 - 10,000), and then apply different sorting techniques to evaluate their
performance under various conditions.

###### Dataset Overview

- Small files: Each containing 10,000 integers.
- Medium files: Each containing 100,000 integers.
- Large files: Each containing 1,000,000 integers.

In total, each category consists of 90 files, split into three equal parts based on their
sorting order:

- Unsorted: Files in their original, unsorted state.
- Sorted (High to Low): Files sorted in descending order.
- Sorted (Low to High): Files sorted in ascending order.

###### Sorting Algorithms

The files generated will be sorted using the following custom algorithms to benchmark their
efficiency:

- Quicksort
- Mergesort
- Heapsort

###### Usage

First generate the files:
	python3 ./textFileGenerator.py

Then sort the files and measure their efficiency:
	python3 ./-


