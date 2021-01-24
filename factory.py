import tkinter as tk
from typing import List

def make_root() -> tk.Tk:
    root = tk.Tk()
    root.title('Calculator')
    root.config(padx = 10, pady = 10, background = '#323232')
    root.resizable(False, False)
    return root
def make_label(root) -> tk.Label:
    label = tk.Label(
        root, text ='Sem Contas',
        anchor = 'e', justify = 'right'
    )
    label.grid(row = 0, column = 0, columnspan = 5, sticky = 'news')
    return label
def make_display(root) -> tk.Entry:
    display = tk.Entry(root)
    display.grid(row = 1, column = 0, columnspan = 5, sticky = 'news', pady = (0, 10))
    display.config(
        font = ('Helvetica', 40, 'bold'),
        justify ='right',
        bd = 1,
        relief = 'flat'
        )
    display.bind('<Control-a>', displayControlA)
    return display
def displayControlA(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'
def make_buttons(root) -> List[List[tk.Button]]:
    buttonTexts: List[List[str]] = [
        ['7','8','9','+','C'],
        ['4','5','6','-','/'],
        ['1','2','3','*','^'],
        ['0','.','(',')','=']
    ]
    buttons: List[List[tk.Button]] = []

    for row, rowValue in enumerate(buttonTexts,start = 2):
        buttonRow = []
        for colIndex, colValue in enumerate(rowValue):
            btn = tk.Button(root, text = colValue)
            btn.grid(row = row, column = colIndex, sticky = 'news', padx = 5, pady = 5)
            btn.config(
                font = ('Helvetica', 15 , 'normal'),
                pady = 40, width = 1, background = '#323232', bd = 0, cursor = 'hand2',
                fg ='#8aff00'
                )
            buttonRow.append(btn)
        buttons.append(buttonRow)
    return buttons
