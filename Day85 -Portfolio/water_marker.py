import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont


# Step 1: Create a function that browses and selects an image file using tkinter

# *tkinter.filedialog is a common dialog that allows the user to specify a file to open or save it

# ------------Save Image Dialog----------

def save_image(image):
    filename = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"),
                                                       ("All files", "*.*")])
    if filename:
        image.save(filename)


# ------------Add Watermark (Text)----------

def add_text_watermark(image, text, position, font_name="Arial", font_size=30, color=(0, 0, 0)):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_name, font_size)
    draw.text(position, text, fill=color, font=font)
    return image


# ------------Browse Image------------------

def browse_image():
    global watermarked_img
    options = {
        'filetypes': [("Image files", "*.jpeg;*.jpg;*.png;*.gif"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
    }
    file = filedialog.askopenfile(**options)
    if file:
        filename = file.name
        print("Selected File:", filename)

        # Load img using Pillow
        image = Image.open(filename)

        # Add text watermark
        watermark_text = input("Write down Your Watermark: ")
        watermarked_img = add_text_watermark(image, watermark_text, position=(10, 10))

        # Display the image in a Tkinter window

        # TKinter cannot directly display a Pillow image
        image_tk = ImageTk.PhotoImage(watermarked_img)

        # create img label
        image_label = tk.Label(window, image=image_tk)

        # prevent the img to become garbage collected by python memory management
        image_label.image = image_tk
        # Display img
        image_label.pack()
        file.close()  # Close the file after use


# ---------------Screen Setup---------------

# create main window
window = tk.Tk()
window.title("Water Marker")

# ---------------Button---------------------

# Create button to browse image
browse_button = tk.Button(window,
                          text="Browse Image",
                          command=browse_image)

save_button = tk.Button(window, text="Save Image", command=lambda: save_image(watermarked_img))
save_button.pack(pady=10)

# show button
browse_button.pack(pady=20)

# Start the Tkinter event loop
window.mainloop()
