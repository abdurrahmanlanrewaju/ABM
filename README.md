

## Introduction

This repository is a simple agent-based model (ABM). It is a model that involves agents wandering around and eating material (data) from the underlying landscape. The model builds up a series of agents in space where each agent has a list of other agents that it communicates with and where each agent knows about the environment it is in and is able to change or query the environment. The agents moves around to check whether other agents are not in the neighbourhood and when it confirms that, it moves around the environment to eat it. The environment contains data from a file which is displayed along with the environment after the model is run. Lastly, the environment saves as the result of the mdoel. 


## Core Components of the ABM
The model consists of the following core components:
1. The Environment
2. The Animals/Agents

# The Environment
The environment is a Euclidean 2D plane that is generated from reading the data in the CSV file [in.txt]. 
In assignment explores the agent-based model (ABM) in order to  designing and build an agent-based model. Taking  through the complete design process, we explore the considerations required in 
defining a simulation _overview_, in designing the simulation _world_, the nature of agent _interactions_ with each other and the world around them, and how the _agents_ communication with environments. 


##Core components
## Introduction
Model code, which deals with interacting with the user and sets up the model, including running the model iterations and checking the stopping conditions. 
Agent code, which is used to build agents that can include the agent's behaviour and any records of their state. The behaviours implemented here is mathematical, or statistical. 



move(): The function moves agents in x and y axis randomly

eat(): The function defines how agents consume given resources

distance_between(): The function calculates distance between x and y axis

share_with_neighbours(): The function defines interaction of agents in neighborhood 






##Model

write_line_to_output(s): The function writes output and reads input from text file


get_maximum(): The function checks environment for largest value




get_minimum(): The function checks environment for minimum value


run(), update() and gentfunction() are developed  for GUI of the system

<img src="Figure_1.png" alt="Segregation ABM" />

## Unittest


<img src="b1.png" alt="Segregation ABM" />







