# 3rd position on first edition

from Players.Player import Player
from Game.Common import is_better_card
from Game.CardCollection import CardCollection

from math import factorial
from statistics import mean


class As_de_espadas(Player):

	def think(self, observation, budget):
		list_actions = observation.get_list_actions()

		for i in range(len(list_actions)):
			new_obs = observation.clone()
			action = list_actions[i]

			#value = self.forward_model.play(new_obs, action, self.heuristic)
			value = self.compute_almost_rational_solution(new_obs, action)

			if i == 0:
				best_action = action
				best_value = value
			elif value > best_value:
				best_action = action
				best_value = value

		return best_action

	def __str__(self):
		return "as_de_espadas"



	def compute_almost_rational_solution(self, new_obs, action):

		playing_cards = new_obs.playing_cards
		card = action.get_card()
		card_points = card.get_value()
		unknown_cards_avereage_value = self.cards_mean_value(self.get_unknown_cards(new_obs))



		if playing_cards.len() == 0:																										#roud = mine
			probability_of_enemies_not_having_better_card = self.hypergeometric_distr(self.better_cards_than_mine(card, self.get_unknown_cards(new_obs), new_obs.trump_card, card), 0, self.get_unknown_cards(new_obs).len(), 2*new_obs.hands[0].len())
																												#roud = mine
			return card_points * probability_of_enemies_not_having_better_card
			+ unknown_cards_avereage_value # The average is the card that my mate might play
				# TODO . prob_of_winning_in_on_future



		elif playing_cards.len() == 1:

			first_card = new_obs.playing_cards.get_card(0)
			other_player_card = new_obs.playing_cards.get_card(0)
			if is_better_card(other_player_card, card, new_obs.trump_card, first_card):
				return -card_points -sum([c.get_value() for c in playing_cards.get_cards()])
			else:
				return card_points + sum([c.get_value() for c in playing_cards.get_cards()])

		elif playing_cards.len() == 2:
			first_card = new_obs.playing_cards.get_card(0)
			other_player_card = new_obs.playing_cards.get_card(1)
			if is_better_card(other_player_card, card, new_obs.trump_card, first_card) and is_better_card(other_player_card, card, new_obs.trump_card, first_card):
				return -card_points -sum([c.get_value() for c in playing_cards.get_cards()])
			else:
				return card_points + sum([c.get_value() for c in playing_cards.get_cards()])

		else:

			first_card = new_obs.playing_cards.get_card(0)
			other_player_card1 = new_obs.playing_cards.get_card(0)
			other_player_card2 = new_obs.playing_cards.get_card(2)
			my_mate_card = new_obs.playing_cards.get_card(1)
			if (is_better_card(other_player_card1, card, new_obs.trump_card, first_card) and
					is_better_card(other_player_card1, my_mate_card, new_obs.trump_card, first_card)) or \
				(is_better_card(other_player_card2, card, new_obs.trump_card, first_card) and
					is_better_card(other_player_card2, my_mate_card, new_obs.trump_card, first_card)):
				return -card_points -sum([c.get_value() for c in playing_cards.get_cards()])
            
			return card_points +sum([c.get_value() for c in playing_cards.get_cards()])

	def cards_mean_value(self, cards):
		if cards.len() == 0:
			return 0
		return mean([c.get_value() for c in cards.get_cards()])


	def better_cards_than_mine(self, card, deck, trump, round_first):
		n_better_on_deck = 0
		for hidden in deck.get_cards():
			if is_better_card(hidden, card, trump, round_first):
				n_better_on_deck += 1
		return n_better_on_deck

    # K apearances in the populationself.
    # k apearances in the sample
    # N population size
    # n sample size
	def hypergeometric_distr(self, K, k, N, n):
		return (self.comb(K, k) * self.comb(N-K, n-k))/(self.comb(N, n))

	def comb(self, n, r):
		if r > n:
			return 0
		return factorial(n) / (factorial(r) * factorial(n-r))


	# Main deck + other player hands todo: manage trump
	def get_unknown_cards(self, new_obs):
		self.unknown_cards = CardCollection()
		self.unknown_cards.add_cards(new_obs.main_deck.get_cards())

		for i in range(len(new_obs.hands)):
			if i != new_obs.turn:
				hand = new_obs.hands[i]
				self.unknown_cards.add_cards(hand.get_cards())

		return self.unknown_cards


    # Tourn: round of the game starting on 0
    # Position: You can start a round in the position 0 or in the pos 3
	def number_of_known_cards(tourn, position): # TODO revisar puede estar mal la definicion de arriba
		return (tourn+1)*4+position

	def get_score(self, observation, player_id):
		if observation.playing_cards.len() == 1:
			return observation.playing_cards.get_card(0).get_value()