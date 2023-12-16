import pandas
import tkinter as tk
import random

FONT = "Arial"
BACKGROUND = "#ffdbc5"
FONT_COLOR = "#2e112d"
DECISION_COLOR = "#b01c33"

data = pandas.read_csv("./restaurant.csv")


def category_roll():
    """Extracts food category to a list and returns a random selection"""
    category_list = data["category"].to_list()
    category_list = list(set(category_list))

    category_choice = random.choice(category_list).title()
    decision_label.config(text=category_choice)

window = tk.Tk()
window.title("Roll for Food")
window.config(padx=20, pady=20, bg=BACKGROUND, highlightthickness=0)

canvas = tk.Canvas(width=200, height=200, bg=BACKGROUND, highlightthickness=0)
d20_img = tk.PhotoImage(file="./images/d20.png")
canvas.create_image(100, 100, image=d20_img)
canvas.grid(row=2, column=1, padx=20, pady=10)

decide_label = tk.Label(text="Still Deciding?", font=(FONT, 36, "bold"))
decide_label.config(bg=BACKGROUND, fg=FONT_COLOR)
decide_label.grid(row=0, column=1)

get_label = tk.Label(text="Get:", font=(FONT, 28, "bold"))
get_label.config(bg=BACKGROUND, fg=FONT_COLOR)
get_label.grid(row=3, column=1)

decision_label = tk.Label(text="Something", font=(FONT, 32, "bold"))
decision_label.config(bg=BACKGROUND, fg=DECISION_COLOR)
decision_label.grid(row=4, column=1)

decide_button = tk.Button(text="Roll for Food", font=(FONT, 12, "normal"), command=category_roll)
decide_button.grid(row=1, column=1, pady=10)

window.mainloop()
