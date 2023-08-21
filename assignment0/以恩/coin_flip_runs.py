"""
File: coin_flip_runs.py
Name: Ian
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	Step1: input the number of runs
	Step2: build a counter of draw and sequential times
	Step3: build a loop of drawing depending on the sequential times
	Step4: print the result
	"""
	# Step1
	number = int(input("Let's flip a coin!\nNumber of runs: "))
	# Step2
	i = 0
	result = ''
	k = 0
	# Step3
	while k < number:
		roll = r.randint(1, 2)
		i += 1
		if roll == 1:
			result += 'H'
		else:
			result += 'T'
		if i >= 3:
			k = 0
			for j in range(i-2):
				if result[j] == result[j+1] and result[j] != result[j+2]:
					k += 1
	# Step 4
	print(result)



# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
