import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """
    Open a file and display its content in the text widget.
    """
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    if not filepath:
        return
    
    txt_edit.delete(1.0, tk.END)

    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
        
    window.title(f"Almdrasa Text Editor - {filepath}")

def save_file():
    """
    Save the content of the text widget to a file.
    """
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    
    if not filepath:
        return
    
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)

    window.title(f"Almdrasa Text Editor - {filepath}")


# Create the main window
window = tk.Tk()
window.title("Almdrasa Text Editor")
window.geometry("800x600")  # Set the initial size of the window

# Create widgets
txt_edit = tk.Text(window)
frame_buttons = tk.Frame(window, relief=tk.RAISED)
btn_open = tk.Button(frame_buttons, text="Open file", command=open_file)
btn_save = tk.Button(frame_buttons, text="Save as", command=save_file)

# Grid layout for widgets
btn_open.grid(column=0, row=0, padx=5, pady=5, sticky="ew")
btn_save.grid(column=0, row=1, padx=5, sticky="ew")

frame_buttons.grid(column=0, row=0, sticky="ns")
txt_edit.grid(column=1, row=0, sticky="nsew")

# Configure grid weights for resizing
window.columnconfigure(1, weight=1)  # Make the text widget expand with the window
window.rowconfigure(0, weight=1)

# Start the main event loop
window.mainloop()
