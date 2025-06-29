import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

import game_data

def dice_game(parent): #es para cuando se llame desde el menu del juego
    window = tk.Toplevel()
    window.title("Dice Game")
    #centrar ventana
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    width = 300
    height = 300
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
    window.resizable(False, False)
    counter = 0

    dice_images = {
        i: ImageTk.PhotoImage(Image.open(f"dice_img/die{i}.png").resize((60, 60)))
        for i in range(1,7)
    }

    face_images = {
        i: ImageTk.PhotoImage(Image.open(f"dice_img/face{i}.png").resize((60, 60)))
        for i in range(0,6)
    }


    def roll_dice(): #ejecutado al oprimir el botón
        
        nonlocal counter
        counter += 1
        no1 = random.randint(1,6)
        no2 = random.randint(1,6)
        
        label_count.config(text=f"Tries: {counter}")
        label_dice1.config(image=dice_images[no1]) #reemplazarn al default de las label
        label_dice2.config(image=dice_images[no2])

        if no1 == no2: #win
            messagebox.showinfo("","--Doubles! You win!--")
            label_count.config(text=f"Tries: 0")
            label_dice1.config(text=f"Die 1: ")
            label_dice2.config(text=f"Die 2: ")
            counter = 0 
            label_face.config(image=face_images[1])

            #money
            game_data.money += 100
            

        elif counter == 1:
            label_face.config(image=face_images[1])
        elif counter == 3:
            label_face.config(image=face_images[2])
        elif counter == 5:
            label_face.config(image=face_images[3])
        elif counter == 7:
            label_face.config(image=face_images[4])
        elif counter == 10:
            label_face.config(image=face_images[5])


    label_count = tk.Label(window, text=f"Tries: 0",pady=20)
    label_count.pack()

    dice_frame = tk.Frame(window)
    dice_frame.pack()

    label_dice1 = tk.Label(dice_frame) #texto que tendran por default las label
    label_dice1.pack(side="left", padx=5)

    label_dice2 = tk.Label(dice_frame)
    label_dice2.pack(side="right", padx=5)

    btn_roll = tk.Button(window, text="Roll the Dice", command=roll_dice)
    btn_roll.pack(pady=20)

    label_face = tk.Label(window, image=face_images[0])
    label_face.pack()


    #al cerrar la ventana del juego:
    def on_close():
        window.destroy()
        game_data.game_open = False

    window.protocol("WM_DELETE_WINDOW", on_close)

