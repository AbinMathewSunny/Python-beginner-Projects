BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

to_learn ={}
try:
  data = pandas.read_csv("data/words_to_learn.csv.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")


else:
   to_learn = data.to_dict(orient="records")




current_card={}



def next_card():
    global current_card,fliptimer
    window.after_cancel(fliptimer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French",fill="black")
    canvas.itemconfig(card_word, text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front_image)
    fliptimer=window.after(3000, func=flipcard)


def flipcard():
    canvas.itemconfig(card_title,text ="English",fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill= "white")
    canvas.itemconfig(card_background,image=card_back_image)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/ words_to_learn.csv",index=FALSE)
    next_card()




window = Tk()
window.title("Flashcard app")

window.config(padx=50,pady=50,bg = BACKGROUND_COLOR)


fliptimer = window.after(3000, func=flipcard)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")



canvas = Canvas(width=800,height=526)
card_background = canvas.create_image(400, 263,image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row =0,column=0,columnspan=2)
card_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"))


cross_imge = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_imge,highlightthickness=0,command =next_card )
unknown_button.grid(row=1,column=0)


check_imge = PhotoImage(file="images/right.png")
known_button = Button(image=check_imge,highlightthickness=0,command =is_known)
known_button.grid(row=1,column=1)

next_card()

window.mainloop()