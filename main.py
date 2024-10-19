import sys
from tkinter import *  
from tkinter import filedialog, font

# Initialize root window
root = Tk()
root.title("Text Editor")
root.geometry("700x500")
text = Text(root, font=("Arial", 12), undo=True)
text.grid(row=1, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Font setting
current_font_family = "Arial"
current_font_size = 12

# Opens files
def open_file():
    file = filedialog.askopenfilename(defaultextension=".txt", 
                                      filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file:
        text.delete(1.0, END)
        with open(file, "r") as f:
            text.insert(INSERT, f.read())

# Saves Files
def saveas():
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if savelocation:
        with open(savelocation, "w") as file1:
            file1.write(t)

# Text formatting
def apply_tag(tag_name, font_style):
    current_tags = text.tag_names("sel.first")
    if tag_name in current_tags:
        text.tag_remove(tag_name, "sel.first", "sel.last")
    else:
        text.tag_add(tag_name, "sel.first", "sel.last")
    text.tag_configure(tag_name, font=(current_font_family, current_font_size, font_style))

def make_bold():
    apply_tag("bold", "bold")

def make_italic():
    apply_tag("italic", "italic")

def make_underline():
    apply_tag("underline", "underline")

# Font selection
def change_font(event=None):
    global current_font_family
    selected_font = font_dropdown.get()
    current_font_family = selected_font
    text.config(font=(current_font_family, current_font_size))

# Text size selection
def change_font_size(event=None):
    global current_font_size
    selected_size = size_dropdown.get()
    current_font_size = int(selected_size)
    text.config(font=(current_font_family, current_font_size))

# Toolbar
open_button = Button(root, text="Open", command=open_file)
open_button.grid(row=0, column=0, padx=5, pady=5)

save_button = Button(root, text="Save", command=saveas)
save_button.grid(row=0, column=1, padx=5, pady=5)

bold_button = Button(root, text="Bold", command=make_bold)
bold_button.grid(row=0, column=2, padx=5, pady=5)

italic_button = Button(root, text="Italic", command=make_italic)
italic_button.grid(row=0, column=3, padx=5, pady=5)

underline_button = Button(root, text="Underline", command=make_underline)
underline_button.grid(row=0, column=4, padx=5, pady=5)

font_dropdown = StringVar(root)
font_dropdown.set("Arial")  # Default font
available_fonts = ["Arial", "Courier", "Times New Roman", "Helvetica", "Verdana"]
font_menu = OptionMenu(root, font_dropdown, *available_fonts, command=change_font)
font_menu.grid(row=0, column=5, padx=5, pady=5)

size_dropdown = StringVar(root)
size_dropdown.set("12")  # Default size
available_sizes = [str(size) for size in range(8, 32, 2)]
size_menu = OptionMenu(root, size_dropdown, *available_sizes, command=change_font_size)
size_menu.grid(row=0, column=6, padx=5, pady=5)

root.mainloop()