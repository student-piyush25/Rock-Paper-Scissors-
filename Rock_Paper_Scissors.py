import tkinter as tk
import random
import winsound  # For sound effects (Windows only)

# Choices & Emoji Mapping
choices = ["Rock", "Paper", "Scissors"]
emoji_map = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}

# Score Variables
user_score = 0
computer_score = 0

# Function to Play
def play(choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)

    # Display Choices
    user_label.config(text=f"🧑 You: {emoji_map[choice]}")
    computer_label.config(text=f"🤖 Computer: {emoji_map[computer_choice]}")

    # Determine Winner
    if choice == computer_choice:
        result_label.config(text="🤝 It's a Tie!", fg="blue")
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        user_score += 1
        result_label.config(text="🎉 You Win!", fg="green")
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)  # Win Sound
    else:
        computer_score += 1
        result_label.config(text="😢 Computer Wins!", fg="red")
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)  # Lose Sound

    # Update Scoreboard
    score_label.config(text=f"🏆 Score - You: {user_score} | Computer: {computer_score}")

# GUI Window
root = tk.Tk()
root.title("Rock Paper Scissors Ultimate")
root.geometry("400x500")

# Labels
tk.Label(root, text="Rock, Paper, Scissors!", font=("Arial", 18, "bold")).pack(pady=10)
user_label = tk.Label(root, text="🧑 You: ", font=("Arial", 14))
user_label.pack()
computer_label = tk.Label(root, text="🤖 Computer: ", font=("Arial", 14))
computer_label.pack()
result_label = tk.Label(root, text="", font=("Arial", 16, "bold"))
result_label.pack(pady=10)
score_label = tk.Label(root, text="🏆 Score - You: 0 | Computer: 0", font=("Arial", 14, "bold"))
score_label.pack(pady=10)

# Buttons
for choice in choices:
    tk.Button(root, text=choice, font=("Arial", 14), command=lambda c=choice: play(c)).pack(pady=5)

# Run App
root.mainloop()
