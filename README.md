# UC-Berkeley-AI-P2

## Project Overview

The Pacman AI project is a series of programming assignments designed to introduce students to artificial intelligence concepts in the context of controlling the Pacman character in a maze environment. The assignments progressively cover various AI techniques, algorithms, and strategies, allowing students to explore and implement different AI agents to control Pacman's behavior.

### Core Concepts

1. **Game Environment**: The project's foundation is the game environment, represented by the `game.py` module. It defines the layout of the maze, the Pacman character, ghosts, food dots, capsules, and other game elements.

2. **Agent Strategies**: The main objective is to implement AI agents that make decisions to control Pacman's movements. Different strategies are employed to achieve specific goals, such as collecting all food dots, avoiding ghosts, and optimizing the score.

## Algorithms and Agents

1. **Reflex Agent**: The reflex agent is a simple agent that uses a state evaluation function to choose actions. The `ReflexAgent` class in `multiAgents.py` demonstrates this approach. The agent evaluates the state and chooses the action that leads to the best outcome based on the evaluation.

2. **Minimax Agent**: The `MinimaxAgent` class in `multiAgents.py` implements the minimax algorithm. In adversarial scenarios, like playing against ghosts, this agent explores the game tree to make optimal decisions while considering the opponents' moves. It aims to minimize its potential loss and maximize its gain.

3. **Alpha-Beta Pruning**: The `AlphaBetaAgent` class in `multiAgents.py` builds upon the minimax algorithm by incorporating alpha-beta pruning. This technique prunes branches of the game tree that are guaranteed not to affect the final decision, significantly reducing the number of explored nodes.

4. **Expectimax Agent**: The `ExpectimaxAgent` class in `multiAgents.py` represents the expectimax algorithm. Unlike the minimax algorithm that considers worst-case scenarios, expectimax accounts for the probabilistic nature of the game when opponents' moves are uncertain. It computes the expected value of outcomes.

## Project Structure

The project code is organized into different modules to facilitate understanding and implementation. The main modules include:

- **`util.py`**: Contains utility functions for data structures and algorithms.
- **`game.py`**: Defines the game environment, actions, and state representations.
- **`multiAgents.py`**: Contains implementations of various AI agents, including reflex agents, minimax agents, alpha-beta agents, and expectimax agents.
- **`search.py`**: Defines search algorithms used by the AI agents.

## Project Learning Objectives

Through this project, students learn:

- How to model a problem in terms of states, actions, transitions, and goals within a game environment.
- The basics of uninformed search algorithms such as depth-first search, breadth-first search, and uniform cost search.
- The application of informed search algorithms like A* search and heuristics.
- How to implement and compare different adversarial search algorithms for decision-making in the presence of opponents.

## Conclusion

The Pacman AI project is an engaging way to learn and practice AI concepts in a fun and interactive manner. By implementing various AI agents to control Pacman's behavior, students gain practical experience with fundamental algorithms used in artificial intelligence and enhance their problem-solving skills in different game scenarios.
