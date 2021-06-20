import tkinter as tk, time


class MyLabel(tk.Label):
    def __init__(self, master, text="My Label", fg="royalblue",pady=10,padx=3,font="Gabriola",f_size=20,f_style="bold"):
        super().__init__(master=master)
        bg = self.master['bg']

        self.configure(text=text, fg=fg, bg=bg,padx=padx,pady=pady,font=(font,f_size,f_style))


class MyEntry(tk.Entry):
    def __init__(self, master, text="",type_x="", fg="royalblue", width=35, font="Gabriola",f_size=15,f_style="bold",borderwidth=1):
        super().__init__(master=master)
        self.bg = self.master['bg']
        self.text = text
        self.type_x = type_x

        self.configure(fg=fg, bg=self.bg,show=type_x, width=width,font=(font,f_size,f_style),borderwidth=borderwidth)

        self.bind("<Button-1>",self.hide_placeholder)
        self.bind("<FocusOut>",self.show_placeholder)

    def hide_placeholder(self,x=0):
        if self.get() == self.text:
            self.delete(0,len(self.text))
        if self.type_x != "":
            self.configure(show=self.type_x)

    def show_placeholder(self,x=0):
        if self.get() == "":
            self.insert(0,self.text)
        if self.type_x != "":
            self.configure(show="")


class MyCheckBox(tk.Checkbutton):
    def __init__(self, master, bg="", fg="royalblue", relief=tk.FLAT):
        super().__init__(master=master)
        if bg == "": bg = master["bg"]
        self.configure(fg=fg, bg=bg, relief=relief)


class MyBtn(tk.Button):
    def __init__(self, master, text="My Button",bg="lime", fg="royalblue", width=5, relief=tk.FLAT):
        super().__init__(master=master)

        self.configure(fg=fg, bg=bg, text=text, width=width,relief=relief)


class MyTk(tk.Tk):
    def __init__(self,bg="white"):
        super().__init__()
        self.minsize(1336,720)
        self.maxsize(1336,720)
        self.title("Ugo's Word Similarity Checker")
        self.resizable(False, False)
        self.configure(bg=bg)


class MyPanel(tk.PanedWindow):
    def __init__(self,master, bg="white", orient=tk.VERTICAL):
        super().__init__(master=master)
        self.configure(bg=bg,orient=orient)


class MyFrame(tk.Frame):
    def __init__(self,master, bg="white",relief=tk.SOLID):
        super().__init__(master=master)
        self.configure(bg=bg,relief=relief)
