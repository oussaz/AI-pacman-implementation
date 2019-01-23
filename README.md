# AI-pacman-implementation
This repository contains all my implementations of AI algorithms in Pacman game.

## Tracking :
In this part, Pacman is chasing invisible ghosts using Bayesian inference with data provided by its sensors.
### Exact inference :
First we assume that ghosts' positions are stationary, and Pacman updates its beliefs of the ghosts distribution using only sensors' data.

Pacman updates updates its beliefs distribution using the following equation :
![ExactInfereq](/img/tracking/exactinferenceupdate.gif)


The results are given in the following captions :

| ![Firstiter](/img/tracking/1.png) | ![Lateriter](/img/tracking/2.png) |
|:---:|:---:|:---:|
| First iterations : The lighter the color, the higher the probability | Later iterations : The lighter the color, the higher the probability |

Because the error in the sensors data has a mean of zero, the probability of the right location converges to one.
In addition, given that the sensors provide only information about the distance to the ghost, Pacman cannot decide which position the ghost is located in if the distance is the same.






## Reinforcement Learning:
