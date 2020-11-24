#!/usr/bin/env python3  

import os 
import sys
import random
import string
import shutil, errno
import tkinter as tk
import PySimpleGUI as sg 

class Converttxt(object):
    
    def process(chars = string.ascii_uppercase + string.digits + string.punctuation):

        # window color theme
        sg.theme('Dark Teal 1')

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
        
        layout2 = [ [sg.Text('Put here the cryptography text to get the original back: ')],
                    [sg.Text('Enter here:'), sg.InputText(key = '-OUTPUT-')],
                    [sg.OK()]
                  ]
        window2 = sg.Window('Cr+', layout2, size=(450,250))
        event2, values2 = window2.read()
        text_output = values2['-OUTPUT-']
        if text_output == transformation:
            sg.popup('the original:', text_input)
        else:
            sg.popup('error')
    process()

if __name__ == '__main__':
    Converttxt()



