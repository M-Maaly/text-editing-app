import tkinter as tk
from tkinter.filedialog import askopenfilename

def open_file():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    if not filepath:
        return
    
    txt_edit.delete(1.0, tk.END)

    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END), text
        
    window.title(f"AlmdrasaTextEditor") - {filepath}

def save_file():
    filepath = askopenfilename(
        defaultextension="txt",
        filepath=[("Text Files", "*.txt"), ("All Files", "*.*")])
    
    if not filepath:
        return
    
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)

    window.title(f"AlmdrasaTextEditor") - {filepath}


window = tk.Tk()
window.title("Almdrasa Text Editor")
window.rowconfigure(0, minsize=600)
window.columnconfigure(1, minsize=800)

txt_edit = tk.Text(window)
frame_buttons = tk.Frame(window, relief=tk.RAISED, )
btn_open = tk.Button(frame_buttons, text="Open file", command=open_file)
btn_save = tk.Button(frame_buttons, text="Save as", command=save_file)

btn_open.grid(column=0, row=0, padx=5, pady=5, sticky="ew")
btn_save.grid(column=0, row=1, padx=5, sticky="ew")

frame_buttons.grid(column=0, row=0, sticky="ns")
txt_edit.grid(column=1, row=0, sticky="nsew")


window.mainloop()