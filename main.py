from tkinter import *

'''VERSION 0

CONTRIBUTORS:
- Vhou-Atroph
'''

#Dictionaries
gags={
#Sound
"bike horn" : 4,
"whistle" : 7,
"bugle" : 11,
"aoogah" : 16,
"elephant trunk" : 21,
"foghorn" : 50,
"opera singer" : 90,

#Throw
"cupcake" : 6,
"fruit pie slice" : 10,
"cream pie slice" : 17,
"whole fruit pie" : 27,
"whole cream pie" : 40,
"birthday cake" : 100,
"wedding cake" : 120,

#Squirt
"squirting flower" : 4,
"glass of water" : 8,
"squirt gun" : 12,
"selzter bottle" : 21,
"fire hose" : 30,
"storm cloud" : 80,
"geyser" : 105,

#Drop
"flower pot" : 10,
"sandbag" : 18,
"anvil" : 30,
"big weight" : 45,
"safe" : 60,
"grand piano" : 170,
"toontanic" : 180
}

#NTS gagsOrg dict

#Window
global window
window=Tk()
window.title("Toontown Damage Calculator")
icon=PhotoImage(file="img/whole-cream-pie.png")
window.iconphoto(True, icon)

#Columns
col1=Frame(window) #Main content of the calculator
col2=Frame(window) #Will be used for calculation history

#Toggles
togBtns=Frame(col1)
orgBtn=Button(togBtns,text='Toggle Organic')
lurChk=Checkbutton(togBtns,text='Cog lured')
emptLbl=Label(togBtns)
clcBtn=Button(togBtns,text='Calculate',font=('Arial',10,'bold'))

#The Gags
gagFrame=Frame(col1)
#Sound
sndFrame=Frame(gagFrame)
bHornImg=PhotoImage(file='img/bike-horn.png') #Will likely turn images into raw data at some point
bHorn=Button(sndFrame,image=bHornImg)
whistleImg=PhotoImage(file='img/whistle.png')
whistle=Button(sndFrame,image=whistleImg)
bugleImg=PhotoImage(file='img/bugle.png')
bugle=Button(sndFrame,image=bugleImg)
aoogahImg=PhotoImage(file='img/aoogah.png')
aoogah=Button(sndFrame,image=aoogahImg)
eTrunkImg=PhotoImage(file='img/elephant-trunk.png')
eTrunk=Button(sndFrame,image=eTrunkImg)
fHornImg=PhotoImage(file='img/fog-horn.png')
fHorn=Button(sndFrame,image=fHornImg)
oSingerImg=PhotoImage(file='img/opera-singer.png')
oSinger=Button(sndFrame,image=oSingerImg)

#Geometry - Main Columns
col1.grid(column=0,row=0,padx=10) #In retrospect I should have used 0 for the column name too, but it doesn't matter *that* much.
col2.grid(column=1,row=0)

#Geometry - Toggles
togBtns.grid(column=0,row=1,pady=10)
lurChk.grid(column=0,row=0,padx=5)
orgBtn.grid(column=1,row=0,padx=5)
emptLbl.grid(column=2,row=0,padx=60)
clcBtn.grid(column=3,row=0)

#Geometry - Gags
gagFrame.grid(column=0,row=2,pady=10)
#Sound
sndFrame.grid(column=0,row=0)
bHorn.grid(column=0,row=0)
whistle.grid(column=1,row=0)
bugle.grid(column=2,row=0)
aoogah.grid(column=3,row=0)
eTrunk.grid(column=4,row=0)
fHorn.grid(column=5,row=0)
oSinger.grid(column=6,row=0)

#Run
window.mainloop()