#!/usr/bin/python3 

from tkinter import *
import os
import random
import string 
import sys

class Convert(object):
    
    root = Tk()
    root.geometry("500x500")
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
        # part to transform it 
        transformation  = ''.join(random.choice(chars) for i in range(len(INPUT)*10))
        print(transformation)
    l.pack()
    inputtxt.pack()    
    Display.pack()    
    mainloop()
    take_input()

if __name__ == '__main__':
    Convert()
