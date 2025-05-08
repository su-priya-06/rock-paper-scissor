import tkinter as tk
import random

# Main window
root = tk.Tk()
root.title("Rock ✊ Paper 🖐 Scissors ✌️")
root.geometry("400x450")
root.configure(bg="#f0f0f0")

choices = ["rock", "paper", "scissors"]
emoji_map = {
    "rock": "✊",
    "paper": "🖐",
    "scissors": "✌️"
}

user_score = 0
computer_score = 0

# Functions
def play(user_choice):
    global user_score, computer_score

    comp_choice = random.choice(choices)
    result = ""

    if user_choice == comp_choice:
        result = "It's a tie! 🤝"
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "scissors" and comp_choice == "paper") or \
         (user_choice == "paper" and comp_choice == "rock"):
        user_score += 1
        result = "You win this round! 🎉"
    else:
        computer_score += 1
        result = "Computer wins this round! 💻"

    update_display(user_choice, comp_choice, result)

def update_display(user_choice, comp_choice, result):
    user_label.config(text=f"You: {emoji_map[user_choice]} ({user_choice})")
    comp_label.config(text=f"Computer: {emoji_map[comp_choice]} ({comp_choice})")
    result_label.config(text=result)
    score_label.config(text=f"Score — You: {user_score}  Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_label.config(text="You: ")
    comp_label.config(text="Computer: ")
    result_label.config(text="")
    score_label.config(text="Score — You: 0  Computer: 0")

# Widgets
title = tk.Label(root, text="Rock ✊ Paper 🖐 Scissors ✌️", font=("Arial", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

user_label = tk.Label(root, text="You: ", font=("Arial", 14), bg="#f0f0f0")
user_label.pack()

comp_label = tk.Label(root, text="Computer: ", font=("Arial", 14), bg="#f0f0f0")
comp_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score — You: 0  Computer: 0", font=("Arial", 14), bg="#f0f0f0")
score_label.pack(pady=5)

btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=20)

rock_btn = tk.Button(btn_frame, text="✊ Rock", font=("Arial", 12), width=10, command=lambda: play("rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(btn_frame, text="🖐 Paper", font=("Arial", 12), width=10, command=lambda: play("paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(btn_frame, text="✌️ Scissors", font=("Arial", 12), width=10, command=lambda: play("scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

reset_btn = tk.Button(root, text="🔁 Reset", font=("Arial", 12), command=reset_game, bg="lightgray")
reset_btn.pack(pady=10)

# Start the GUI loop
root.mainloop()
