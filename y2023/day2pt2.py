
games = []
with open("../data/day2.txt", "r") as f:
	games += f.readlines()



sum = 0
for game in games:
	limits = {
		"red": 0,
		"green": 0,
		"blue": 0
	}

	index = game.find(":")
	rounds = [r for r in game[index+1:-1].split(";")]
	for round in rounds:
		instance = [r[1:].split(" ") for r in round.split(",")]
		for num, color in instance:
			limits[color] = max(int(num), limits[color])

	game_id = game[5:index]
	sum += limits["red"] * limits["green"] * limits["blue"]

print(sum)