import re
import tkinter as tk
import math
from typing import List



class Calculator:
    def __init__(self, root: tk.Tk, label: tk.Label, display: tk.Entry , buttons: List[List[tk.Button]]):
        self.root = root
        self.label = label
        self.display = display
        self.buttons = buttons

    def start(self):
        self.configButtons()
        self.configDisplay
        self.root.mainloop()
    def configButtons(self):
        buttons = self.buttons
        for rowValues in buttons:
            for button in rowValues:
                buttonText = button['text']

                if buttonText == 'C':
                    button.bind('<Button-1>', self.clear)
                    button.config(bg = '#8aff00', fg='#fff')
                if buttonText in '0123456789.+-/*()^':
                    button.bind('<Button-1>', self.addTextDisplay)
                if buttonText == '=':
                    button.bind('<Button-1>', self.calculate)
                    button.config(bg = '#42124c', fg = '#fff')

    def configDisplay(self):
        self.display.bind('<Return>', self.calculate)
        self.display.bind('<KP_Enter>', self.calculate)

    def fixText(self, text):
        # Substitui tudo que não for 0123456789+*-/^
        text = re.sub(r'[^\d\.\/\*\-\+\^\(\)e]', r'', text,0)
        # Substitui sinais repetidos para apenas um sinal
        text = re.sub(r'([\.\+\/\-\*\^])\1+',r'\1',text,0)
        # Substitui () ou *() para nada
        text = re.sub(r'\*?\(\)', '', text)

        return text
    def clear(self, event = None):
        self.display.delete(0, 'end')
    def addTextDisplay(self,event):
        self.display.insert('end', event.widget['text'])
    def calculate(self,event):
        fixedText = self.fixText(self.display.get())
        equations = self.getEquations(fixedText)

        try:
            if len(equations) == 1:
                result = eval(self.fixText(equations[0]))
            else:
                result = eval(self.fixText(equations[0]))
                for equation in equations[1:]:
                    result = math.pow(result, eval(self.fixText(equation)))
            self.display.delete(0, 'end')
            self.display.insert('end', result)
            self.label.config(text = f'{fixedText} = {result}')

        except OverflowError:
            self.label.config(text = 'Overflow')
        except Exception as e:
            self.label.config(text = e)
    def getEquations (self, text) :
        return re.split(r'\^', text, 0)
        
