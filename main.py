import turtle as t
import pandas as pd

FONT = ("Arial", 16, "normal")
CENTER = "center"

def get_mouse_click_cor(x, y):
    print(x, y)
    
# Function to add letter at x,y coordinates
def add_state(letter, x, y):
    t.penup()
    t.write(letter, align="center", font=FONT)

screen = t.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()  # 印出所有的state。
guessed_states = []

# 可以用append的方式，找到數字。
while len(guessed_states) < 50:
    # Add title()，可以用在確認不管是否能用在辨識大小寫。
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50 Guess the State",
                                    prompt="What's another state's name").title()
    if answer_state == "Exit":
        # Changed to List comprehension
        missing_list = [ element for element in all_states if element not in guessed_states ]
        # 把資料轉成csv
        df = pd.DataFrame(guessed_states)
        df.to_csv('leftover_city.csv')
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        print(f"Correct Answer { answer_state }")
        state_data = data[data.state == answer_state].iloc[0] # 找到相同state，取出state那一欄的數值。
        x_loc, y_loc = state_data.x, state_data.y             # 透過state_data.x找到x_loc, y_loc。
        add_state(answer_state, x_loc, y_loc)                 # 加上州的資料。

t.mainloop()
screen.exitonclick()

"""
1. Convert the guess to Title case
2. Check if the guess is among the 50 states
3. Write correct guesses onto the map
4. Use a loop to allow the user to keep guessing
5. Record the correct guesses in a list
6. Keep track of the score
"""