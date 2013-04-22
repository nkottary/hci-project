from Tkinter import * 
from pytesser import *
import os
import tkFileDialog
import tkMessageBox
from tkMessageBox import *

BACKGROUND_COLOR = "#335566"
ACTIVE_BACKGROUND = "#556677"
root = Tk()
SCREEN_WIDTH, SCREEN_HEIGHT = root.winfo_screenwidth(), root.winfo_screenheight()-60
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (SCREEN_WIDTH, SCREEN_HEIGHT))

root.current_image_file_name = None
root.output_text = None
root.saved = False

'''
    if output_text is generated write 
''' 
def save_file():
    if root.output_text:
        file_name = tkFileDialog.asksaveasfilename(defaultextension = ".txt",
                                     filetypes = [('TXT','*.txt')],
                                     title = "save text file")
        if file_name:
            f = open(file_name,"w")
            f.write(root.output_text)
            f.close()
            root.saved = True
    else:
        tkMessageBox.showerror("Error","You have not converted any file! , nothing to save.")

#root of the window 
root.title("Convertor")
root.configure(bg = BACKGROUND_COLOR)
root.tk_strictMotif(False)

photox = PhotoImage(file="icons/logo.gif")
w1x = Label(root, image=photox,borderwidth = 0, bg = BACKGROUND_COLOR)
w1x.photo = photox
w1x.pack()
w1x.place(x = 10,y = 10)

leftframe = Frame(root, bg = BACKGROUND_COLOR)
leftframe.pack()
rightframe = Frame(root, bg = BACKGROUND_COLOR)
rightframe.pack()
leftframe.place(x = 10,y = 160)
rightframe.place(x = 600,y = 160)

v1 = StringVar()
v1.set("Input Image: None")
w = Label(leftframe, textvariable = v1, justify = CENTER,font = ("helvetica",16),fg = "green", bg = BACKGROUND_COLOR)
w.pack(side = TOP)

canvas = Canvas(leftframe, width="5i", height="5i",background="white",scrollregion=(0, 0, "10i", "10i"))                                
canvas.scrollX = Scrollbar(leftframe, orient=HORIZONTAL)
canvas.scrollY = Scrollbar(leftframe, orient=VERTICAL)

# now tie the three together. This is standard boilerplate text
canvas['xscrollcommand'] = canvas.scrollX.set
canvas['yscrollcommand'] = canvas.scrollY.set
canvas.scrollX['command'] = canvas.xview
canvas.scrollY['command'] = canvas.yview

# pack 'em up
canvas.scrollX.pack(side=BOTTOM, fill=X)
canvas.scrollY.pack(side=RIGHT, fill=Y)
canvas.pack(expand = YES, fill = BOTH,side = LEFT)

#gif1 = PhotoImage(file = current_image_file_name)
#canvas.create_image(50,10,image = gif1, anchor = NW)

def open_file():
    file_name = tkFileDialog.askopenfilename(defaultextension = ".jpg",
                                 filetypes = [('GIF','*.gif')],
                                 title = "open image")
    if file_name:
        root.current_image_file_name = file_name
        v1.set("Input Image: "+str(root.current_image_file_name))
        canvas.delete(ALL)
        gif1 = PhotoImage(file = root.current_image_file_name)
        w = gif1.width()
        h = gif1.height()
        canvas.create_image(w/2, h/2, image = gif1)
        canvas.z = gif1
   
def quit_app():
    
    if root.output_text and not root.saved:
        reply = tkMessageBox.askquestion("File not saved","You have not saved the file, do you want to save it now?", type = YESNOCANCEL)
        if reply == "yes":
            save_file()
        elif reply == "no":
            root.quit()
    else:
        root.quit()
# create a toplevel menu
menubar = Menu(root)
menubar.add_command(label="Open", command=open_file)
menubar.add_command(label="Save", command=save_file)
menubar.add_command(label="Close", command=quit_app)

# display the menu
root.config(menu=menubar)

w2 = Label(rightframe, text = "Output Text", justify = CENTER,font = ("helvetica",16),fg = "green", bg = BACKGROUND_COLOR)
w2.pack()
text = Text(rightframe,wrap = NONE)

text.scrollX = Scrollbar(rightframe, orient=HORIZONTAL)
text.scrollY = Scrollbar(rightframe, orient=VERTICAL)

# now tie the three together. This is standard boilerplate text
text['xscrollcommand'] = text.scrollX.set
text['yscrollcommand'] = text.scrollY.set
text.scrollX['command'] = text.xview
text.scrollY['command'] = text.yview

# pack 'em up
text.scrollX.pack(side=BOTTOM, fill=X)
text.scrollY.pack(side=RIGHT, fill=Y)
text.pack(expand = YES, fill = BOTH,side = LEFT)

#Label(rightframe, textvariable=v, bg = "white",justify = LEFT,font = ("Rockwell",10)).pack(side = LEFT)

var = IntVar()
check = Checkbutton(root, text = "Append to existing text", variable = var,bg = BACKGROUND_COLOR,fg = "green",activebackground = ACTIVE_BACKGROUND)
check.var = var
check.pack()
check.place(x = 600,y = 600) 

def Button1():     
    if not root.current_image_file_name:
        tkMessageBox.showerror("Error","Please open an image file")
    else:
        im = Image.open(root.current_image_file_name)
        print check.var
        root.output_text = image_to_string(im)
        text.delete(1.0, END)
        text.insert(INSERT, root.output_text)
        root.saved = False

f = Frame(root, height=100, width=100)
f.pack_propagate(0) # don't shrink
f.pack()

photo = PhotoImage(file="icons/convert_img2.gif")
button1 = Button(f, image = photo, command = Button1,borderwidth = 0,bg = BACKGROUND_COLOR,activebackground = ACTIVE_BACKGROUND)  
button1.photo = photo
button1.pack(fill=BOTH, expand=1)
f.place(x = SCREEN_WIDTH-475, y = 10)

f1 = Frame(root, height=100, width=100)
f1.pack_propagate(0) # don't shrink
f1.pack()

photo = PhotoImage(file="icons/exit_img.gif")
button2 = Button(f1, image = photo, command = quit_app,borderwidth = 0,bg = BACKGROUND_COLOR,activebackground = ACTIVE_BACKGROUND)  
button2.photo = photo
button2.pack(fill=BOTH, expand=1)
f1.place(x = SCREEN_WIDTH-100, y = 10)

f2 = Frame(root, height=100, width=100)
f2.pack_propagate(0) # don't shrink
f2.pack()

photo = PhotoImage(file="icons/save_img.gif")
button3 = Button(f2, image = photo, command = save_file,borderwidth = 0,bg = BACKGROUND_COLOR,activebackground = ACTIVE_BACKGROUND)  
button3.photo = photo
button3.pack(fill=BOTH, expand=1)
f2.place(x = SCREEN_WIDTH-225, y = 10)

f3 = Frame(root, height=100, width=100)
f3.pack_propagate(0) # don't shrink
f3.pack()

photo = PhotoImage(file="icons/open_img.gif")
button4 = Button(f3, image = photo, command = open_file,borderwidth = 0,bg = BACKGROUND_COLOR,activebackground = ACTIVE_BACKGROUND)  
button4.photo = photo
button4.pack(fill=BOTH, expand=1)
f3.place(x = SCREEN_WIDTH-350, y = 10)

#Label(root, text = "Output text", bg = "white",justify = LEFT).pack(anchor = S)

root.mainloop()