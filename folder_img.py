from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Gallery')
my_img = ImageTk.PhotoImage(Image.open('img/eda.jpg'))
# my_img1 = ImageTk.PhotoImage(Image.open('img/1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('img/2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('img/3.jpg'))
img_list = [my_img, my_img3, my_img2]

my_label = Label(image=my_img)


def forward(img_number):
    global my_label  # global is useful for getting values outside the func
    global button_forward
    global button_back
    
    my_label.grid_forget()  # first thing is don't overlap but delete the
    # previous one
    
    my_label = Label(image=img_list[img_number - 1])  # now create what is
    # Update
    button_forward = Button(root, text='>>', command=lambda: forward(
        img_number + 1))
    button_back = Button(root, text='<<', command=lambda: back(img_number - 1))
    if img_number == len(img_list):
        # disable the button >> for the last photo
        button_forward = Button(root, text='>>', state=DISABLED)
    # going to display on screen
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    

def back(img_num):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=img_list[img_num])
    button_forward = Button(root, text='>>', command=lambda: forward(img_num
                                                                     + 1))
    button_back = Button(root, text='<<', command=lambda: back(img_num - 1))
    if img_num == 0:
        button_back = Button(root, text='<<', state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)


# Buttons
button_forward = Button(root, text='>>', command=lambda: forward(2))
# use of lambda to pass through a list
button_exit = Button(root, text='Exit', command=root.quit)
button_back = Button(root, text='<<', command=back, state=DISABLED)


# Put things on screen
my_label.grid(row=0, column=0, columnspan=3)
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
