import tkinter as tk
 
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
 
    # here is the main func to create the window with the messages 
    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Just testing the window\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                               command=self.master.destroy)
        self.quit.pack(side="bottom")
 
    def say_hi(self):
        print("I'm here in the bash my dude!")
 
root = tk.Tk()
app = Application(master=root)
app.mainloop() # drive it 
