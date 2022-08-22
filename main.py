from tkinter import *

class Application:
    def __init__(self, master=None):
        self.default_font = ("Arial", "10")
        self.first_container = Frame(master)
        self.first_container["pady"] = 10
        self.first_container.pack()

        self.second_container = Frame(master)
        self.second_container["padx"] = 20
        self.second_container.pack()

        self.third_container = Frame(master)
        self.third_container["padx"] = 20
        self.third_container.pack()

        self.fourth_container = Frame(master)
        self.fourth_container["pady"] = 20
        self.fourth_container.pack()

        self.title = Label(self.first_container, text="File Organizer")
        self.title["font"] = ("Arial", "10", "bold")
        self.title.pack()

        self.lb_path = Label(self.second_container,text="Path ", font=self.default_font)
        self.lb_path.pack(side=LEFT)

        self.lb_path = Entry(self.second_container)
        self.lb_path["width"] = 30
        self.lb_path["font"] = self.default_font
        self.lb_path.pack(side=LEFT)

        self.btn_organize = Button(self.fourth_container)
        self.btn_organize["text"] = "Organize"
        self.btn_organize["font"] = ("Calibri", "8")
        self.btn_organize["width"] = 12
        self.btn_organize.pack()

        self.mensagem = Label(self.fourth_container, text="", font=self.default_font)
        self.mensagem.pack()


root = Tk()
Application(root)
root.mainloop()