import random
from turtle import Screen, Turtle, TK
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from black_overlay import Black_overlay
import time
import tkinter as tk
from tkinter import messagebox

# Set up the screen
screen = Screen()
screen.setup(600, 600)
screen.title("Guess the City")
overlay = Black_overlay()
city_names = ["alkmaar", "amersfoort", "amsterdam","bourtange", "delft", "dordrecht","franeker", "gouda", "groningen", "haarlem", "leiden", "leeuwarden", "middelburg","naarden", "utrecht", "woerden", "zwolle"]
hidden_city = random.choice(city_names)
hidden_image = f"cities/{hidden_city}.png"
screen.bgpic(hidden_image)

print(hidden_city)

score_board = ScoreBoard()
slang = Snake()
food = Food()

# Configure controls
screen.listen()
screen.onkey(slang.turn_left, "Left")
screen.onkey(slang.turn_right, "Right")
screen.onkey(slang.turn_up, "Up")
screen.onkey(slang.turn_down, "Down")

screen.tracer(0)


# Display the messagebox and wait until it is closed
def show_messagebox_and_reset(title, message, reset_needed=False):
    messagebox.showinfo(title, message)
    # Reset the snake only if specified
    if reset_needed:
        slang.reset()

def check_answer():
    answer = city_entry.get()
    if answer.lower() == hidden_city.lower():
        show_messagebox_and_reset("Correct!", f"Nice! Your score is {len(score_board.hearts)}!")
        window.destroy()
    else:
        if len(score_board.hearts) == 1:
            show_messagebox_and_reset("Game Over", f"Sorry, you got 0 score. The city is {hidden_city}.")
            window.destroy()
        else:
            score_board.loss_heart()
            show_messagebox_and_reset("Try Again", f"Wrong! {len(score_board.hearts)} hearts left.", reset_needed=True)
            window.withdraw()  # Hide the prompt window instead of destroying it


# Initialize Tkinter window at the start
window = tk.Tk()
window.withdraw()  # Start with the window hidden
window.title("Guess")
window.config(padx= 40, pady=20)
tk.Label(window, text="Which CITY is it?").grid(column=0, row=0)
city_entry = tk.Entry(window)
city_entry.grid(column=0, row=1, pady=10)
tk.Button(window, text="Submit", command=check_answer).grid(column=0, row=2)

# Modified guess_city_prompt function
def guess_city_prompt():
    # city_entry.delete(0, tk.END)  # Clear any previous text
    window.deiconify()  # Show the window
    city_entry.focus_set()


def trigger_guess_prompt():
    screen.ontimer(guess_city_prompt, 300)  # Delay by 0.3 seconds

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    slang.move()

    # Check collision with food
    if slang.lichaam_lijst[0].distance(food) < 28:
        food.refresh()
        slang.extend()
        score_board.clear()
        score_board.add_score()

    # Check for wall collision
    if (slang.head.xcor() > 280 or slang.head.xcor() < -280 or
        slang.head.ycor() > 280 or slang.head.ycor() < -280):
        for seg in slang.lichaam_lijst:
            overlay.clear_area(seg.xcor(), seg.ycor())
        trigger_guess_prompt()
        # slang.reset()

    # Check for self-collision
    for segment in slang.lichaam_lijst[1:]:
        if slang.head.distance(segment) < 10:
            for seg in slang.lichaam_lijst:
                overlay.clear_area(seg.xcor(), seg.ycor())
            trigger_guess_prompt()
            # slang.reset()

screen.exitonclick()
