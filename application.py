from tkinter import *
import tkinter
from file_organizer import organize

bg_color = '#84BF04'
black = '#171717'
white = '#ffffff'
default_font = 'Arial'

class Application:
    def __init__(self, master=None):

        self.default_font = (default_font, "12")

        self.first_container = Frame(master)
        self.first_container["pady"] = 10
        self.first_container.config(bg=bg_color)
        self.first_container.pack()

        self.second_container = Frame(master)
        self.second_container["padx"] = 20
        self.second_container.config(bg=bg_color)
        self.second_container.pack()

        self.third_container = Frame(master)
        self.third_container["padx"] = 20
        self.third_container.config(bg=bg_color)
        self.third_container.pack()

        self.fourth_container = Frame(master)
        self.fourth_container["pady"] = 20
        self.fourth_container.config(bg=bg_color)
        self.fourth_container.pack()

        self.title = Label(self.first_container, text="File Organizer")
        self.title["font"] = (default_font, "14", "bold")
        self.title.config(bg=bg_color)
        self.title.pack()

        self.lb_path = Label(self.second_container,text="Path ", font=self.default_font)
        self.lb_path["font"] = (default_font, "12")
        self.lb_path.config(bg=bg_color)
        self.lb_path.pack(side=LEFT)

        self.path = Entry(self.second_container, borderwidth=5, relief=tkinter.FLAT)
        self.path["width"] = 30
        self.path["font"] = self.default_font
        self.path.pack(side=LEFT)
        
        self.btn_organize = Button(self.fourth_container, command=lambda: organize(self))
        self.btn_organize["text"] = "Organize"
        self.btn_organize["font"] = (default_font, "10")
        self.btn_organize["width"] = 12
        self.btn_organize.configure(bg=black)
        self.btn_organize.configure(fg=white)
        self.btn_organize.pack()

        self.message = Label(self.fourth_container, text="", font=self.default_font)
        self.message.config(bg=bg_color)
        self.message.pack()

root = Tk()
root.title('File Organizer')
root.config(bg=bg_color)
root.eval('tk::PlaceWindow . center')
Application(root)
root.mainloop()