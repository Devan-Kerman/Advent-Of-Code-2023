
calibrations = []
with open("../data/day1.txt", "r") as f:
	calibrations += f.readlines()

sum = 0
digits = [
	"zero",
	"one",
	"two",
	"three",
	"four",
	"five",
	"six",
	"seven",
	"eight",
	"nine",
]

for calibration in calibrations:
	first = None
	last = 0
	for i, c in enumerate(calibration):
		if c.isdigit():
			if not first:
				first = c
			last = c

		for j, d in enumerate(digits):
			if calibration[i:-1].startswith(d):
				if not first:
					first = str(j)
				last = str(j)


	sum += int(first + last)

print("Sum=", sum)