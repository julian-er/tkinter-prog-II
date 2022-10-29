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

    def __init__(self, title='DS Urquiza',  iconUrl='./assets/icon_inmo.ico', cols=12, rows=12):

        # define variables
        self.title = title
        self.iconUrl = iconUrl
        self.col = cols
        self.row = rows
        self.root = Tk()

        self.root.minsize(width=500, height=500)
        self.root.resizable(False, False)
        self.root.title(self.title + ' second term practice')

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
        if theme.lower() == "dark":
            self.root.title(self.title + ' - dark theme')
            self.root.config(background='#000000')
        else:
            self.root.title(self.title + ' - light theme')
            self.root.config(background='#FFFFFF')

    def define_cols_quantity(self):
        '''
            Choose quantity columns for your grid

            Parameter:
            col (int) : default 12
        '''
        for x in range(self.col):
            self.root.columnconfigure(x, weight=1, uniform="x")

    def define_rows_quantity(self):
        '''
            Choose quantity columns for your grid

            Parameter:
            col (int) : default 12
        '''
        for x in range(self.row):
            self.root.rowconfigure(x, weight=1, uniform="x")

    def execute_window(self):
        '''
            Execute mainloop and indispensable functions
        '''
        self.define_cols_quantity()
        self.define_rows_quantity()    

