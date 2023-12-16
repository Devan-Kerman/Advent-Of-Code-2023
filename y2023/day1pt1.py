
calibrations = []
with open("../data/day1.txt", "r") as f:
	calibrations += f.readlines()

sum = 0
for calibration in calibrations:
	first = None
	last = 0
	for c in calibration:
		if c.isdigit():
			if not first:
				first = c
			last = c
	sum += int(first + last)

print("Sum=", sum)