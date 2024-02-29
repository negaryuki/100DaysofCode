import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk , ImageDraw, ImageFont


# Step 1: Create a function that browses and selects an image file using tkinter

# *tkinter.filedialog is a common dialog that allows the user to specify a file to open or save it

#------------Save Image Dialog----------

def save_image(image):
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
    if filename:
        image.save(filename)

#------------Add Watermark (Text)----------

def add_text_watermark(image, text, position, font_path="arial.ttf",font_size =30, color=(255,255,255)):
  
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)
    draw.text(position, text, fill=color, font=font)
    
    return image     
  
#------------Browse Image------------------
    
def browse_image():
  filename= filedialog.askopenfile(filetypes=["Image files","*.jpeg;*.jpg;*.png;*.gif"])
  if filename:
     print("Selected File:", filename)
     
     # Load img using Pillow
     image = Image.open(filename)
     
     # Add text watermark
     watermark_text = input("Write down Your Watermark")
     watermarked_img = add_text_watermark(image, watermark_text, position=(10,10))
     
     # Display the image in a Tkinter window
     
     # TKinter cannot directly display a Pillow image 
     image_tk = ImageTk.PhotoImage(watermarked_img)
     
     # create img label
     image_label = tk.Label(window, image= image_tk)
     
     # prevent the img to beccome garbage collected by python memory managment 
     image_label.image = image_tk
     # Display img
     image_label.pack()

     
#---------------Screen Setup---------------

# create main window
window = tk.Tk()
window.title("Water Marker")

#---------------Button---------------------

# Create button to browse image
browse_button= tk.Button(window, 
text="Browse Image",
command= browse_image)


save_button = tk.Button(window, text="Save Image", command=lambda: save_image(watermarked_img))
save_button.pack(pady=10) 

# show button
browse_button.pack(pady=20)


