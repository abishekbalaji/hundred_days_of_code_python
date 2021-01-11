import turtle
import pandas

FONT = ('Arial', 12, 'normal')
ALIGNMENT = 'center'

screen = turtle.Screen()
screen.title("U.S.States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()
states_data = pandas.read_csv('50_states.csv')
states_list = states_data.state.to_list()

text = turtle.Turtle()
text.pu()
text.hideturtle()

answered_states = []


while len(answered_states) <= 50:
    answer_state = screen.textinput(title=f"{len(answered_states)}/50 Correct", prompt="Enter a state's name.").title()
    if answer_state == "Exit":
        unanswered_states_data = [state for state in states_list if state not in answered_states]
        df = pandas.DataFrame(unanswered_states_data)
        df.to_csv('unanswered.csv')
        break
    elif answer_state in states_list:
        state_data = states_data[states_data.state == answer_state]
        print(state_data)
        text.goto(int(state_data.x), int(state_data.y))
        text.write(arg=answer_state, move=False, align=ALIGNMENT, font=FONT)
        answered_states.append(answer_state)
turtle.mainloop()
