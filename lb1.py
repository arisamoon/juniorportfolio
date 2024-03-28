def emoji():
  import play # this is the first line in the program

  B_head = play.new_circle(
    color = "black",
    x = 130, 
    y = 190,
    radius = 40,
  )
  eye_B_B=play.new_circle(
    color="red",
    x = 110,
    y = 190, 
    radius = 5
  )
  eye_B_B=play.new_circle(
    color= "red",
    x = 150,
    y = 190, 
    radius = 5
  )
  Bnose = play.new_circle(
    color = "white",
    x= 130,
    y= 185, 
    radius= 5, 
  )
  Bmouth = play.new_circle(
      color = "red",
      x = 130,
      y = 165,
      radius= 10,
  )

  A_head = play.new_circle(
    color = "red",
    x = 20, 
    y = 100,
    radius = 30,
  )
  A_L_eye = play.new_circle(
    color = "black",
    x= 10,
    y=110, 
    radius= 3, 
    border_color = "black",
    border_width = 1,
  )
  A_R_eye = play.new_circle(
    color = "black",
    x= 30,
    y=110, 
    radius= 3, 
    border_color = "black",
    border_width = 1,
  )
  A_nose = play.new_circle(
    color = "black",
    x= 20,
    y= 95, 
    radius= 3, 
    border_color = "black",
    border_width = 1,
  )
  hmouth = play.new_box(
      color = "black",
      x = 20,
      y = 80,
      width = 15,
      height = 5,
  )

  S_head = play.new_circle(
    color = "lightblue",
    x = 30, 
    y = 200,
    radius = 40,
  )
  eye_S_S=play.new_circle(
    color="blue",
    x = 10,
    y = 200, 
    radius = 3
  )
  eye_S_S=play.new_circle(
    color="blue",
    x = 50,
    y = 200, 
    radius = 6
  )
  sbrow = play.new_box(
      color = "red",
      x = 10,
      y = 210,
      width = 25,
      height = 2,
  )
  sbrow = play.new_box(
      color = "red",
      x = 50,
      y = 210,
      width = 25,
      height = 2,
  )
  snose = play.new_circle(
    color = "white",
    x= 30,
    y= 195, 
    radius= 5, 
  )
  smouth = play.new_box(
      color = "red",
      x = 30,
      y = 180,
      width = 45,
      height = 3,
  )
  sm = play.new_box(
      color = "red",
      x = 30,
      y = 180,
      width = 5,
      height = 15,
  )
  sm = play.new_box(
      color = "red",
      x = 10,
      y = 180,
      width = 5,
      height = 15,
  )
  sm = play.new_box(
      color = "red",
      x = 50,
      y = 180,
      width = 5,
      height = 15,
  )



  head5 = play.new_circle(
    color = "pink",
    x = 10, 
    y = 11,
    radius = 50,
  )
  body = play.new_circle(
    color = "pink",
    x = 100, 
    y = 10,
    radius = 60,
  )
  eye_T_H = play.new_circle(
    color = "white",
    x= -10,
    y=20, 
    radius= 8, 
    border_color = "black",
    border_width = 1,
  )
  eye_T_H = play.new_circle(
    color = "black",
    x= -10,
    y=20, 
    radius= 3, 
    border_color = "black",
  )
  eye_L_H = play.new_circle(
    color = "white",
    x= 30,
    y=20, 
    radius= 8, 
    border_color = "black",
    border_width = 1,
  )
  eye_L_H = play.new_circle(
    color = "white",
    x= 30,
    y=20, 
    radius= 8, 
    border_color = "black",
    border_width = 1,
  )
  eye_L_H = play.new_circle(
    color = "black",
    x= 30,
    y=20, 
    radius= 3, 
    border_color = "black",
    border_width = 1,
  )
  ears_L = play.new_circle(
    color = "pink",
    x= -20,
    y=50, 
    radius= 20, 
  )
  ears_R = play.new_circle(
    color = "pink",
    x= 40,
    y=50, 
    radius= 20, 
  )
  hnose = play.new_circle(
    color = "red",
    x= 10,
    y=3, 
    radius= 5,
    border_color = "black",
    border_width = 1,
  )
  hmouth = play.new_box(
      color = "black",
      x = 10,
      y = -20,
      width = 25,
      height = 25,
  )
  hmouth = play.new_box(
      color = "red",
      x = 10,
      y = -27,
      width = 9,
      height = 9,
  )
  leg = play.new_box(
    color = "pink",
    x = 70,
    y = -55,
    width = 9,
    height = 30,
)
  leg = play.new_box(
    color = "pink",
    x = 130,
    y = -55,
    width = 9,
    height = 30,
)
  play.start_program()