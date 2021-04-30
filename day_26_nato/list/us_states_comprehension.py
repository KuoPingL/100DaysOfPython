import pandas as pd
import turtle as tt


def get_mouse_click_coor(x, y):
    print(x, y)


screen = tt.Screen()
screen.title(titlestring="US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
tt.shape(image)

screen.listen()
tt.onscreenclick(get_mouse_click_coor)

is_game_done = False
df = pd.read_csv("50_states.csv")

print(df.state)

guessed_states = []
missed_states = []

print(df.state.shape[0])
print(df.shape)

while len(guessed_states) < df.state.shape[0]:

    if len(guessed_states) == 0:
        answer = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    else:
        answer = screen.textinput(title=f"{len(guessed_states)}/{df.state.shape[0]} Correct",
                                  prompt="What's another state's name?").title()

    if answer == "Quit":
        # CHANGE to COMPREHENSION
        # for state in df.state:
        #     if state not in guessed_states:
        #         missed_states.append(state)
        missed_states = [state for state in df.state if state not in guessed_states]

        print(missed_states)
        break

    if answer in df.state.tolist():
        data = df[df.state == answer]
        # print(data)
        # print(data.x.item())
        # print(data.y.item())
        temp_tt = tt.Turtle()
        temp_tt.penup()
        temp_tt.hideturtle()
        # temp_tt.goto(data.x.item(), data.y.item())
        temp_tt.goto(int(data.x), int(data.y))
        temp_tt.write(data.state.item())
        guessed_states.append(answer)

# states to learn csv
# https://stackoverflow.com/a/42133330/9795114
if len(guessed_states) < df.state.shape[0]:
    states = df[~df.state.isin(guessed_states)]
    # https://cmdlinetips.com/2018/04/how-to-reset-index-in-pandas-dataframe/
    # states.reset_index(drop=True)
    states.to_csv("states_to_learn.csv")

# keep the screen open
tt.mainloop()
