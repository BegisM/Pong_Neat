# AI in Computer Games Project

This project implements an AI system using the NEAT (NeuroEvolution of Augmenting Topologies) algorithm to control agents within a game environment built using Pygame.

## NEAT Algorithm Explanation

NEAT (NeuroEvolution of Augmenting Topologies) is an evolutionary algorithm used to evolve artificial neural networks. It combines genetic algorithms with neural networks and has the ability to evolve both the topology and the weights of the network. NEAT works by evolving populations of neural networks over generations, where each network competes to perform a specific task, such as controlling an agent in a game. Over time, the best-performing networks are selected, mutated, and recombined, improving their abilities.

For more information on the NEAT algorithm, you can visit the official paper or any relevant resources about evolutionary algorithms and neuroevolution.

## Dependencies

This project requires the following libraries to run:

- **Pygame**: A set of Python modules designed for writing video games.
- **NEAT-Python**: A Python implementation of the NEAT algorithm for evolving neural networks.

### Installing Dependencies

To get started with the project, first install the required dependencies:

1. **Install Pygame**:
   ```bash
   pip install pygame
2. **Install NEAT-Python**:
   ```bash
   pip install neat-python
After installing the dependencies, you can run the game and observe how the AI, powered by NEAT, learns to perform tasks in the game environment.

How to Run?
To run the project, simply execute the Python script that contains the Pygame game logic. 

**Like here**:
   ```bash
   python game.py