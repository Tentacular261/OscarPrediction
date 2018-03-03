# Author: Joseph
# Purpose: Change director csv (with award data) to usable format
# for the R script to train a model for Oscar nominations

awards = {}

with open("director_award_data_formatted.csv", 'r') as input_file:
	lines = input_file.readlines()
	for line in lines[1:]:
		vals = line.strip().split(',')
		awards[vals[0]] = vals[1:]

with open("best_director_nominations.txt", 'r') as input_file:
	for line in input_file:
		line = line.strip()
		pline = line
		for val in awards[line]:
			pline += "," + val;
		print(pline)
