rows = []
with open("../data/day3.txt", "r") as f:
	rows += [line[:-1] for line in f.readlines()]

# 539821
# 539821
# 567141
def findSum(knownParts):
	sum = 0
	for i, row in enumerate(rows):
		for j, c in enumerate(row):
			if c.isdigit() and not row[max(j - 1, 0)].isdigit():
				idx = j
				for k in range(len(row) - j):
					if row[idx].isdigit():
						idx += 1

				start = max(j - 1, 0)
				end = min(idx + 1, len(row))
				neighbors = [rows[k][start:end] for k in range(max(i - 1, 0), min(i + 2, len(rows)))]

				print(neighbors)
				real = False
				for n in "".join(neighbors):
					if not n.isdigit() and n != '.':
						real = True
						break

				value = int(row[j:idx])
				if real or value in knownParts:
					knownParts[value] = True
					sum += value
	return sum, knownParts

oldtotal, parts = findSum({})
total, _ = findSum(parts)
print(oldtotal, total)