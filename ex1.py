import turtle as t
import random

#---------------------------------------#
#             SCREEN SETUP              #
#---------------------------------------#

width = 10
height = 5
t.setup(width*100+20,height*100+20)
screen = t.Screen()
screen.title("Captain Planet")
screen.screensize(width*100,height*100)

right = 100*(width/2-1)
top = 100*height/2

screen.bgpic("bgpic.gif")

#GLOBAL TURN
turn = 0

#---------------------------------------#
#       POLLUTION'S ENDLESS MARCH       #
#---------------------------------------#

t.register_shape("square", ((0,0),(0,50), (50,50), (50,0)))
waste = t.Turtle()
waste.ht()
waste.up()
waste.speed(0)
waste.shape("square")
waste.goto(right, 0)

def waste_left():
    global waste
    waste.goto(waste.pos()[0]-55, waste.pos()[1])

def pollute():
    global waste
    waste.stamp()
    if random.random() > 0.3:
        waste.goto(waste.pos()[0], waste.pos()[1]+random.triangular(-55,55))
    else:
        waste_left()

#---------------------------------------#
#           CLICK LISTENERS             #
#---------------------------------------#

elements = [ "earth","fire","wind","water","heart"]
colors = ["brown", "orange", "grey", "blue", "red"]
heroes = []
for i in range(len(elements)):
    t.register_shape(elements[i]+".gif")
    t1 = t.Turtle()
    t1.shape(elements[i]+".gif")
    t1.up()
    t1.goto(50+122*(i-1), -100)
    heroes.append(t1)

def click(x,y):
    global turn
    reset_state()
    screen.onclick(None) #Stop Listening
    heroes[turn%(len(heroes))].goto(x,y) #Move
    pollute()
    turn += 1
    screen.onclick(click) #Listen again
screen.onclick(click)

#---------------------------------------#
#  KEYBOARD LISTENERS: (num keys 1-5)   #
#---------------------------------------#

connector = t.Turtle()
connector.pensize(10)
connector.up()

state = []
def reset_state():
    global state, connector
    connector.clear()   #Clear all lines.
    connector.up()      #Connector ready for next sequence.
    state = []          #State initialized

def captain_planet():
    global state, connector
    print ("Captain Planet!")
    print (state)
    reset_state()

def command(key):
    global state, connector, colors
    def f():
        global state, connector, colors
        if len(state) > 0 and key in state[1:]:
            return
        #Begin Move to hero
        for i in range(len(heroes)):
            screen.onkey(None, str(i+1)) #Stop listening
        connector.goto(heroes[key].pos()) #Move
        for i in range(len(heroes)):
            screen.onkey(command(i), str(i+1)) #Listen again.
        #End Move
        connector.down()
        connector.pencolor(colors[key])
        if len(state)>0 and state[0] == key:
            captain_planet()
        else:
            state.append(key)
    return f

for i in range(len(heroes)):
    screen.onkey(command(i), str(i+1))
screen.listen()

#---------------------------------------#
#               MAIN LOOP               #
#---------------------------------------#
t.mainloop()