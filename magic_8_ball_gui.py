import random
import tkinter as tk

class Magic8Ball:
    def __init__(self):
        self.responses = [
            ("Yes, definitely!", "green"),
            ("It is certain.", "green"),
            ("Without a doubt.", "green"),
            ("Most likely.", "lightgreen"),
            ("Ask again later.", "orange"),
            ("Cannot predict now.", "orange"),
            ("Don't count on it.", "salmon"),
            ("My sources say no.", "red"),
            ("Outlook not so good.", "red"),
            ("Very doubtful.", "red")
        ]

        # Create the main window
        self.window = tk.Tk()
        self.window.title("Magic 8-Ball")
        self.window.geometry("400x500")
        self.window.configure(bg="#1a1a2e")

        # Title
        title = tk.Label(
            self.window,
            text="Magic 8-Ball",
            font=("Arial", 28, "bold"),
            fg="#eee",
            bg="#1a1a2e"
        )
        title.pack(pady=20)

        # The 8-ball circle
        self.canvas = tk.Canvas(
            self.window,
            width=250,
            height=250,
            bg="#1a1a2e",
            highlightthickness=0
        )
        self.canvas.pack(pady=10)

        # Draw the ball
        self.canvas.create_oval(10, 10, 240, 240, fill="#0f0f23", outline="#333", width=3)
        self.canvas.create_oval(60, 60, 190, 190, fill="#16213e", outline="#444", width=2)

        # Answer text on the ball
        self.answer_text = self.canvas.create_text(
            125, 125,
            text="8",
            font=("Arial", 36, "bold"),
            fill="#4a90d9",
            width=120
        )

        # Question entry
        tk.Label(
            self.window,
            text="Ask a yes/no question:",
            font=("Arial", 12),
            fg="#aaa",
            bg="#1a1a2e"
        ).pack(pady=(20, 5))

        self.question_entry = tk.Entry(
            self.window,
            font=("Arial", 14),
            width=30,
            bg="#16213e",
            fg="white",
            insertbackground="white"
        )
        self.question_entry.pack(pady=5)

        # Shake button
        self.button = tk.Button(
            self.window,
            text="Shake the Ball!",
            font=("Arial", 14, "bold"),
            bg="#4a90d9",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.shake
        )
        self.button.pack(pady=20)

        # Bind Enter key
        self.question_entry.bind("<Return>", lambda e: self.shake())

    def shake(self):
        question = self.question_entry.get().strip()
        if not question:
            self.canvas.itemconfig(self.answer_text, text="Ask\nsomething!", fill="orange", font=("Arial", 18, "bold"))
            return

        # Get random response
        response, color = random.choice(self.responses)

        # Update the ball
        self.canvas.itemconfig(self.answer_text, text=response, fill=color, font=("Arial", 14, "bold"))

        # Clear the entry
        self.question_entry.delete(0, tk.END)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = Magic8Ball()
    app.run()
