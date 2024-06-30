# SimulatingNaturalSelectionDecisionMaking

This repository contains a Python simulation that explores the intersection of natural selection and decision making through the lens of game theory. The simulation models how individuals within a population make decisions that affect their survival and reproductive success, illustrating the principles of natural selection and evolutionary game theory.

## Introduction

Natural selection is the process by which traits become more or less common in a population due to consistent effects upon the survival or reproduction of their bearers. Decision making, especially in the context of evolutionary biology, often involves strategies that individuals employ to maximize their fitness in response to environmental challenges and opportunities.

Game theory, a mathematical framework developed to understand strategies in competitive situations, provides a powerful tool for modeling decision making in natural selection. It helps in understanding how cooperation, competition, and strategy evolution play out in the natural world.

## Game Theory

Game theory is the study of mathematical models of strategic interaction among rational decision-makers. It has applications in all fields of social science, as well as in logic, systems science, and computer science. In the context of natural selection, game theory models can illustrate how different strategies adopted by individuals affect their survival and reproduction, leading to evolutionarily stable strategies (ESS).

### Key Concepts

- **Nash Equilibrium**: A situation in which each player is choosing the best strategy given the strategies that all the other players have chosen.
- **Evolutionarily Stable Strategy (ESS)**: A strategy that, if adopted by a population, cannot be invaded by any alternative strategy that is initially rare.
- **Payoff Matrix**: A mathematical representation of the outcomes of different strategies played by individuals in a game.

## Natural Selection

Natural selection acts on the phenotype, the characteristics of an organism which actually interact with the environment. Through the lens of game theory, we can simulate environments where different phenotypic strategies compete, leading to the survival and proliferation of the most fit strategies.

### Simulation Overview

The simulation models a population of individuals who make decisions based on game theory principles. Each individual has a set of strategies for dealing with specific environmental scenarios. The success of these strategies affects their survival and reproductive success, simulating natural selection.

## Content Details

To run the simulation, you will need Python installed on your computer. Clone this repository, navigate to the project directory, and install the required dependencies:

```bash
git clone https://github.com/Kshitij-Vaidya/SimulatingNaturalSelectionDecisionMaking.git
cd SimulatingNaturalSelectionDecisionMaking
```

### Simulating Normal Form Games

The following files contain the classes defined to simulate the Players (Creatures) and the Game (Environment): 

`Player.py`

`NormalGame.py`

The `TestNormalGame.py` file contains a simple simulation code to run a Normal Form Game between two players whose attributes are randomly generated. The functions defined within the `NormalFormGame` class allow to define the Payoff Matrix between two players whose attributes namely speed, size and strategy are randomly generated. 

We can simulate a single round or a match till a winner is decided. This game simulation is the first step towards simulating more complicated natural environments with multiple players and strategies and also add attributes to the existing `Player` class to allow for more complex player interactions.



## Contributing
Contributions to this project are welcome! Please fork the repository, make your changes, and submit a pull request.