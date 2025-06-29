import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk
import winsound
import game_data


def mole_game(parent):

    mole_img = ImageTk.PhotoImage(Image.open("mole_img/mole.png").resize((50, 50)))

    window = tk.Toplevel()
    window.title("Guess the Number")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    width = 500
    height = 500
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
    window.resizable(False, False)
    score = 0

    def mole_start():

        #timer
        timer = 15

        def start_countdown():
            
            def countdown():
                nonlocal timer
                nonlocal score
                if timer > 1:
                    timer -= 1
                    timer_label.config(text=f"Time: {timer}")
                    window.after(1000,countdown)
                else: #time out

                    


                    message_label.config(text=f"Game Over! Final score: {score}\nClick the Start button when you are ready")
                    timer_label.pack_forget()

                    #quitar al topo - regresar el start - resetear score

                    mole.place_forget()
                    btn_start.pack()
                    

                    messagebox.showinfo("",f"--Time's up! Score: {score}--")
                    score = 0

            timer_label.config(text=f"Time: {timer}")
            window.after(1000,countdown)
        timer_label.pack(pady=5)
        


        
        mx_position = random.randint(50,400)
        my_position = random.randint(50,400)
        mole.place(x=mx_position, y=my_position)
        btn_start.pack_forget()

        message_label.config(text=f"Score: {score}")

        start_countdown()

    def mole_whacked():

        #point winned
        nonlocal score
        score += 1
        message_label.config(text=f"Score: {score}")
        winsound.PlaySound("mole_img/mole_hit.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

        mx_position = random.randint(50,400)
        my_position = random.randint(50,400)
        mole.place(x=mx_position, y=my_position)

        #money
        game_data.money += 10
        

    message_label = tk.Label(window, text="Click the Start button when you are ready")
    message_label.pack(pady=5)

    timer_label = tk.Label(window)
    timer_label.pack_forget()
    timer_label.pack(pady=5)

    mole = tk.Button(window, command=mole_whacked, image=mole_img)
    mole.image = mole_img


    btn_start = tk.Button(window, text="Start", command=mole_start, bg ="lightgreen")
    btn_start.pack(pady=5)
    

       #al cerrar la ventana del juego:
    def on_close():
        window.destroy()
        game_data.game_open = False

    window.protocol("WM_DELETE_WINDOW", on_close)