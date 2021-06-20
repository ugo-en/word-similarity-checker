from gui import *


class MainFrame(MyFrame):
    def __init__(self,master):
        super().__init__(master)
        self.panel1 = MyPanel(self)
        self.panel2 = MyPanel(self,orient=tk.HORIZONTAL)
        self.panel3 = MyPanel(self,orient=tk.HORIZONTAL)

        self.label1 = MyLabel(self,"Word Similarity Checker",f_size=30)
        self.entry = MyEntry(self,text="Word you want to check")
        self.entry2 = MyEntry(self,text="Word to check with")
        self.go_btn = MyBtn(self,"Go")

        self.ans = MyLabel(self,"",f_size=20,fg="darkblue")
        self.binding()

        self.entry.focus_force()

    def binding(self):
        self.go_btn.bind('<Button-1>',self.respond)

    def show(self):
        self.pack(pady=150)

        self.panel1.pack()

        self.panel1.add(self.label1)
        self.panel1.add(self.panel2,pady=50)
        self.panel1.add(self.panel3,pady=50)
        self.panel2.add(self.entry)
        self.panel2.add(self.entry2)
        self.panel2.add(self.go_btn)
        self.panel3.add(self.ans)

    def respond(self,x):
        self.ans.configure(text=s.score(self.entry.get(),self.entry2.get()))
