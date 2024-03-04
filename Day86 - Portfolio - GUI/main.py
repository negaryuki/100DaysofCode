import tkinter as tk
import random
import time


class TypingTestTimeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("400x300")

        self.sample_text = [
            "The quick brown fox jumps over the lazy dog.",
            "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "Python is an interpreted, high-level and general-purpose programming language."
        ]

        self.current_text = random.choice(self.sample_text)
        self.time_start = 0
        self.time_end = 0
        self.total_words = len(self.current_text.split())

        # Instruction Label
        self.instruction_label = tk.Label(self.root, text="Type the Following Text as fast as you can:")
        self.instruction_label.pack()

        # Test Sentence
        self.test_text_label = tk.Label(self.root, text=self.current_text, wraplength=380)
        self.test_text_label.pack()

        # Text Box
        self.text_input = tk.Text(self.root, height=5, width=50)
        self.text_input.pack()

        # Button
        self.start_btn = tk.Button(self.root, text="Start", command=self.start_typing_test)
        self.start_btn.pack()

        # Result Label
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        # Restart Button
        self.restart_btn = tk.Button(self.root, text="Restart", command=self.restart_typing_test)
        self.restart_btn.pack()
        self.restart_btn.pack_forget()  # Hide Restart Button

    def start_typing_test(self):
        self.start_btn.pack_forget()
        self.time_start = time.time()  # Record current time

        # This line binds the <KeyRelease> event to the check_typing_speed method.
        # This means that every time a key is released (i.e., a key is typed) in the txt_input text widget,
        # the check_typing_speed method will be called to check the typing speed.
        self.text_input.bind("<KeyRelease>", self.check_typing_speed)

    def check_typing_speed(self, event):
        if self.text_input.get("1.0", "end-1c") == self.current_text:
            self.time_end = time.time()
            time_taken = self.time_end - self.time_start
            words_per_minute = int((self.total_words / time_taken) * 60)
            self.result_label.config(text=f"Your Typing speed is {words_per_minute} words per minute.")
            self.text_input.unbind("<KeyRelease>")
            self.restart_btn.pack()

    def restart_typing_test(self):
        self.current_text = random.choice(self.sample_text)
        self.total_words = len(self.current_text)
        self.test_text_label.config(text=self.current_text)
        self.text_input.delete("1.0", "end")
        self.result_label.config(text="")
        self.restart_btn.pack_forget()
        self.start_btn.pack()


if __name__ == "main":
    root = tk.Tk()
    app = TypingTestTimeApp(root)
    root.mainloop()
