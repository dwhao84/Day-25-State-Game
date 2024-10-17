import turtle as t
import pandas

FONT = ("Arial", 16, "normal")
CENTER = "center"

def get_mouse_click_cor(x, y):
    print(x, y)
    
# Function to add letter at x,y coordinates
def add_state(letter, x, y):
    t.penup()
    t.write(letter, align="center", font=FONT)
    
# Set a score as variable
score = 0

is_finish = True

screen = t.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"]  # 找到所有的state。
print(states)           # 印出所有的state。

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name")
for answer in states:
    if answer == answer_state:
        score += 1
        print(f"Correct Answer { answer_state }")
        # 找到相同state，取出state那裡面的數值。
        state_data = data[data.state == answer_state].iloc[0]
        # 透過state_data.x找到x_loc, y_loc。
        x_loc, y_loc = state_data.x, state_data.y
        # 加上州的資料。
        add_state(answer_state, x_loc, y_loc)
    else:
        print("you're enter the wrong answer.")
        
print(score) # 計算分數
print(f"{ answer_state }")
screen.title(f"{ score } / 50 States Correct")

# t.onscreenclick(get_mouse_click_cor)
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