# from turtle import Turtle, Screen
# import time
# tim = Turtle("turtle")
# tim.penup()
# screen = Screen()
# screen.tracer(0)
# moving = True
# screen.listen()
#
#
# def reset():
#     tim.goto(0, 0)
#
#
# screen.onkey(reset, "c")
#
# while tim.xcor() < 250:
#     screen.update()
#     time.sleep(0.1)
#     tim.forward(10)
#     with open("test.txt", mode="a") as test_data:
#         test_data.write(f"{tim.xcor()}\n")
#     print(tim.xcor())
#
# clear = screen.textinput(title="Do you want to clear the text file ?", prompt='Type \'yes\' or \'no\'').lower()
# if clear == 'yes':
#     with open('test.txt', mode='w') as clear_data:
#         clear_data.write('')
#
#
# screen.exitonclick()
