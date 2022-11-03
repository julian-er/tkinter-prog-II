# import tkinter for all exercises
# All the exercises  will be documented using python self document
from tkinter import *
from tkinter import ttk

# Create tkinter basics class


class tkinter_basics:
    '''
        Define Tkinter class with basics windows and configurations
        Parameter:
        title (str) : title of window -> has default if value not provided
        iconUrl (str) : route of window icon -> has default if value not provided
        cols (int) : number of columns on your window
        rows (int) : number of rows on your window
        Return tk basics class , to execute window do your_variable.execute_window()
    '''

    def __init__(self, title='Inmobiliaria Software', iconUrl='./assets/icon_inmo.ico', cols=5, rows=5):

        # define variables
        self.title = title
        self.iconUrl = iconUrl
        self.col = cols
        self.row = rows
        self.root = Tk()

        self.root.minsize(width=500, height=200)
        self.root.iconbitmap(self.iconUrl)
        self.root.resizable(False, False)
        self.root.title(self.title)

    def can_resize(self, resizable_boolean):
        '''
            Allow resize your tk window. By default it's not allowed.
            Parameter:
            resizable_boolean (boolean)
        '''
        self.root.resizable(resizable_boolean, resizable_boolean)

    def change_theme(self, theme):
        '''
            Choose a theme with string, by default theme is light.
            Parameter:
            theme (str)
        '''
        if theme == "dark":
            self.root.config(background='#000000')
        else:
            self.root.config(background='#FFFFFF')

    def execute_window(self):
        '''
            Execute mainloop and indispensable functions
        '''
        self.root.mainloop()