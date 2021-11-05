import random

class Agent():
    
    def __init__(self, i, agents, environment, rows, cols, y, x):
        # self.x = random.randint(0, 99)
        # self.y = random.randint(0, 99)
        self.x = x
        self.y = y
        self.environment = environment
        self.agents = agents
        self.store = 0
        self.rows = rows
        self.cols = cols
        self.i = i
    
    def __str__(self):
        return "id=" + str(self.i) \
            + ", x=" + str(self.x) \
            + ", y=" + str(self.y) \
            + ", store=" + str(self.store)
        
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % self.rows
        else:
            self.y = (self.y - 1) % self.rows
        if random.random() < 0.5:
            self.x = (self.x + 1) % self.cols
        else:
            self.x = (self.x - 1) % self.cols
            
    def eat(self):
        # The commented out code was to check that this works.
        ## Test by setting the environment value
        #self.environment[self.y][self.x] = 8
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            #print("Adding a value less than 10")
            #print("Before self.environment[self.y][self.x]", self.environment[self.y][self.x])
            #print(self)
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
            #print("After self.environment[self.y][self.x]", self.environment[self.y][self.x])
            #print(self)
        if self.store >= 100:
            #print("Sick")
            self.environment[self.y][self.x] += 100
            self.store = 0
            
    def distance_between(self, b):
        return (((self.x - b.x)**2) + ((self.y - b.y)**2))**0.5
            
    def share_with_neighbours(self, neighbourhood):
        #print("neighbourhood", neighbourhood)
        # Loop through the agents in self.agents.
        #for agent in self.agents:        
        for i in range(len(self.agents)):
            # Calculate the distance between self and the current other agent:
            distance = self.distance_between(self.agents[i])
            # If distance is less than or equal to the neighbourhood
            if distance < neighbourhood:
                print("distance", distance)
                # Sum self.store and agent.store .
                total = self.store + self.agents[i].store
                # Divide sum by two to calculate average.
                average = total / 2
                # self.store = average
                self.store = average
                # agent.store = average
                self.agents[i].store = average
            # End if
        # End loop

    def getID(self):
        return self.i





   
            
            
            
            
            
            
            