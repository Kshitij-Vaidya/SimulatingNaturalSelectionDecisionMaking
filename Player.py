import matplotlib.pyplot as plt
import numpy as np
import random

class Player:
    def __init__(self, strategy = [0.5, 0.5],
                health = 1000):
        self.size = random.randint(1, 20)
        self.speed = random.randint(1, 100)
        self.strategy = strategy
        self.health = health
        self.history = []
        self.score = 0

    def print_player(self):
        print("Size:", self.size)
        print("Speed:", self.speed)
        print("Health:", self.health)
        print("Strategy:", self.strategy)
        print("Score:", self.score)


