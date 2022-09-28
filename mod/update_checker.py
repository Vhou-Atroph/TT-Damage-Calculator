"""
TT-Damage-Calculator
Copyright (C) 2022 Vhou-Atroph
"""

from tkinter import *
from tkinter import messagebox
import urllib.request
import webbrowser

def compare_versions(local_file,git_file):
  try:
    local_file=open(local_file,"r").read()
  except:
    messagebox.showerror("Error", "Could not find the local version.txt")
    raise BaseException("Could not find the local version.txt")
  try:
    git_file=urllib.request.urlopen(git_file).read()
    git_file=git_file.decode('UTF-8')
  except:
    messagebox.showerror("Error", "Something went wrong looking for the most recent version.txt. Are you connected to the internet?")
    raise BaseException("Something went wrong looking for the most recent version.txt. Are you connected to the internet?")
  #print(local_file)
  #print(git_file)
  if local_file==git_file:
    #print("Current version is the latest version.")
    messagebox.showinfo("Latest Version", "You are using the latest version of the Toontown Gag Calculator.")
  else:
    #print("Git version is a different version, probably later.")
    diff_version(local_file,git_file)

def diff_version(local,git):
  popup=Toplevel()
  popup.title("New Version")
  popup.resizable(0,0)
  popup_label=Label(popup,text="A new version may be available!",font=('Arial',11,'normal'))
  popup_label.grid(pady=6,padx=4,row=0,columnspan=2)
  cur_ver_label=Label(popup,text="Current Version:",font=('Arial',11,'bold'))
  cur_ver_label.grid(padx=7,row=1,column=0)
  cur_ver_id_label=Label(popup,text=local,font=('Arial',10,'italic'))
  cur_ver_id_label.grid(row=2,column=0)
  new_ver_label=Label(popup,text="GitHub Version:",font=('Arial',11,'bold'))
  new_ver_label.grid(padx=7,row=1,column=1)
  new_ver_id_label=Label(popup,text=git,font=('Arial',10,'italic'))
  new_ver_id_label.grid(row=2,column=1)
  popup_button=Button(popup,text="Take me to Github!",font=('Arial',11,'normal'))
  popup_button.configure(command=lambda:webbrowser.open_new_tab('https://github.com/Vhou-Atroph/TT-Damage-Calculator'))
  popup_button.grid(pady=5,columnspan=2)
  popup.mainloop()