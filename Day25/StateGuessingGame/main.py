import turtle
import pandas  

# setup screen:
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)  # Add shape to the screen in order to be available

turtle.shape(image)  # change shape to img file


#-------------------------------------------------

# This function helps to find the xcor and ycor in a picture whenever you click on it

# def get_mouse_click_coor(x,y):
#   print(x,y)
# turtle.onscreenclick(get_mouse_click_coor())  

#-------------------------------------------------
  
# Pop-up to ask question:
answer_state = scree.textinput(title="Guess the State",prompt = "what's another State?")




turtle.mainloop() # is an alternative for screen.exitonclick(). continues program even after code has finished running 
