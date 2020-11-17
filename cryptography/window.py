#!/usr/bin/python3 

from tkinter import *
import os
import numpy as np
import random
import string 
import sys

class Convert(object):
    frame = np.array([500,500])
    root = Tk()
    root.geometry(frame)
   #root.geometry("500x500")
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
    l = Label(text = "Please, put your text to cryptography below.")
    inputtxt = Text(root, height = 10,
                    width = 25,
                    bg = "light blue")

    Output = Text(root, height = 5,
                  width = 25,
                  bg = "light cyan")
         
    Display = Button(root, height = 2,
                     width = 20,
                     text = "Show",
                     command = lambda:take_input())

    l.pack()
    inputtxt.pack()    
    Display.pack()    
    Output.pack()
    mainloop()
   
    take_input()

if __name__ == '__main__':
    Convert()
