from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title('Learn to code')
# root.iconbitmap('folder name')  # display the little icon up left on the
# screen
my_img = ImageTk.PhotoImage(Image.open('img/eda.jpg'))
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(root, text='Exit', command=root.quit)
button_quit.pack()

root.mainloop()
