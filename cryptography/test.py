#!/usr/bin/python3 

from tkinter import *
import tkinter as tk
import os
import numpy as np
import random
import string 
import sys

class Convert(object):

    root = tk.Tk()
    root.geometry("700x550")
    root.title("Cryptography")

    def take_input(chars = string.ascii_uppercase + string.digits + string.punctuation):
        INPUT = inputtxt.get("1.0", "end-1c")
        convert_num_str = f'{INPUT}'
        sys.stdout.write("\033[F")
        """
        // sys stdout

        #include <iostream>
        using namespace std;
        
        int main() {
           int txt;
           cout << "Please, enter a text: ";
           cin >> txt;
           cout << "The text you entered is: " << txt;
           return 0;
        }
        """

        # txt -> cryptography
        transformation  = ''.join(random.choice(chars) for i in range(len(INPUT)*10))
        print(transformation)

    # TODO: take the initial input and print it in an new label with the transformation

    # txt window 1
    l = Label(text = "Please, put your text to cryptography below.")
    inputtxt = Text(root, height = 10,
                    width = 30,
                    bg = "light blue")
    print(' ')

    # button
    display = Button(root, height = 2,
                     width = 15,
                     text = "Show",
                     command = lambda:take_input())

    # txt window 2
    Label_middle = tk.Label(root,
                            text = "This is your cryptography text.")
    Label_middle.place(relx = 0.5,
                            rely = 0.5,
                            anchor = 'center')
    output = Text(root, height = 10,
                  width = 30,
                  bg = "light yellow")

    #l1.pack()
    l.pack()
    inputtxt.pack()    
    display.pack()    
    output.pack()
    mainloop()
   
    take_input()

if __name__ == '__main__':
    Convert()
