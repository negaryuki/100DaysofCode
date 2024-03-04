import tkinter as tk
import random
import time

class TypingTestTimeApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("400x300")

        self.sample_text =[
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
        self.restart_btn.pack_forget()   # Hide Restart Button

