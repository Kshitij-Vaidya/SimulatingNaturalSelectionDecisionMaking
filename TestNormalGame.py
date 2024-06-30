from Player import Player
from NormalGame import NormalFormGame

player1 = Player(health=1000)
player2 = Player(health=1000)

player1.print_player()
player2.print_player()

game = NormalFormGame(player1, player2)
game.generate_payoff_matrix()
game.game_parameters()
game.play_match()