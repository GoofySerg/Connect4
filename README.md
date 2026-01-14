# Connect 4 with AI Opponents

## Overview

This project is a fully playable **Connect 4** game featuring **three distinct AI opponents** of increasing difficulty. It was developed to demonstrate core concepts in **game AI**, **search algorithms**, and **decision optimisation**, with a particular focus on **Minimax** and **Alpha–Beta pruning**.

The project is intended both as a functional game and as a technical showcase for employers interested in algorithmic thinking, AI fundamentals, and clean software design.

---

## Features

* **Classic Connect 4 gameplay** (7×6 grid, standard rules)
* **Three AI opponents** with different skill levels
* **Minimax algorithm** for optimal move selection
* **Alpha–Beta pruning** for significant performance optimisation
* Clear separation between **game logic**, **AI logic**, and **UI / input handling**

---

## Algorithms Used

### Minimax

The Minimax algorithm is used to evaluate possible future game states by assuming:

* The **AI plays optimally** to maximise its chances of winning
* The **human player plays optimally** to minimise the AI’s score

Each possible move is explored recursively until a terminal state or maximum depth is reached.

### Alpha–Beta Pruning

To improve efficiency, **Alpha–Beta pruning** is applied to the Minimax search:

* Branches that cannot influence the final decision are discarded
* This dramatically reduces the number of evaluated nodes
* Allows deeper searches without exponential performance costs

This optimisation is essential for the Hard AI opponent.

---

## Evaluation Function

Non-terminal board states are scored using a heuristic evaluation function that considers:

* Potential four-in-a-row sequences
* Control of the centre columns
* Offensive and defensive threats

The heuristic design balances **aggressive play** with **blocking opponent wins**, resulting in realistic AI behaviour.

---

## Technical Skills Demonstrated

* Game state representation and management
* Recursive search algorithms
* Algorithmic optimisation techniques
* Clean modular code structure
* Problem decomposition and abstraction


## Future Improvements

* Graphical user interface
* Adjustable search depth at runtime
* Time-limited AI decision making
* Multiplayer (human vs human)
* Machine-learning-based evaluation function

---

## Motivation

This project was built to deepen my understanding of **artificial intelligence in games** and to apply theoretical algorithms in a practical, interactive setting. It reflects a strong interest in computer science, optimisation, and intelligent systems.

