#!/usr/bin/python3 

from tkinter import *
import os
import random
import string 
import sys
import numpy as np 

class Convert(object):
    
    frame = np.array([-500,-500])
    root = Tk()
    root.geometry(frame)
    root.title("Cryptography")

    def take_input(chars = string.ascii_uppercase + string.digts + string.punctuation):
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


if __name__ == '__main__':
    Convert()
