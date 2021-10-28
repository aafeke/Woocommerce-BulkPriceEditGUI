#TODO: 
#   Fix the local variable issue in the main.getDir()    

import csv_tool
import tkinter as tk
from tkinter import Frame, Text, ttk, messagebox
from tkinter.filedialog import askopenfilename

# State codes
#   0: Awaiting import
#   1: Import succeeded with no changes on file
#   2: Import succeeded and file got changed

state = 0
filePath = ''

def init():
    # Initialize widgets and UI.
    global root, button_Export, button_Import, label_FileName, frame
    global label_Constant, entry_Constant, button_Add

    root = tk.Tk()
    #root.geometry('290x120+0+0')

    frame= Frame(root)
    frame.pack(fill= 'both', expand= True, padx= 5, pady=5)

    label_FileName = ttk.Label(
        frame,
        text='Please Import a CSV File'
        )

    button_Import = ttk.Button(
        frame, 
        text="Import CSV", 
        command=onImport,
        )

    button_Export = ttk.Button(
        frame, 
        text="Export CSV",
        command=onExport,  
        state='disabled'
        )

    label_Constant = ttk.Label(
        frame,
        text='Add a constant value:'
    )

    entry_Constant = ttk.Entry(
        frame,
    )
    
    # Positionings
    label_FileName.grid(row=0, column=0)
    button_Import.grid(row=1, column=0)
    button_Export.grid(row=2, column=0)

    label_Constant.grid(row=0, column=1, padx=20)
    entry_Constant.grid(row=1, column=1, padx=20)

def onImport():
    # Get the path of the CSV file.

    filePath = askopenfilename()

    # If not a csv file, beep and return
    if(not filePath.endswith('.csv')):
        print('\a')
        return
    
    # Check for the price header in the file
    if( csv_tool.verifyFile(filePath) ):
        label_FileName.config(text=filePath)

        # Prepare for the CSV operations
        csv_tool.prepare(filePath)
        # Set the status flag
        switchState(1)

    else:
        print('\a')
        label_FileName.config(text='"Price" header could not found in given file')

def onExport():
    constant = entry_Constant.get()
    try: constant = float(constant)
    except:
        print('\a')
        messagebox.showerror(title='Error', message='Input is not a number')
        entry_Constant.delete(0, 'end')
        return
    csv_tool.modify(constant)
    switchState(2)

def switchState(statusCode):
    global state
    if(statusCode == 0):
        state = 0
        button_Export.config(state='disabled')
        label_FileName.config(text='Please Import a CSV File')
        entry_Constant.delete(0, 'end')
    if(statusCode == 1):
        state = 1 
        button_Export.config(state='enabled')
    if(statusCode == 2):
        state = 2
        button_Export.config(state='disabled')
        messagebox.showinfo(title='Success', message='Output generated in "output" folder under current directory.')

init()
root.mainloop()