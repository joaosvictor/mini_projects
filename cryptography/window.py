#!/usr/bin/env python3  

import PySimpleGUI as sg
import os
import sys
import random

class Converttxt(object):
    def process():

        sg.theme('DarkAmber')

        # inside your window 
        layout = [ [sg.Text('Cryptography your text now! Cr+.')],
                   [sg.Text('Please, enter your text: '), sg.InputText()],
                   [sg.Button('Convert'), sg.Button('Cancel')]]

        # create window
        window = sg.Window('Cr+', layout)

        # event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
            print('You entered ', values[0])

        window.close()
        process()

if __name__ == '__main__':
    Converttxt()



