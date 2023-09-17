import customtkinter
import random



def Rock():
    user = "Камень"
    computer = random.choice(["Камень", "Бумага", "Ножницы"])
    labelText.configure(text=f"{computer}",text_color='orange')
    if user == computer:
        info_label.configure(text="Ничья! ", text_color='orange')
    elif computer == "Бумага":
        info_label.configure(text="PC выйграл! ", text_color='orange')
    else:
        info_label.configure(text="Ты выйграл! ", text_color='orange')


def Ciseaux():
    user = "Ножницы"
    computer = random.choice(["Камень", "Бумага", "Ножницы"])
    labelText.configure(text=f"{computer}",text_color='orange')
    if user == computer:
        info_label.configure(text="Ничья! ", text_color='orange')
    elif computer == "Камень":
        info_label.configure(text="PC выйграл!", text_color='orange')
    else:
        info_label.configure(text="Ты выйграл! ", text_color='orange')


def Paper():
    user = "Бумага"
    computer = random.choice(["Камень", "Бумага", "Ножницы"])
    labelText.configure(text=f"{computer}",text_color='orange')
    if user == computer:
        info_label.configure(text="Ничья! ", text_color='orange')
    elif computer == "Ножницы":
        info_label.configure(text="PC выйграл! ", text_color='orange')
    else:
        info_label.configure(text="Ты выйграл!", text_color='orange')


window = customtkinter.CTk()
window.geometry('800x600')
window.title("Камень ножницы бумага")
window.resizable(width=False, height=False)
h1_text = customtkinter.CTkLabel(window, text='Ход PC:', font=('', 50))
h1_text.place(y=50, x=30)
labelText = customtkinter.CTkLabel(window, text='', font=('', 90))
labelText.place(y=50, x=300)
info_label = customtkinter.CTkLabel(window, text='', font=('', 110))
info_label.place(y=220, x=50)
player_text = customtkinter.CTkLabel(window, text='Ваш ход:', font=('', 60))
player_text.place(y=400, x=30)
btn_stone = customtkinter.CTkButton(window, text="Камень", font=('', 30), width=150, height=70, command=Rock)
btn_stone.place(y=500, x=30)
btn_scissors = customtkinter.CTkButton(window, text="Ножницы", font=('', 30), width=170, height=70, command=Ciseaux)
btn_scissors.place(y=500, x=330)
btn_paper = customtkinter.CTkButton(window, text="Бумага ", font=('', 30), width=150, height=70, command=Paper)
btn_paper.place(y=500, x=600)

window.mainloop()
