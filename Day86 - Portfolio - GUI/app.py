import tkinter as tk
import random
import time
from PIL import Image, ImageTk


def display_image(url, width, height, transparent=False):
    img = Image.open(url)
    img = img.resize((width, height))
    if transparent:
        img = img.convert("RGBA")
        datas = img.getdata()
        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        img.putdata(newData)
    photo = ImageTk.PhotoImage(img)
    img_label = tk.Label(image=photo)
    img_label.image = photo  # Store a reference to prevent image from being garbage collected
    return img_label


class TypingTestTimeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Tester")
        self.root.geometry("400x700")

        self.high_score = 0
        self.current_score = 0

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

        # Load BG image
        self.bg = display_image("assets/bg.jpg", 400, 700)
        self.bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Place Logo
        self.logo = display_image("assets/logo.PNG", 400, 150)
        #self.create_image(350,200,image=self.logo)
        self.logo.grid(column=0, row=0, sticky=tk.N + tk.S)

        # Place PC Logo
        self.pc_logo = display_image("assets/PC.PNG", 400, 300, transparent=True)
        self.pc_logo.grid(column=0, row=1, sticky=tk.N + tk.S)

        # Instruction Label
        self.instruction_label = tk.Label(self.root, text="Type the Following Text as fast as you can:",
                                          fg="black",
                                          font=("Helvetica", 16, "bold"))
        self.instruction_label.grid(column=0, row=2, pady=(0, 10))

        # Test Sentence
        self.test_text_label = tk.Label(self.root, text=self.current_text, wraplength=300, fg="black",
                                        font=("Helvetica", 17))
        self.test_text_label.grid(column=0, row=3, pady=(0, 20))

        # Text Box
        self.text_input = tk.Text(self.root, height=5, width=50, bd=3, relief="solid", bg="white", fg="black")
        self.text_input.grid(column=0, row=4, pady=10)

        # Button
        self.start_btn = tk.Button(self.root, text="Start", command=self.start_typing_test, fg="black",
                                   font=("Helvetica", 15, "bold"))
        self.start_btn.grid(column=0, row=5)

        # Result Label
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(column=0, row=6)

        # Restart Button
        self.restart_btn = tk.Button(self.root, text="Restart", command=self.restart_typing_test)
        self.restart_btn.grid(column=0, row=7)
        self.restart_btn.grid_forget()  # Hide Restart Button

        # Highscore Label
        self.high_score_label = tk.Label(self.root, text=f'Highscore {self.high_score}', bg="white", fg="black")
        self.high_score_label.grid(column=0, row=8)

        # Recent Score Label
        self.recent_score_label = tk.Label(self.root, text="")
        self.recent_score_label.grid()

    def start_typing_test(self):
        self.start_btn.grid_forget()
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
            self.recent_score = words_per_minute

            if self.recent_score > self.high_score:
                self.high_score = self.recent_score

            self.result_label.config(text=f"Your Typing speed is {self.recent_score} words per minute.", fg="black")
            self.high_score_label.config(text=f'Highscore {self.high_score}')
            self.text_input.unbind("<KeyRelease>")
            self.restart_btn.grid()

    def restart_typing_test(self):
        self.current_text = random.choice(self.sample_text)
        self.total_words = len(self.current_text.split())
        self.test_text_label.config(text=self.current_text)
        self.text_input.delete("1.0", "end")
        self.result_label.config(text="")
        self.restart_btn.grid_forget()
        self.start_btn.grid()


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestTimeApp(root)
    root.mainloop()