# 2nd position on first edition
import math
import time
import random

from Game.Common import is_better_card
from Game.Action import Action
from Game.ForwardModel import ForwardModel
from Game.Heuristic import Heuristic
from Players.Player import Player


class IAsauriosPlayer(Player):
    def __init__(self):
        self.forward_model = ForwardModel()
        self.heuristic = MyHeuristic()  # Mon was here!!//

    def __str__(self):
        return "IAsaurios"

    def get_points(self, observation):
        points = 0
        for i in range(observation.playing_cards.len()):
            points += observation.playing_cards.get_card(i).get_value()
        return points

    def think(self, observation, budget):

        initial_time = time.time()
        time_difference = budget * 0.9  # para tener tiempo de margen

        # Lista de acciones del turno
        list_actions = observation.get_list_actions()
        if len(list_actions) == 1:
            return list_actions[0]

        values = [0, 0, 0]

        player_id = observation.turn
        played_cards = observation.playing_cards.len()
        # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        if played_cards == 0 or played_cards == 2:
            factor = -1
        else:
            factor = 1
        # AAAAAAAAAAAAAAAAAAAAAAAAAAAA

        # # Antes de entrar al bucle, mirar en qué posición estoy
        #
        #
        # # Somos los ultimos -> jugar como humanos
        # if (played_cards == 3):
        #     first_card = observation.playing_cards.get_card(0)
        #     trump = observation.trump_card
        #     playing_cards = observation.playing_cards
        #
        #     best_played_card_id = 0
        #     for x in range(1, 3):
        #         if (is_better_card(playing_cards.get_card(x), playing_cards.get_card(best_played_card_id), trump,
        #                            first_card)):
        #             best_played_card_id = x
        #
        #     best_card_index = -1
        #     # Compañero va ganando
        #     if best_played_card_id == 1:
        #
        #         #mirar la más alta que no es triunfo
        #         for action_index in range(len(list_actions)):
        #             action_card = list_actions[action_index].get_card()
        #
        #             #mirar si no es triunfo
        #             if action_card.get_type() != trump.get_type():
        #                 #es la primera carta NO triunfo
        #                 if best_card_index == -1:
        #                     best_card_index = action_index
        #                 #toca comparar cartas
        #                 else:
        #                     if action_card.get_value() > list_actions[best_card_index].get_card().get_value():
        #                         best_card_index = action_index
        #
        #         #si todas son triunfos, coger la más baja
        #         if best_card_index == -1:
        #             best_card_index = 0
        #             for action_index in range(len(list_actions)):
        #
        #                 if list_actions[action_index].get_card().get_value() < list_actions[best_card_index].get_card().get_value():
        #                     best_card_index = action_index
        #
        #     #somos los últimos pero equipo va perdiendo
        #     else:
        #         n_triunfos = 0
        #         for action_index in range(len(list_actions)):
        #             action_card = list_actions[action_index].get_card()
        #             # mirar si no es triunfo
        #             if action_card.get_type() != trump.get_type():
        #                 # es la primera carta NO triunfo
        #                 if best_card_index == -1:
        #                     best_card_index = action_index
        #                 # toca comparar cartas
        #                 else:
        #                     if action_card.get_value() > list_actions[best_card_index].get_card().get_value():
        #                         best_card_index = action_index
        #             else:
        #                 n_triunfos += 1
        #         # 1º Intentar ganar sin triunfos -> con la mejor carta
        #         # Se compara tu mejor carta no triunfo con las de los oponentes, si no ganas --> 2º PASO
        #         if not is_better_card(list_actions[best_card_index].get_card(), playing_cards.get_card(0), trump,
        #                               first_card) \
        #                 and not is_better_card(list_actions[best_card_index].get_card(), playing_cards.get_card(2), trump,
        #                                        first_card):
        #             best_card_index = -1
        #
        #         #2º Intentar ganar con triunfos
        #         if best_card_index == -1:  # comprobar si entramos a este punto
        #             #2.a Mirar si tenemos triunfos
        #             if n_triunfos != 0:
        #                 # 2.a.1 Si hay 0 puntos -> llamar a worst_card_in_hand_index()
        #                 if self.get_points(observation) ==  0:
        #                     best_card_index = self.worst_card_in_hand_index(list_actions, trump)
        #
        #                 #2.a.2 Hay más de 0 puntos -> peor carta con triunfos
        #                 else:
        #                     best_card_index = 0
        #                     for index in range(len(list_actions)):
        #                         if list_actions[index].get_card().get_type() == trump.get_type() \
        #                             and list_actions[index].get_card().get_value() < list_actions[best_card_index].get_card().get_value():
        #                             best_card_index = index
        #
        #             #2.b No tenemos triunfos -> llamar a worst_card_in_hand_index()
        #             else:
        #                 best_card_index = self.worst_card_in_hand_index(list_actions, trump)
        #
        #         #3º No puedo ganar --> la peor carta
        #         if best_card_index == -1:   #aun no tenemos carta elegida
        #             best_card_index = self.worst_card_in_hand_index(list_actions, trump)
        #
        #     return list_actions[best_card_index]

        #no somos los ultimos -> IA
        #else:
            # poner un while para evitar el fallo de tiempo
        while time.time() - initial_time < time_difference:
            j = 0
            new_obs_rand = observation.get_randomized_clone()
            for action in list_actions:
                new_obs = new_obs_rand.clone()
                # Yo juego mi carta
                value = self.forward_model.play(new_obs, action, self.heuristic)
                played_cards = played_cards + 1
                other = player_id + 1

                # while iteraciones
                # Recoger cartas, barajar y volver a repartir
                while played_cards < 4:
                    if other == 4:
                        other = 0
                    # Seleccionar una carta al azar
                    ith = random.choice(range(new_obs.hands[other].len()))
                    c = new_obs.hands[other].get_card(ith)
                    # Otro jugador juega una carta
                    value = self.forward_model.play(new_obs, Action(c), self.heuristic)
                    played_cards += 1
                    other += 1

                # Guarda el valor de nuestras cartas

                values[j] += value * factor

                j += 1

        # buscar el maximo en values una vez que hemos salido de los bucles
        # print(values)
        max = -math.inf
        index = -1
        for i in range(len(list_actions)):
            if values[i] > max:
                max = values[i]
                index = i
        # print(len(list_actions))
        # print(index)
        return list_actions[index]

    #funcion que devuelve el indice de la peor carta que tenemos en la mano
    def worst_card_in_hand_index(self, list_actions, trump):
        worst_card_index = -1
        min = math.inf

        #mirar las cartas que no son triunfos
        for i in range(len(list_actions)):
            actual_card = list_actions[i].get_card()
            if actual_card.get_type() != trump.get_type():
                if actual_card.get_value() < min:
                    min = actual_card.get_value()
                    worst_card_index = i

        #todas son triunfos
        if worst_card_index == -1:
            for i in range(len(list_actions)):
                actual_card = list_actions[i].get_card()
                if actual_card.get_value() < min:
                    min = actual_card.get_value()
                    worst_card_index = i

        return worst_card_index

class MyHeuristic:
    def get_score(self, observation, player_id):
        if observation.playing_cards.len() == 0:
            return 0

        # points of played cards
        cards = observation.playing_cards.get_cards()
        points = 0
        for card in cards:
            points += card.get_value()

        player_card = observation.playing_cards.get_last_card()
        first_card = observation.playing_cards.get_card(0)
        if observation.playing_cards.len() == 1:
            score = points
        elif observation.playing_cards.len() == 2:
            other_player_card = observation.playing_cards.get_card(0)
            if is_better_card(other_player_card, player_card, observation.trump_card, first_card):
                score = -points
            else:
                score = points
        elif observation.playing_cards.len() == 3:
            other_player_card = observation.playing_cards.get_card(1)
            my_mate_card = observation.playing_cards.get_card(0)
            if is_better_card(other_player_card, player_card, observation.trump_card, first_card) and \
                    is_better_card(other_player_card, my_mate_card, observation.trump_card, first_card):
                score = -points
            else:
                score = points
        else:
            other_player_card1 = observation.playing_cards.get_card(0)
            other_player_card2 = observation.playing_cards.get_card(2)
            my_mate_card = observation.playing_cards.get_card(1)
            if (is_better_card(other_player_card1, player_card, observation.trump_card, first_card) and
                    is_better_card(other_player_card1, my_mate_card, observation.trump_card, first_card)) or \
                (is_better_card(other_player_card2, player_card, observation.trump_card, first_card) and
                    is_better_card(other_player_card2, my_mate_card, observation.trump_card, first_card)):
                score = -points
            else:
                score = points

        return score
