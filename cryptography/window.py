#!/usr/bin/env python3  

import os 
import sys
import random
import string
import shutil, errno
import tkinter as tk
import PySimpleGUI as sg 

class Converttxt(object):
    '''
    src = ""
    dest = ""
    def copy(src, dest):
        try:
            shutil.copytree(src, dest)
        except OSError as e:
            if e.errno == errno.ENOTDIR:
                shutil.copy(src, dest)
            else:
                print('Directory not copied. Error:  %s' % e)
    '''
    def process(chars = string.ascii_uppercase + string.digits + string.punctuation):

        # window color theme
        sg.theme('Dark Teal 1')

        # inside your window 
        layout = [ [sg.Text('Cryptography your text now! Cr+ it.')],
                   [sg.Text('Please, enter your text: '), sg.InputText(key = '-INPUT-')],
                   [sg.OK(), sg.Cancel()],
                   [sg.Button("Copy")]
                   ]
 
        '''
        convert_num_str = f'{layout}'
        transformation = ''.join(random.choice(chars) for i in range(len(convert_num_str) * 10))
        '''

        # create window
        window = sg.Window('Cr+', layout, size=(450,250) )
        '''
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancel'):
                break
            print('Your crypto text:',values[0])
            if event  == 'Copy':
                copy(values[0], values[1])
        '''    
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
        
    process()

if __name__ == '__main__':
    Converttxt()



