# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 13:17:11 2022

@author: Dimitris
"""

from os import listdir, path

from googletrans import Translator
from paddleocr import PaddleOCR

from tkinter import Tk, Label, OptionMenu, Button, StringVar
from tkinter import filedialog

def language_to_code(argument):
    switcher = {
        "English": "en",
        "German": "de",
        "Spanish": "es",
        "French": "fr"
    }

    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(argument, "nothing")

def get_image_files(parent_dir):
    files = []
    
    for file_name in listdir(parent_dir):
        if file_name.endswith(".jpg") or file_name.endswith(".png"):
            file_path = path.join(parent_dir, file_name)
            files.append(file_path)

    return files

def translate():
    global clicked, directory
    
    # Change tkinter
    drop.destroy()
    button.destroy()
    file_open.destroy()
    label.config(text = "Detection Language: {}".format(clicked.get()))
    
    label_2 = Label( root , text = "Translation Language: English" )
    label_2.pack(pady = 10)
    
    text_label = Label( root , text = "Initializing scanner..." )
    text_label.pack(pady = 10)
    
    prog_label = Label( root , text = "" )
    prog_label.pack(pady = 10)
    
    root.update()
    
    lang = language_to_code(clicked.get())
            
    ocr = PaddleOCR(lang = lang, use_gpu = False) # need to run only once to download and load model into memory
    
    translator = Translator()
    
    original_file = open(path.join(directory, "original.txt"), "a")
    translation_file = open(path.join(directory, "translation.txt"), "a")
    
    image_files = get_image_files(directory)
    
    total = len(image_files)
    completed = 0
    
    text_label.config(text = "Images scanned:")
    
    for image_path in image_files:
        prog_label.config(text = "{}/{}".format(completed, total))
        root.update()
  
        result = ocr.ocr(image_path, cls=False)        
        
        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                text = line[1][0]
                original_file.write(text + "\n")
                
                translation = translator.translate(text)
                translation_file.write(translation.text + "\n")                
               
        # New lines for new image
        original_file.write("\n\n\n")
        translation_file.write("\n\n\n")
        
        completed += 1
        
    root.destroy()
    original_file.close()
    translation_file.close()

root = Tk()
root.title("Image Translator")
root.geometry("350x200")

def clear_frame():
   for widgets in root.winfo_children():
      widgets.destroy()

# Dropdown menu options
options = [
    "English",
    "German",
    "Spanish",
    "French"
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set( "English" )

# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()



#function definition for opening file dialog
def openf():
    global label, directory
    directory = filedialog.askdirectory(initialdir='/', title="Select Folder")
    label.config(text = directory)

file_open = Button(root, text="Open file", command= openf)
file_open.pack(pady = 10)

# Create Label
label = Label( root , text = "/" )
label.pack(pady = 10)

# Create button, it will change label text
button = Button( root , text = "Translate" , command = translate )
button.pack(pady = 10)


# Execute tkinter
root.mainloop()