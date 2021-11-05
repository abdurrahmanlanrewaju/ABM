import random
import operator
import tkinter
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import csv
import requests
import bs4


random.seed(0)

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
# print(td_ys)
# print(td_xs) 

def write_line_to_output(s):
    with open("output.txt", "a+") as f:
        f.write(s)
        f.write("\n")

# Read in the in.txt file into a list of lists called environment
environment = []
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowList = []
        for value in row:
            #print(value)
            rowList.append(value)
        environment.append(rowList)

# Check environment
rows = len(environment)
cols = len(environment[0])
print("rows", rows)
print("cols", cols)
# Check the number of rows in the data have the same number of columns
for row in range(rows):
    if (len(environment[row]) != cols):
        print("unhappy")
            
def get_maximum(environment):
    # Check environment for the largest value
    maximum = environment[0][0]
    # Check the number of rows in the data have the same number of columns
    for row in range(rows):
        for col in range(cols):
            maximum = max(maximum, environment[row][col])
    return maximum

def get_minimum(environment):
    # Check environment for the largest value
    m = environment[0][0]
    # Check the number of rows in the data have the same number of columns
    for row in range(rows):
        for col in range(cols):
            m = min(m, environment[row][col])
    return m
print("maximum", get_maximum(environment))
print("minimum", get_minimum(environment))

#print(environment)
#matplotlib.pyplot.imshow(environment) # Visually check by plotting
#matplotlib.pyplot.show()
            
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 3000
agents = []
neighbourhood = 20

# Make the agents.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(i, agents, environment, rows, cols, y, x))

# Print the agents
for i in range(num_of_agents):
    print(agents[i])


# for i in range(num_of_agents):
#     agents.append(agentframework.Agent(i, agents, environment, rows, cols))

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw() 

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

carry_on = True	
	
def update(frame_number):
    
    fig.clear()   
    global carry_on
    
    # Plot the environment first
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.xlim(0, cols)
    matplotlib.pyplot.ylim(0, rows)
    
    print("Iteration", frame_number)
    random.shuffle(agents)
    for i in range(num_of_agents):
        #print(agents[i])
        #print(i, "before move", agents[i].x, agents[i].y)
        agents[i].move()
        #print(i, "after move", agents[i].x, agents[i].y)
        #print("store before eat", agents[i].store)
        agents[i].eat()
        #print("store after eat", agents[i].store)
        agents[i].share_with_neighbours(neighbourhood)
        
    print("maximum", get_maximum(environment))
    print("minimum", get_minimum(environment))

    # if random.random() < 0.1:
    #     carry_on = False
    #     print("stopping condition")
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
        #print(agents[i][0],agents[i][1])

		
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
# animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)



# matplotlib.pyplot.show()

def getID():
    return agents.i
    
# Print agents
print("Final agents")
# https://docs.python.org/3/howto/sorting.html
sorted_agents = sorted(agents, key=lambda a: a.i)
for i in range(num_of_agents):
    print(sorted_agents[i])

tkinter.mainloop()

