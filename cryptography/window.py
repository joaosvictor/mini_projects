#!/usr/bin/env python3  

import os 
import sys
import time
import random
import string
import shutil, errno
import tkinter as tk
import PySimpleGUI as sg 

class Converttxt(object):
    
    def process(chars = string.ascii_uppercase + string.digits + string.punctuation):

        # window color theme
        sg.theme('Tan')

        # inside your window 
        layout = [ [sg.Text('Cryptography your text now! Cr+ it.')],
                   [sg.Text('Please, enter your text: '), sg.InputText(key = '-INPUT-')],
                   [sg.OK(), sg.Cancel()],
                   ]
 
        # create window
        window = sg.Window('Cr+', layout, size=(450,250) )
        event, values = window.read() 

        window.close()
                                         
        # get input key from layout
        text_input = values['-INPUT-']
                                
        # here the magic happens
        transformation = len(text_input)
        if transformation <= 35:
            transformation = ''.join(random.choice(chars) for i in range(len(text_input)*10))
        else: 
            transformation = ''.join(random.choice(chars) for i in range(len(text_input)))
        
        
        sg.popup('Your cryptography text: ', transformation)
        print(transformation)
        
        # create window that offer the original text back
        layout2 = [ [sg.Text('Put here your cryptography text to get the original back: ')],
                    [sg.Text('Enter here: '), sg.InputText(key = '-INPUT2-')],
                    [sg.OK()]
                  ]

        window2 = sg.Window('Cr+', layout2, size=(450,250))
        event2, values2 = window2.read()

        text_input2 = values2['-INPUT2-']

        if text_input2 == transformation:
            sg.popup('Your original text:', text_input)
        else:
            sg.popup('Error')
        
        # time execution
        start_time = time.time()
        print("-> %s seconds " % (time.time()- start_time)) 

    process()

if __name__ == '__main__':
    Converttxt()

