import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

import game_data

def number_game(parent): #es para cuando se llame desde el menu del juego
    window = tk.Toplevel()
    window.title("Guess the Number")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    width = 300
    height = 200
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
    window.resizable(False, False)
    counter = 0

    temperature_images = {
        i: ImageTk.PhotoImage(Image.open(f"number_img/temperature{i}.png").resize((60, 60)))
        for i in range(1,6)
    }

    number = random.randint(1,100)

    number_history = []

    def guess_submit():
        nonlocal number
        nonlocal number_history
        guess = entry.get()

        if guess.isdigit(): 
             
        
            difference = abs(int(guess) - number)

            number_history.append(guess)
            label_history.config(text=", ".join(number_history))

            if difference == 0: #win
                    messagebox.showinfo("","--You guessed right!, A new number has been generated--")
                    label_clue.config(text="Type your guess! (A number between 1-100)", fg="#000000")#reseteamos la info
                    label_temperature.config(image="")
                    label_history.config(text="")
                    entry.delete(0, tk.END)
                    number = random.randint(1,100)

                    #money
                    game_data.money += 200

            elif difference < 4:
                label_clue.config(text="HOT HOT!", fg="#FF0000")
                label_temperature.config(image=temperature_images[5])
                entry.delete(0, tk.END)
            elif difference < 7:
                label_clue.config(text="Hot", fg="#FF4500")
                label_temperature.config(image=temperature_images[4])
                entry.delete(0, tk.END)
            elif difference < 16:
                label_clue.config(text="Warm", fg="#BCA313")
                label_temperature.config(image=temperature_images[3])
                entry.delete(0, tk.END)
            elif difference < 21:
                label_clue.config(text="Cold", fg="#87CEFA")
                label_temperature.config(image=temperature_images[2])
                entry.delete(0, tk.END)
            else:
                label_clue.config(text="Freezing...", fg="#216EF2")
                label_temperature.config(image=temperature_images[1])
                entry.delete(0, tk.END)
        else:
            label_clue.config(text="Please, type a valid number", fg="#000000")


    label_clue = tk.Label(window, text="Type your guess! (A number between 1-100)")
    label_clue.pack()

    label_temperature = tk.Label(window)
    label_temperature.pack()

    guess_frame = tk.Frame(window)
    guess_frame.pack()

    label_history = tk.Label(window, wraplength=280)
    label_history.pack()

    entry = tk.Entry(guess_frame, width=30)
    entry.pack(pady=5)

    entry.bind("<Return>", lambda event: guess_submit()) #le bindeamos el enter al campo entry para ejecutar asi la funcion al presionar enter

    btn_roll = tk.Button(guess_frame, text="Sumbit", command=guess_submit)
    btn_roll.pack(pady=5)


   #al cerrar la ventana del juego:
    def on_close():
        window.destroy()
        game_data.game_open = False

    window.protocol("WM_DELETE_WINDOW", on_close)
