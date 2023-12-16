
games = []
with open("../data/day2.txt", "r") as f:
	games += f.readlines()

limits = {
	"red": 12,
	"green": 13,
	"blue": 14
}

sum = 0
for game in games:
	index = game.find(":")

	rounds = [r for r in game[index+1:-1].split(";")]
	invalid = False
	for round in rounds:
		instance = [r[1:].split(" ") for r in round.split(",")]
		for num, color in instance:
			if int(num) > limits[color]:
				invalid = True

	game_id = game[5:index]
	if not invalid:
		sum += int(game_id)

print(sum)