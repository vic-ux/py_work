numbers = [5,2,5,2,2]
for num in numbers:
	num *= "x"
	print(f"{num}")

numbers = [5,2,5,2,2]
for num in numbers:
	print (f"{'x' * num}")

"""nested loop"""



numbers = [1,1,1,5]
for num in numbers:
	output = ""
	for nu in range(num):
		output += 'x'
	print(output)
