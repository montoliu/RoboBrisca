from Players.Player import Player


class HumanPlayer(Player):
    def think(self, observation, budget):
        list_actions = observation.get_list_actions()
        print("Actions that can be done: ")
        i = 0
        for action in list_actions:
            print(str(i) + " -> " + str(action))
            i += 1

        print("Select the action: ")
        action_ith = int(input())
        return list_actions[action_ith]

    def __str__(self):
        return "HumanPlayer"
