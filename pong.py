import play #loading the play library
import random #loading the random library 

w = 400 #defines the global variable for horizontal size of court 
h = 500 #defines the global variable for the vertical size of court 
half_width = w / 2 #defining global variable for half width of court 
half_height = h / 2 #defining global varibale for half height of court 
score = 0 #defining global variable for score
speed = 3 #defining gloal varible for the speed of the ball 
@play.when_program_starts #creates a keyframe to start the game 
def do(): #defining or initializing the function DO
    play.set_backdrop( (35, 41, 129) ) #sets the background and its color 

court = play.new_box(  #declaring the variable that will be the play field, (play) calls the library, (.) query for a aprebuild function, (new_box) the prebuild function to create rectangles, the parenthesis holds the parameters 
    color = (200, 152, 15), #initializing the parameter 'color' to be purple
    x = 0, #initializing the X value, horozontal coordinate value
    y = 0, #initializing the Y value, vertical coordinates value
    width = w, #initializing the width to the pre set value 'w'
    height = h, #initializing the height to pre set value 'h'
) #closes parenthesis of parameters 


ball = play.new_circle( #declares the variable to hold a function for circle 
    color = "black", #initializing the parameter for color 
    radius = 10, #initializing the parameter radius to ten 
    x = 0, #initializing teh X coordinates to 0
    y = half_height - 30, #initializing the Y value with the half_height - 30 to have a fixed starting point 
    angle = random.randint(210,330), #initializing the bouncing angle 
) #closes parenthesis of parameters

paddle = play.new_box( #declares the variable to hold a fucntion for a paddle
    color = "dark blue", #initializing the parameter for color of paddle 
    width = 50, #initializing the width to 50 
    height = 10, #initializing the height to 10 
    x = 0, #initializinf the X coordinates to 0
    y = -half_height + 10,  #initializing the Y value with half_height + 10 to have a fixed starting point 
) #closes parameters 

score_text = play.new_text( #declares the varibale to hold a function for text 
    words = "SCORE: " + str(score), #initializing the display of words at the top of the court 
    x = 0, #initializinf the X coordinates to )
    y = half_height + 15, #initializing the Y value with half_height + 15 to have a fixed starting point 
    font = None, #intializing the font of the text "SCORE"
    color = "white", #intializing the color of the text "SCORE"
) 

'''
    angle_text = play.new_text(
    words = "Angle: " + str(ball.angle),
    x = 0, 
    y = -half_height - 15, 
    font = None 
    color = "white",
)
'''

@play.repeat_forever #keyframe to do the following as long as the game is being played 
def do(): #redefines the DO function 
    global score #calling for the global variable score 

    paddle.x = play.mouse.x #dot notation to recall the x parameter of paddle to reassign value to match mouse X coord
    #ensure the paddle isn't off playfield
    if(play.mouse.x < -half_width + paddle.width/2): #left side 
        paddle.x = -half_width + paddle.width/2
    if(play.mouse.x > half_width - paddle.width/2): #right side 
        paddle.x = half_width - paddle.width/2

    ball.move(speed)

    #bounce off top/bottom: 360 - angle 
    #top wall
    if(ball.y + ball.radius > half_height):
        ball.angle = 360 - ball.angle 

    #bottom wall 
    if(ball.y - ball.radius < -half_height):
        ball.angle = 360 - ball.angle 
        score -= 1 #score = score -1

    #bounce off left/right :180 - angle
    #right wall 
    if(ball.x + ball.radius > half_width):
        ball.angle = 180 - ball.angle

    #left wall
    if(ball.x - ball.radius < -half_width):
        ball.angle = 180 - ball.angle #make it bounce as if it hit the bottom and give it a little change of trajectory

    if(ball.is_touching(paddle)):
      #make it bounce as if it hit the bottom, and give it a little change of trajectory
      ball.angle = 360 - ball.angle + random.randint(-30, 30)
      ball.angle %= 360 #ensures angle is valid 

    #make sure the ball goes up after hitting the paddle
      if(ball.angle < 20):
          ball.angle = 20 
      elif(ball.angle > 160):
          ball.angle = 160 
      score += 1 
      if(score == 5):
        paddle.width -= 10

    ball.angle %= 360 #ensures angle is valid 
    score_text.words = "SCORE: " + str(score)
  #angle_text.words = "Angle: " + str(ball.angle)


play.start_program()