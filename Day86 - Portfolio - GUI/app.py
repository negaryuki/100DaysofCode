from functions import *

#logo = display_image("assets/logo.jpeg",2,1)

root=tk.Tk()
img = Image.open("assets/logo(01).jpeg")
photo = ImageTk.PhotoImage(img)
img_label = tk.Label(root,image=photo)
img_label.img = img
img_label.pack()

root.mainloop()