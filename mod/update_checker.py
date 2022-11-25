"""
TT-Damage-Calculator
Copyright (C) 2022 Vhou-Atroph
"""

from tkinter import *
from tkinter import messagebox
import webbrowser

from mod import tt_settings

def compare_versions(local_file):
  try:
    data = tt_settings.comp_data(local_file)
  except:
    messagebox.showerror("Error", "Something went wrong checking your version. Are you connected to the internet and have a version.txt file?")
  if data[0]:
    messagebox.showinfo("Latest Version", "You are using the latest version of the Toontown Gag Calculator.")
  else:
    diff_version(data[2],data[1])

def diff_version(local,git):
  popup=Toplevel()
  popup.title("New Version")
  popup.resizable(0,0)
  popup_label=Label(popup,text="A new version may be available!",font=('Arial',11,'normal'))
  popup_label.grid(pady=6,padx=4,row=0,columnspan=2)
  cur_ver_label=Label(popup,text="Your version:",font=('Arial',11,'bold'))
  cur_ver_label.grid(padx=7,row=1,column=0)
  cur_ver_id_label=Label(popup,text=local,font=('Arial',10,'italic'))
  cur_ver_id_label.grid(row=2,column=0)
  new_ver_label=Label(popup,text="Latest Version:",font=('Arial',11,'bold'))
  new_ver_label.grid(padx=7,row=1,column=1)
  new_ver_id_label=Label(popup,text=git,font=('Arial',10,'italic'))
  new_ver_id_label.grid(row=2,column=1)
  popup_button=Button(popup,text="Take me to Github!",font=('Arial',11,'normal'))
  popup_button.configure(command=lambda:webbrowser.open_new_tab('https://github.com/Vhou-Atroph/TT-Damage-Calculator'))
  popup_button.grid(pady=5,columnspan=2)
  popup.mainloop()