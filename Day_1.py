##		Richard Roberts, 2022 Advent of Code.	Completed 9/13/2023

file = open("adventpuzzle.txt")		##	File containing Calories from each of the Elves

elfRoster = []		##	List of the total Calories per Elf in the roster

currElf, topCalorie= 0, [0, 0, 0]		##	Storage for current Elf's Calorie count, and the Top 3 descending Calorie sums

for line in file:		##	Iterates through each line in file
	if line.strip():		##	If the line is not empty:
		currElf+=int(line)		##	Add its value to the current Elf's Calorie count
	else:					##	Else, add complete Calorie count to top 3 placement if applicable
		if currElf > topCalorie[0]:		##	If greater than previous greatest, lower the other 2 rankings
			topCalorie[2] = topCalorie[1]
			topCalorie[1] = topCalorie[0]
			topCalorie[0] = currElf
		elif currElf > topCalorie[1] and currElf < topCalorie[0]:	##	If only greater than middle, lower the current middle
			topCalorie[2] = topCalorie[1]
			topCalorie[1] = currElf
		if currElf > topCalorie[2] and currElf < topCalorie[1]:		##	If only greater than third, replace third
			topCalorie[2] = currElf
		elfRoster.append(currElf)		##	Append Calorie count to the Elf roster
		currElf = 0						##	Reset our Calorie count
else:					##	Handling the last Elf that doesn't trigger the above condition
	if currElf > topCalorie[0]:
		topCalorie[2] = topCalorie[1]
		topCalorie[1] = topCalorie[0]
		topCalorie[0] = currElf
	elif currElf > topCalorie[1] and currElf < topCalorie[0]:
		topCalorie[2] = topCalorie[1]
		topCalorie[1] = currElf
	if currElf > topCalorie[2] and currElf < topCalorie[1]:
		topCalorie[2] = currElf
	elfRoster.append(currElf)
print(elfRoster)		##	Displays all Elves present in given sample
print(topCalorie)		##	Displays the top 3 highest calories
print(topCalorie[0] + topCalorie[1] + topCalorie[2])	##	Sum of the 3 highest calories