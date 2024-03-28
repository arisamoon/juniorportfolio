import play
w=300
h=300
@play.when_program_starts
def do():
  play.screen.width = w
  play.screen.height = h
#box start 
box = play.new_box(
  color=(255,233,200),
  x=252 ,
  y=70 ,
  width=w ,
  height=h ,
)
play.set_backdrop((0,0,110))

#face start
A_head = play.new_circle(
  color = "red",
  x = 155, 
  y = -10,
  radius = 30,
)
A_L_eye = play.new_circle(
  color = "black",
  x= 143,
  y=-7, 
  radius= 3, 
  border_color = "black",
  border_width = 1,
)
A_R_eye = play.new_circle(
  color = "black",
  x= 170,
  y=-7, 
  radius= 3, 
  border_color = "black",
  border_width = 1,
)
A_nose = play.new_circle(
  color = "black",
  x= 158,
  y= -17, 
  radius= 3, 
  border_color = "black",
  border_width = 1,
)
hmouth = play.new_box(
 color = "black",
x = 158,
 y = -30,
 width = 15,
 height = 5,
)
#face end, text display 
text =play .new_text(
  color= "red",
  words="why is dog food so bad..",
  x=255,
  y=33,
  font_size=20,
)

@play.repeat_forever
async def speak_slowly():
  await play.timer(seconds=2)
  text.words="No, it's not, my dog likes his food>:("
#end text display, start mouse coord 
  mouse_text= play.new_text(
    color= "green",
  words=" ",
  x=0,
  y=0,
  font_size=20,
  )
  @play.repeat_forever
  def mouse_coords():
    mouse_text.go_to(play.mouse)
    mouse_text.words = str(int(play.mouse.x))+", "+str(int(play.mouse.y))
play.start_program()