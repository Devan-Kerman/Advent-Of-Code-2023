cards = []
with open("../data/day4.txt", "r") as f:
	cards += [line[:-1] for line in f.readlines()]

total_count = 0
card_counts = {}
for card in cards:
	start = card.find(":")
	mid = card.find("|")

	id = int(card[5:start])
	winning = [int(card[i:i+2]) for i in range(start+2, mid, 3)]
	numbers = [int(card[i:i+2]) for i in range(mid + 2, len(card), 3)]

	count = 0
	for number in numbers:
		if number in winning:
			count += 1

	curr = card_counts[id] if id in card_counts else 0
	card_counts[id] = curr + 1

	for i in range(count):
		idx = id+i+1
		extra = card_counts[idx] if idx in card_counts else 0
		card_counts[idx] = extra+curr+1
	print(f"Matches: {count}")
	print(card_counts)


print(sum(card_counts.values()))