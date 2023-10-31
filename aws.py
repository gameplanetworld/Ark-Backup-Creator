import tkinter as tk
from tkinter.filedialog import askdirectory
from distutils.dir_util import copy_tree
from tkinter import font
from tkinter import *

src_path = r""
dst_path = r""

with open("srcpath.txt", 'r') as f:
    for src_path in f:
        src_path = src_path
with open("dstpath.txt", 'r') as f:
    for dst_path in f:
        dst_path = dst_path

# GUI Start
root = tk.Tk()
root.title("Ark World Backup")
root.resizable(False, False)
root.config(bg="#1D1D1D")
root.iconbitmap("arklogo.ico")

def resize_window():
    desired_width = 300
    desired_height = 380

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - desired_width) // 2
    y = (screen_height - desired_height) // 2

    root.geometry(f"{desired_width}x{desired_height}+{x}+{y}")
resize_window()

pixel = tk.PhotoImage(width=1, height=1)
textfont = font.Font(family="Ariel", size=22, weight="bold")


# Save Folder Destination
def srcpathcheck():
    if src_path != "":
        SaveFolderDtsEntry.insert(0,src_path)

def SaveFolderDts():
    SaveFolder = askdirectory()
    src_path = SaveFolder
    SaveFolderDtsEntry.delete(0,END)
    SaveFolderDtsEntry.insert(0,src_path)
    with open('srcpath.txt','w') as data:
        data.write(str(src_path))

#style (SFDB)
SFDB_frame_color = "#3B3B3B"
SFDB_frame = tk.Frame(root, bg=SFDB_frame_color, highlightbackground=SFDB_frame_color, highlightthickness=1)
SFDB_frame.place(x=0, y=60)

#font (SFDB)
SFDB_Font = font.Font(family="Ariel", size=10, weight="bold")

#button (SFDB)
SaveFolderDtsButton = tk.Button(SFDB_frame, command=SaveFolderDts, bg="#313131", fg="white", activebackground="#1D1D1D", activeforeground="white", relief="flat", text="Change The Folder Destanation", font=SFDB_Font, image=pixel, height=25, width=300, compound="c")
SaveFolderDtsButton.pack()

#style (SFDT)
SFDE_frame_color = "#3B3B3B"
SFDE_frame = tk.Frame(root, bg=SFDE_frame_color, highlightbackground=SFDE_frame_color, highlightthickness=1)
SFDE_frame.place(x=0, y=40)

#entry (SFDT)
SaveFolderDtsEntry = tk.Entry(SFDE_frame, width=49, background="#959595", foreground="black")
SaveFolderDtsEntry.pack()

#text
SFDT = tk.Label(root, text="Ark Folder:", font=textfont, bg="#1D1D1D", fg="white")
SFDT.pack()

#check if source path already exsist
srcpathcheck()


# Destination Folder Destination
def dstpathcheck():
    if dst_path != "":
        DstFolderDtsEntry.insert(0,dst_path)

def DstFolderDts():
    DstFolder = askdirectory()
    dst_path = DstFolder
    DstFolderDtsEntry.delete(0,END)
    DstFolderDtsEntry.insert(0,dst_path)
    with open('dstpath.txt','w') as data:
        data.write(str(dst_path))

#style (DFDB)
SFDB_frame_color = "#3B3B3B"
SFDB_frame = tk.Frame(root, bg=SFDB_frame_color, highlightbackground=SFDB_frame_color, highlightthickness=1)
SFDB_frame.place(x=0, y=160)

#font (DFDB)
SFDB_Font = font.Font(family="Ariel", size=10, weight="bold")

#button (DFDB)
DstFolderDtsButton = tk.Button(SFDB_frame, command=DstFolderDts, bg="#313131", fg="white", activebackground="#1D1D1D", activeforeground="white", relief="flat", text="Change The Folder Destanation", font=SFDB_Font, image=pixel, height=25, width=300, compound="c")
DstFolderDtsButton.pack()

#style (DFDT)
DFDE_frame_color = "#3B3B3B"
DFDE_frame = tk.Frame(root, bg=DFDE_frame_color, highlightbackground=DFDE_frame_color, highlightthickness=1)
DFDE_frame.place(x=0, y=140)

#entry (DFDT)
DstFolderDtsEntry = tk.Entry(DFDE_frame, width=49, background="#959595", foreground="black")
DstFolderDtsEntry.pack()

#text
DFDT = tk.Label(root, text="Backup Folder:", font=textfont, bg="#1D1D1D", fg="white")
DFDT.place(x=45, y=100)

#check if source path already exsist
dstpathcheck()


# Copy Paths (src_path -> dst_path)
def src_dst():
    with open("srcpath.txt", 'r') as f:
        for src_path in f:
            src_path = src_path
    with open("dstpath.txt", 'r') as f:
        for dst_path in f:
            dst_path = dst_path
    copy_tree(src_path, dst_path)
    StatusResult.config(text="Backup Saved")
    
    
#frame
SRC_DST_frame_color = "#3B3B3B"
SRC_DST_frame = tk.Frame(root, bg=SRC_DST_frame_color, highlightbackground=SRC_DST_frame_color, highlightthickness=1)
SRC_DST_frame.place(x=0, y=240)

#text
src_dst_text = tk.Label(root, text="Backup Saver:", font=textfont, bg="#1D1D1D", fg="white")
src_dst_text.place(x=45, y=200)

#button font
bfont = font.Font(family="Ariel", size=13, weight="bold")

#SRC_DST button
SRC_DST_Button = tk.Button(SRC_DST_frame, command=src_dst, bg="#313131", fg="white", activebackground="#1D1D1D", activeforeground="white", relief="flat", font=bfont, text="Backup ARK Save", compound="c", image=pixel, width=140, height=75)
SRC_DST_Button.pack()


# Copy Paths (dst_path -> src_path)
def dst_src():
    with open("srcpath.txt", 'r') as f:
        for src_path in f:
            src_path = src_path
    with open("dstpath.txt", 'r') as f:
        for dst_path in f:
            dst_path = dst_path
    
    copy_tree(dst_path, src_path)
    StatusResult.config(text="Backup Restored")
    
    
#frame
dst_src_frame_color = "#3B3B3B"
dst_src_frame = tk.Frame(root, bg=dst_src_frame_color, highlightbackground=dst_src_frame_color, highlightthickness=1)
dst_src_frame.place(x=150, y=240)

#text
dst_src_text = tk.Label(root, text="Backup Saver:", font=textfont, bg="#1D1D1D", fg="white")
dst_src_text.place(x=45, y=200)

#button font
bfont = font.Font(family="Ariel", size=13, weight="bold")

#dst_src button
dst_src_Button = tk.Button(dst_src_frame, command=dst_src, bg="#313131", fg="white", activebackground="#1D1D1D", activeforeground="white", relief="flat", font=bfont, text="Restore Backup", compound="c", image=pixel, width=140, height=75)
dst_src_Button.pack()



# Status System
statusfont = font.Font(family="Ariel", size=14, weight="bold")

Status = tk.Label(root, text="Status: ", font=textfont, bg="#1D1D1D", fg="white")
Status.place(x=10, y=330)

StatusResult = tk.Label(root, text="Not Saved", font=statusfont, bg="#1D1D1D", fg="white")
StatusResult.place(x=120, y=337)


# GUI End
root.mainloop()