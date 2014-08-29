import random

def play(color, money, bid, max_rounds, turn_based):
	current_round = 0
	inital_bid = bid
	high = money
	best_round = 0
	while money > 0 and current_round <= max_rounds:
		if (turn_based):
			raw_input("new round")

		r = spin()
		money = money - bid

		if (r == color):
			# won the spin
			winnings = bid * 2
			print "You won! Won {0}".format(winnings)
			# reset bid to inital bid
			bid = inital_bid
			money += winnings
			if money > high:
				high = money
				best_round = current_round
		else:
			# lost, double down on bid
			bid = bid * 2
			print "You lost, upping bid to {0}".format(bid)

		current_round += 1
		print "Round: {round} Current money: {money}".format(round = current_round, money = money)

	print "{status}: High: {high} at round {best_round}".format(status= money, high=high, best_round=best_round)

	return money


# 1 -> red
# 2 -> black
# 3 -> green
# 0 - 18 => 1, 19 - 36 => 2, 37 => 3
def main():
	num_games = 1000
	max_high = 0
	won_games = 0
	lost_games = 0

	for i in range(num_games):
		winnings = play(color = 1, money = 10, bid = 1, max_rounds = 1000, turn_based = True)
		if winnings > 0:
			won_games += 1
		else:
			lost_games += 1

		if (winnings > max_high):
			max_high = winnings

	print "MOST WINNINGS: {0}".format(max_high)
	print "WON {0} LOST {1}".format(won_games, lost_games)

def spin():
	random.seed()
	result = random.randint(0,37)
	if result in range(0, 19):
		return 1
	if result in range(19, 37):
		return 2
	if result == 37:
		return 3


main()