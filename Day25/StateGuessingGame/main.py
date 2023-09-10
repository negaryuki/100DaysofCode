import turtle
import pandas  


# setup screen:
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)  # Add shape to the screen in order to be available

turtle.shape(image)  # change shape to img file

# extract data from csv file:
data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
xcor_states = data.x
ycor_states = data.y

#-------------------------------------------------

# This function helps to find the xcor and ycor in a picture whenever you click on it

# def get_mouse_click_coor(x,y):
#   print(x,y)
# turtle.onscreenclick(get_mouse_click_coor())  

#-------------------------------------------------
  

guessed_states = []
while len(guessed_states) < 50:  #50 states

  # Pop-up to ask question:
  answer_state = screen.textinput(title= f"{len(guessed_states)}/50 States Correct",prompt = "what's another State?").title()
  
  if answer_state =="Exit":             # States to Learn
    missing_states = []
    
    for state in all_states:
      if state not in guessed_states:
        missing_states.append(state)
        
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv()"states_to_learn.csv"
        
    break                     # there is no need for the turtle.mainloop anymore

  if answer_state in all_states:
      guessed_states.append(answer_state)
      # create turtle to write down the name in the map
      t = turtle.Turtle()
      t.hideshape()
      t.penup()
      #state_data = data[data.state == answer_state]
      t.goto(int(xcor_states),int(ycor_states)) #state_data.x ,state_data.y
      t.write(answer_state) # state_data.state.item(). --> returns the first element 
  

# turtle.mainloop() # is an alternative for screen.exitonclick(). continues program even after code has finished running 
