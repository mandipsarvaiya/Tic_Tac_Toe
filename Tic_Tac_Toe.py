import tkinter as tk
from tkinter import messagebox

def check_winner():
  for i in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
    if buttons[i[0]]['text'] == buttons[i[1]]['text'] == buttons[i[2]]['text'] != "":
      buttons[i[0]].config(bg='lightgreen')
      buttons[i[1]].config(bg='lightgreen')
      buttons[i[2]].config(bg='lightgreen')

      messagebox.showinfo("Game Over", f"{buttons[i[0]]['text']} wins!")
      root.quit()

def on_click(index):
  if buttons[index]["text"] == "" and not winner:
    buttons[index]["text"] = current_player
    check_winner()
    toggle_player()

def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"  
    lable.config(text=f"{current_player}'s Turn")
  
root = tk.Tk()
root.title("Tic Tac Toe")


buttons = [tk.Button(root, text="", font=('Arial', 20), width=5, height=2, command=lambda i=i: on_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)

current_player = "X"
winner = False
lable = tk.Label(root, text=f"{current_player}'s Turn", font=('Arial', 14))
lable.grid(row=3, column=0, columnspan=3)


root.mainloop()
