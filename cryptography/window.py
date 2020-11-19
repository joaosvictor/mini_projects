#!/usr/bin/env python3  

import os 
import sys
import random
import string
import PySimpleGUI as sg 

class Converttxt(object):
    def process(chars = string.ascii_uppercase + string.digits + string.punctuation):

        # window color theme
        sg.theme('Black')


        # inside your window 
        layout = [ [sg.Text('Cryptography your text now! Cr+.')],
                   [sg.Text('Please, enter your text: '), sg.InputText(key = '-IN-')],
                   [sg.Submit(), sg.Cancel()]]
 
        '''
        convert_num_str = f'{layout}'
        transformation = ''.join(random.choice(chars) for i in range(len(convert_num_str) * 10))
        '''

        # create window
        window = sg.Window('Cr+', layout)

        # event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
            print('Your cryptography text:  ', values[0])

        window.close()
    process()

if __name__ == '__main__':
    Converttxt()



