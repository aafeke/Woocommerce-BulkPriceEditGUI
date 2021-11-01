import csv_tool
import tkinter as tk
from tkinter import Frame, ttk, messagebox
from tkinter.filedialog import askopenfilename

# State codes
#   0: Awaiting import
#   1: Import succeeded with no changes on file
#   2: Export succeeded

state = 0
filePath = ''

def init():
    # Initialize widgets and UI.
    global root, button_Export, button_Import, label_FileName, frame
    global label_Constant, entry_Constant, button_Add

    root = tk.Tk()

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
        onError(1)
        return
    
    # Check for the price header in the file
    elif( csv_tool.verifyFile(filePath) ):
        label_FileName.config(text=filePath)

        # Prepare for the CSV operations
        csv_tool.prepare(filePath)
        # Set the status flag
        switchState(1)

    else:
        onError(2)

def onExport():
    constant = entry_Constant.get()

    # Check if input is a number or is in '%{number}' format.
    try: float(constant)
    except ValueError:
        try: float(constant.replace('%', ''))
        except ValueError: 
            onError(0)
            return
    
    # If input is fine, switch to state 2
    try: csv_tool.modify(constant)
    except: onError(3)
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
        messagebox.showinfo(title='Success', message='Output generated in ".temp" folder under current directory.')

        # Return to first state
        switchState(0)

def onError(code: int):
    """
    Handles errors.
    0: Convertion Error
    1: Not a CSV File
    2: Required Headers Could Not Found in the CSV File
    3: Unexpected
    """
    if code == 0:
        print('\a')
        messagebox.showerror(title='Error', message='The input is not valid')
        entry_Constant.delete(0, 'end')
        switchState(1)
    elif code == 1:
        print('\a')
        messagebox.showerror(title='Error', message='Unknown File Type')
        switchState(0)
    elif code == 2:
        print('\a')
        label_FileName.config(text='"Price" header could not found in given file')
        switchState(0)
    else:
        print('\a')
        messagebox.showerror(title='Error', message='Unexpected Error')
        switchState(0)

init()
root.mainloop()