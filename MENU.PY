import tkinter as tk
from tkinter import ttk
from DICE import dice_game
from NUMBER import number_game
from MOLE import mole_game
import game_data
from PIL import Image, ImageTk
import random
from tkinter import messagebox
import pygame
pygame.mixer.init()


def open_diceGame():

    if game_data.game_open == False:
        game_data.game_open = True
        dice_game(root)
    
def open_numberGame():

    if game_data.game_open == False:
        game_data.game_open = True
        number_game(root)
    

def open_moleGame():

    if game_data.game_open == False:
        game_data.game_open = True
        mole_game(root)
    


root = tk.Tk()
root.title("Main Menu")
#centrar ventana
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 500
height = 800
x = (screen_width - width) // 2
y = (screen_height - height) // 2
root.geometry(f"{width}x{height}+{x}+{y}")
root.resizable(False, False)


label_welcome = tk.Label(root, text=f"Welcome! Please, select your game:", pady=20)
label_welcome.pack()

btn_diceGame = tk.Button(root, text="Dice Game", bg= "lightblue", command=open_diceGame,pady=8 )
btn_diceGame.pack(pady=10)

btn_guessGame = tk.Button(root, text="Guess the Number", bg= "lightgreen", command=open_numberGame, pady=8)
btn_guessGame.pack(pady=10)

btn_moleGame = tk.Button(root, text="Whack-a-mole", bg= "lightpink", command=open_moleGame, pady=8)
btn_moleGame.pack(pady=10)


#se actualice en tiempo real
label_money = tk.Label(root,text="Money: 0", pady=20)
label_money.pack()

previous_money = game_data.money

def money_update():
    global previous_money
    if previous_money != game_data.money:

        label_money.config(text=f"Money: {game_data.money}")
        previous_money = game_data.money

    root.after(300, money_update)

money_update()

#Store
store_frame = tk.Frame(root)
store_frame.pack(pady=10,padx=10)


store_items = [
    {"name": "Banana!", "image": ImageTk.PhotoImage(Image.open("storeimg/banana.jpg").resize((60, 60)))},
    {"name": "Quokka plushie", "image": ImageTk.PhotoImage(Image.open("storeimg/quokka.png").resize((60, 60)))},
    {"name": "Oia Uia cat", "image": ImageTk.PhotoImage(Image.open("storeimg/oia uia cat.png").resize((60, 60)))},
    {"name": "Funny coffee mug", "image": ImageTk.PhotoImage(Image.open("storeimg/coffe mug.png").resize((60, 60)))},
    {"name": "Pepto-Bismol", "image": ImageTk.PhotoImage(Image.open("storeimg/pepto.png").resize((60, 60)))},
    {"name": "1lb dumbbell", "image": ImageTk.PhotoImage(Image.open("storeimg/dumbbell.png").resize((60, 60)))},
    {"name": "A single Froot Loop", "image": ImageTk.PhotoImage(Image.open("storeimg/frootloop.png").resize((60, 60)))},
    {"name": "Infinite Enlightenment", "image": ImageTk.PhotoImage(Image.open("storeimg/enlightenment.png").resize((60, 60)))},
    {"name": "Extradimensional amulet", "image": ImageTk.PhotoImage(Image.open("storeimg/amulet.png").resize((60, 60)))}
]



def bought_item(img, text, price, button):
    def bought():

        if price <= game_data.money:


            if text.cget("text") == "???":
                

                pygame.mixer.music.load("cash.mp3")
                pygame.mixer.music.play()

                item = random.choice(store_items)
                img.config(image=item["image"])
                img.image = item["image"] #para que la referencia de imagen no se pierda
                text.config(text=item["name"])

                store_items.remove(item)        #excluir numero ya incluido

                game_data.money -= price
                #inhabilitar boton de compra al haberlo comprado
                button.config(state="disabled", bg="gray", text="Bought", fg="white")
        else: 
            messagebox.showinfo("","You don't have enough money!")

    return bought
    
    


for i in range(1,4):

    

    item_frame = tk.Frame(store_frame, padx= 10, pady=15)
    item_frame.grid(row=i,column=1)

    button_frame = tk.Frame(store_frame, padx= 10, pady=15)
    button_frame.grid(row=i,column=0)

    mystery_img = ImageTk.PhotoImage(Image.open("storeimg/mystery.png").resize((60, 60)))

    item_img = tk.Label(item_frame, image=mystery_img, width=50, height=50)
    item_img.image = mystery_img  # guardar referencia para que no se borre de memoria
    item_img.pack()

    item_name = tk.Label(item_frame,text="???")
    item_name.pack()

    price = i*i*100

    buy_button  = tk.Button(button_frame, text="Buy", bg= "green", fg= "white", pady=8, padx=15)
    buy_button.config(command=bought_item(item_img, item_name, price, buy_button))
    buy_button.pack()    

    buy_price = tk.Label(button_frame,text = f"Price: {price}")
    buy_price.pack()


root.mainloop()


#preguntar a chat q le puedo personalizar para q se vea mas bonito