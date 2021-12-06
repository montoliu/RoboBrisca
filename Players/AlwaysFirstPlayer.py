# --------------------------------------------------------
# - RoboBrisca
# - AlwaysFirstPlayer
# - Implemented by: Raul Montoliu (Dic 2021)
# --------------------------------------------------------
from Players.Player import Player


# ---------------------------------------------------------------------------
# Returns always the first action from the list of possible actions
# ---------------------------------------------------------------------------
class AlwaysFirstPlayer(Player):
    def think(self, observation, budget):
        list_actions = observation.get_list_actions()
        return list_actions[0]

    def __str__(self):
        return "AlwaysFirstPlayer"
