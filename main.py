import pandas
import random
from playsound import playsound
from tkinter import *
BG = "#B1DDC6"
current_card = {}


def french():
    try:
        data = pandas.read_csv("assets/french_words.csv")
    except FileNotFoundError:
        original_data1 = pandas.read_csv("assets/french_words.csv")
        to_learn = original_data1.to_dict(orient="records")
    else:
        to_learn = data.to_dict(orient="records")

    def flip_card():
        canvas1.itemconfig(card_title, text="English", fill="white")
        canvas1.itemconfig(card_word, text=current_card["English"], fill="white")
        canvas1.itemconfig(card_background, image=card_back_image)

    def next_card():
        global current_card
        current_card = random.choice(to_learn)
        canvas1.itemconfig(card_title, text="French", fill="black")
        canvas1.itemconfig(card_word, text=current_card["French"], fill="black")
        canvas1.itemconfig(card_background, image=card_front_image)

    def is_known():
        to_learn.remove(current_card)
        data1 = pandas.DataFrame(to_learn)
        data1.to_csv("assets/Words_to_learn.csv", index=False)
        # label1.config(text=f"{93-len(to_learn)} | 93")
        next_card()
    canvas.destroy()
    title.destroy()
    french_button.destroy()
    spanish_button.destroy()
    sanskrit_button.destroy()
    chinese_button.destroy()
    canvas1 = Canvas(width=700, height=500, bg=BG, highlightthickness=0)
    french_title = Label(text="French Language", font=("Ariel", 80, "bold"), bg=BG)
    french_title.place(x=275, y=15)
    card_front_image = PhotoImage(file="assets/card_front.png")
    card_back_image = PhotoImage(file="assets/card_back.png")
    card_background = canvas1.create_image(300, 197, image=card_front_image)
    card_title = canvas1.create_text(300, 50, text="", font=("Ariel", 40, "italic"))
    card_word = canvas1.create_text(300, 197, text="", font=("Ariel", 60, "bold"))
    cross_img = PhotoImage(file="assets/wrong.png")
    unknown_button = Button(image=cross_img, highlightthickness=0, command=flip_card)
    check_img = PhotoImage(file="assets/right.png")
    unknown_button.photoimage = check_img
    known_button = Button(image=check_img, highlightthickness=0, command=is_known)
    known_button.photoimage = cross_img
    canvas1.config(bg=BG, highlightthickness=0)
    canvas1.place(x=450, y=200)
    known_button.place(x=1050, y=600)
    unknown_button.place(x=350, y=600)
    next_card()


def chinese():
    try:
        data = pandas.read_csv("assets/Data.csv")
    except FileNotFoundError:
        original_data1 = pandas.read_csv("assets/Data.csv")
        to_learn = original_data1.to_dict(orient="records")
    else:
        to_learn = data.to_dict(orient="records")
    canvas.destroy()
    title.destroy()
    french_button.destroy()
    spanish_button.destroy()
    sanskrit_button.destroy()
    chinese_button.destroy()
    canvas1 = Canvas(width=700, height=500, bg=BG, highlightthickness=0)
    french_title = Label(text="Mandarin Language", font=("Ariel", 80, "bold"), bg=BG)
    french_title.place(x=275, y=15)
    card_front_image = PhotoImage(file="assets/card_front.png")
    card_back_image = PhotoImage(file="assets/card_back.png")
    card_background = canvas1.create_image(300, 197, image=card_front_image)
    card_title = canvas1.create_text(300, 50, text="", font=("Ariel", 40, "italic"))
    card_word = canvas1.create_text(300, 197, text="", font=("Ariel", 60, "bold"))
    canvas1.config(bg=BG, highlightthickness=0)
    canvas1.place(x=450, y=200)

    def flip_card():
        global current_card
        canvas1.itemconfig(card_title, text="English", fill="white")
        canvas1.itemconfig(card_word, text=current_card["English"], fill="white")
        canvas1.itemconfig(card_background, image=card_back_image)

    def next_card():
        global current_card
        current_card = random.choice(to_learn)
        canvas1.itemconfig(card_title, text="Mandarin", fill="black")
        canvas1.itemconfig(card_word, text=current_card["Mandarin"], fill="black")
        canvas1.itemconfig(card_background, image=card_front_image)

    def is_known():
        to_learn.remove(current_card)
        data1 = pandas.DataFrame(to_learn)
        data1.to_csv("assets/Words_to_learn.csv", index=False)
        # label1.config(text=f"{93-len(to_learn)} | 93")
        next_card()

    def play():
        global current_card
        playsound(current_card["Audio"])

    cross_img = PhotoImage(file="assets/wrong.png")
    unknown_button = Button(image=cross_img, highlightthickness=0, command=flip_card)
    unknown_button.place(x=350, y=600)
    check_img = PhotoImage(file="assets/right.png")
    known_button = Button(image=check_img, highlightthickness=0, command=is_known)
    known_button.place(x=1050, y=600)
    unknown_button.photoimage = cross_img
    known_button.photoimage = check_img
    play_button = Button(text="How to pronounce?", font=("Helvetica", 32),
                         relief=GROOVE, command=play)
    play_button.place(x=550, y=600)
    next_card()


def spanish():
    try:
        data = pandas.read_csv("assets/spanish_words.csv")
    except FileNotFoundError:
        original_data1 = pandas.read_csv("assets/spanish_words.csv")
        to_learn = original_data1.to_dict(orient="records")
    else:
        to_learn = data.to_dict(orient="records")
    canvas.destroy()
    title.destroy()
    french_button.destroy()
    spanish_button.destroy()
    sanskrit_button.destroy()
    chinese_button.destroy()
    canvas1 = Canvas(width=700, height=500, bg=BG, highlightthickness=0)
    spanish_title = Label(text="Spanish Language", font=("Ariel", 80, "bold"), bg=BG)
    spanish_title.place(x=275, y=15)
    card_front_image = PhotoImage(file="assets/card_front.png")
    card_back_image = PhotoImage(file="assets/card_back.png")
    card_background = canvas1.create_image(300, 197, image=card_front_image)
    card_title = canvas1.create_text(300, 50, text="", font=("Ariel", 40, "italic"))
    card_word = canvas1.create_text(300, 197, text="", font=("Ariel", 60, "bold"))
    canvas1.config(bg=BG, highlightthickness=0)
    canvas1.place(x=450, y=200)

    def flip_card():
        global current_card
        canvas1.itemconfig(card_title, text="English", fill="white")
        canvas1.itemconfig(card_word, text=current_card["English"], fill="white")
        canvas1.itemconfig(card_background, image=card_back_image)

    def next_card():
        global current_card
        current_card = random.choice(to_learn)
        canvas1.itemconfig(card_title, text="Spanish", fill="black")
        canvas1.itemconfig(card_word, text=current_card["Spanish"], fill="black")
        canvas1.itemconfig(card_background, image=card_front_image)

    def is_known():
        to_learn.remove(current_card)
        data1 = pandas.DataFrame(to_learn)
        data1.to_csv("assets/Words_to_learn.csv", index=False)
        # label1.config(text=f"{93-len(to_learn)} | 93")
        next_card()

    cross_img = PhotoImage(file="assets/wrong.png")
    unknown_button = Button(image=cross_img, highlightthickness=0, command=flip_card)
    unknown_button.place(x=350, y=600)
    check_img = PhotoImage(file="assets/right.png")
    known_button = Button(image=check_img, highlightthickness=0, command=is_known)
    known_button.place(x=1050, y=600)
    unknown_button.photoimage = cross_img
    known_button.photoimage = check_img
    next_card()


def sanskrit():
    try:
        data = pandas.read_csv("assets/sanskrit_words.csv")
    except FileNotFoundError:
        original_data1 = pandas.read_csv("assets/sanskrit_words.csv")
        to_learn = original_data1.to_dict(orient="records")
    else:
        to_learn = data.to_dict(orient="records")
    canvas.destroy()
    title.destroy()
    french_button.destroy()
    spanish_button.destroy()
    sanskrit_button.destroy()
    chinese_button.destroy()
    canvas1 = Canvas(width=700, height=500, bg=BG, highlightthickness=0)
    sanskrit_title = Label(text="Sanskrit Language", font=("Ariel", 80, "bold"), bg=BG)
    sanskrit_title.place(x=275, y=15)
    card_front_image = PhotoImage(file="assets/card_front.png")
    card_back_image = PhotoImage(file="assets/card_back.png")
    card_background = canvas1.create_image(300, 197, image=card_front_image)
    card_title = canvas1.create_text(300, 50, text="", font=("Ariel", 40, "italic"))
    card_word = canvas1.create_text(300, 197, text="", font=("Ariel", 60, "bold"))
    canvas1.config(bg=BG, highlightthickness=0)
    canvas1.place(x=450, y=200)

    def flip_card():
        global current_card
        canvas1.itemconfig(card_title, text="English", fill="white")
        canvas1.itemconfig(card_word, text=current_card["English"], fill="white")
        canvas1.itemconfig(card_background, image=card_back_image)

    def next_card():
        global current_card
        current_card = random.choice(to_learn)
        canvas1.itemconfig(card_title, text="Sanskrit", fill="black")
        canvas1.itemconfig(card_word, text=current_card["Sanskrit"], fill="black")
        canvas1.itemconfig(card_background, image=card_front_image)

    def is_known():
        to_learn.remove(current_card)
        data1 = pandas.DataFrame(to_learn)
        data1.to_csv("assets/Words_to_learn.csv", index=False)
        next_card()

    cross_img = PhotoImage(file="assets/wrong.png")
    unknown_button = Button(image=cross_img, highlightthickness=0, command=flip_card)
    unknown_button.place(x=350, y=600)
    check_img = PhotoImage(file="assets/right.png")
    known_button = Button(image=check_img, highlightthickness=0, command=is_known)
    known_button.place(x=1050, y=600)
    unknown_button.photoimage = cross_img
    known_button.photoimage = check_img
    next_card()


window = Tk()
logo = PhotoImage(file="assets/logo.png")
window.title("LET'S LEARN !")
window.config(padx=50, pady=50, bg=BG, height=768, width=1366)
canvas = Canvas(width=500, height=500, bg=BG, highlightthickness=0)
canvas.create_image(225, 300, image=logo)
canvas.place(x=120, y=120)
title = Label(text="Learn it easy !", font=("Ariel", 80, "bold"), bg=BG)
title.place(x=300, y=15)
score = Label(text="", bg=BG, highlightthickness=0)
french_button = Button(text="French", font=("Ariel", 40, "bold"), command=french)
french_button.place(x=750, y=250)
chinese_button = Button(text="Mandarin", font=("Ariel", 40, "bold"), command=chinese)
chinese_button.place(x=1000, y=250)
spanish_button = Button(text="Spanish", font=("Ariel", 40, "bold"), command=spanish)
spanish_button.place(x=750, y=450)
sanskrit_button = Button(text="Sanskrit", font=("Ariel", 40, "bold"), command=sanskrit)
sanskrit_button.place(x=1020, y=450)
window.mainloop()
