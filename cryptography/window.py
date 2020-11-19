#!/usr/bin/env python3  

import os 
import sys
import random
import string
import PySimpleGUI as sg 

class Converttxt(object):
    def process(chars = string.ascii_uppercase + string.digits + string.punctuation):

        # window color theme
        sg.theme('Dark Teal 5')

        # inside your window 
        layout = [ [sg.Text('Cryptography your text now! Cr+.')],
                   [sg.Text('Please, enter your text: '), sg.InputText(key = '-IN-')],
                   [sg.Submit(), sg.Cancel()]
                   ]
 
        '''
        convert_num_str = f'{layout}'
        transformation = ''.join(random.choice(chars) for i in range(len(convert_num_str) * 10))
        '''

        # create window
        window = sg.Window('Cr+', layout)

        event, values = window.read()
        window.close()

        # get input key from layout
        text_input = values['-IN-']
        
        # here
        transformation = ''.join(random.choice(chars) for i in range(len(text_input)*10))
        sg.popup('Your cryptography text: ', transformation)

    process()

if __name__ == '__main__':
    Converttxt()



