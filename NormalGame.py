import matplotlib.pyplot as plt
import numpy as np
import random


class NormalFormGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.strat1 = player1.strategy
        self.start2 = player2.strategy

        self.payoff_matrix = np.array([[[0, 0], [0, 0]], 
                                       [[0, 0], [0, 0]]])
        self.environment_const = np.random.randint(1, 10)

    def game_parameters(self):
        print("Player 1 Size:", self.player1.size)
        print("Player 1 Speed:", self.player1.speed)
        print("Player 2 Size:", self.player2.size)
        print("Player 2 Speed:", self.player2.speed)
        print("Environment Constant:", self.environment_const)

    # Players can either choose to Attack or Defend
    '''
    If Both players choose to attack : 
    Player with the larger size wins and other player suffers damage proportional to the difference in Kinetic Energy of the two players
    The winning player also suffers some recoil damage proportional to the difference in the Kinetic Energies of the two players

    If Both players choose to defend :
    Both players suffer some damage proportional to Momentum of the two players and an Environment Dependent Proportionality Constant
    So larger the momentum of the player, more the damage suffered

    If one player chooses to attack and the other chooses to defend :
    If the speed of the attacking player is greater than the speed of the defending player, the attacking player wins and the defending player suffers damage proportional to the difference in Kinetic Energy of the two players
    The winning player also suffers some recoil damage proportional to the difference in the Kinetic Energies of the two players

    If the speed of the attacking player is less than the speed of the defending player, the defending player wins and the attacking player suffers damage proportional to the difference in Kinetic Energy of the two players
    The winning player also suffers some recoil damage proportional to the difference in the Kinetic Energies of the two players
    The losing player also suffers some damage proportional to the difference in Kinetic Energy of the two players
    '''

    def generate_payoff_matrix(self):
        ke_p1 = self.player1.size * self.player1.speed ** 2
        ke_p2 = self.player2.size * self.player2.speed ** 2
        mom_p1 = self.player1.size * self.player1.speed
        mom_p2 = self.player2.size * self.player2.speed

        # Attack, Attack
        if ke_p1 > ke_p2:
            self.payoff_matrix[0, 0, 0] = - 0.25 * (ke_p1 - ke_p2) / 100
            self.payoff_matrix[0, 0, 1] = - 0.75 * (ke_p1 - ke_p2) / 100
        elif ke_p1 < ke_p2:
            self.payoff_matrix[0, 0, 0] = - 0.75 * (ke_p2 - ke_p1) / 100
            self.payoff_matrix[0, 0, 1] = - 0.25 * (ke_p2 - ke_p1) / 100
        else:
            self.payoff_matrix[0, 0, 0] = - self.environment_const
            self.payoff_matrix[0, 0, 1] = - self.environment_const

        # Defend, Defend
        self.payoff_matrix[1, 1, 0] = - 0.5 * mom_p1 * self.environment_const
        self.payoff_matrix[1, 1, 1] = - 0.5 * mom_p2 * self.environment_const

        # Attack, Defend
        if self.player1.speed > self.player2.speed:
            self.payoff_matrix[0, 1, 0] = - 0.1 * abs(ke_p1 - ke_p2) / 1000
            self.payoff_matrix[0, 1, 1] = - 0.9 * abs(ke_p1 - ke_p2) / 1000
        elif self.player1.speed < self.player2.speed:
            self.payoff_matrix[0, 1, 0] = - 0.9 * abs(ke_p2 - ke_p1) / 1000
            self.payoff_matrix[0, 1, 1] = - 0.1 * abs(ke_p2 - ke_p1) / 1000
        else:
            self.payoff_matrix[0, 1, 0] = - self.environment_const * 0.4
            self.payoff_matrix[0, 1, 1] = - self.environment_const * 0.6

        # Defend, Attack
        if self.player1.speed > self.player2.speed:
            self.payoff_matrix[1, 0, 0] = - 0.9 * abs(ke_p1 - ke_p2) / 1000
            self.payoff_matrix[1, 0, 1] = - 0.1 * abs(ke_p1 - ke_p2) / 1000
        elif self.player1.speed < self.player2.speed:
            self.payoff_matrix[1, 0, 0] = - 0.1 * abs(ke_p2 - ke_p1) / 1000
            self.payoff_matrix[1, 0, 1] = - 0.9 * abs(ke_p2 - ke_p1) / 1000
        else:
            self.payoff_matrix[1, 0, 0] = - self.environment_const * 0.6
            self.payoff_matrix[1, 0, 1] = - self.environment_const * 0.4


    def play_round(self):
        index1 = random.choices(range(len(self.player1.strategy)), self.player1.strategy)[0]
        index2 = random.choices(range(len(self.player2.strategy)), self.player2.strategy)[0]

        payoff1, payoff2 = self.payoff_matrix[index1, index2]
        return np.array([payoff1, payoff2])
    

    def play_match(self):
        p1_score = [self.player1.health]
        p2_score = [self.player2.health]
        round_count = [0]

        while self.player1.health > 0 and self.player2.health > 0:
            payoffs = self.play_round()
            self.player1.health += payoffs[0]
            self.player2.health += payoffs[1]
            p1_score.append(self.player1.health)
            p2_score.append(self.player2.health)
            round_count.append(round_count[-1] + 1)

        plt.plot(round_count, p1_score, label="Player 1")
        plt.plot(round_count, p2_score, label="Player 2")
        plt.xlabel("Round")
        plt.ylabel("Health")
        plt.title("Health of Players over time")
        plt.legend()
        plt.show()

        if self.player1.health > 0 and self.player2.health <= 0:
            print("Player 1 wins")
        elif self.player1.health <= 0 and self.player2.health > 0:
            print("Player 2 wins")
        else:
            print("Draw")
