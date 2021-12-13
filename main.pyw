from tkinter import *
import math
import os

'''VERSION A-2.0.0 UNSTABLE

CONTRIBUTORS:
- Vhou-Atroph
- BoggoTV
'''

#Window
global window
window=Tk()
window.title("Toontown Damage Calculator")
icon=PhotoImage(file="img/whole-cream-pie.png")
window.iconphoto(True, icon)
window.resizable(0,0)

#Variables
global lured
global dmgDown
global dlLock
global organic
global sndUsed
global trwUsed
global sqtUsed
global drpUsed
global trpUsed
global totDmg
lured=IntVar()
defValues=['0%','10%','15%','20%']
dmgDown=StringVar()
dmgDown.set('0%')
dlOptions=['No lock','Lock lure','Lock defense','Lock both']
dlLock=StringVar()
dlLock.set('No lock')
organic=0
sndUsed=list()
trwUsed=list()
sqtUsed=list()
drpUsed=list()
trpUsed=list()
totDmg=0

#Columns
col1=Frame(window) #Main content of the calculator
col2=Frame(window) #Will be used for calculation history

#Total damage calculation
def clcDmg(opt=""):
  global lured
  localLure=0
  if lured.get()==1: #Find out if lure is enabled. If it is, save a local variable.
    localLure=1
  if len(trpUsed)>0:
    trpDmgClc()
  if len(sndUsed)>0:
    sndDmgClc()
  if len(trwUsed)>0:
    trwDmgClc()
  if len(sqtUsed)>0:
    sqtDmgClc()
  if len(drpUsed)>0:
    drpDmgClc()
  global totDmg
  print("Total damage this round: "+str(totDmg))
  theDmg.configure(text=str(totDmg))
  cHPIndClc()
  totDmg=0
  if localLure==1:
    lured.set(1)

#Toggles
togBtns=Frame(col1)
orgBtn=Button(togBtns,text='Toggle Organic',font=('Arial',11,'normal'))
lurChk=Checkbutton(togBtns,text='Cog lured',variable=lured,onvalue=1,offvalue=0,font=('Arial',11,'normal'),command=clcDmg)
clrBtn=Button(togBtns,text='Reset damage',font=('Arial',11,'normal'))
defLbl=Label(togBtns,text='Defense:',font=('Arial',11,'normal'))
defBtn=OptionMenu(togBtns,dmgDown,*defValues,command=clcDmg)
defBtn.configure(width=4,font=('Arial',11,'normal'))
lockDwn=OptionMenu(togBtns,dlLock,*dlOptions)
lockDwn.configure(width=12,font=('Arial',11,'normal'))

#The Gags
gagFrame=Frame(col1)
#Sound
sndFrame=Frame(gagFrame)
bHornImg=PhotoImage(file='img/bike-horn.png')
bHorn=Button(sndFrame,image=bHornImg,bg='#1888D3',activebackground='#186AD3')
whistleImg=PhotoImage(file='img/whistle.png')
whistle=Button(sndFrame,image=whistleImg,bg='#1888D3',activebackground='#186AD3')
bugleImg=PhotoImage(file='img/bugle.png')
bugle=Button(sndFrame,image=bugleImg,bg='#1888D3',activebackground='#186AD3')
aoogahImg=PhotoImage(file='img/aoogah.png')
aoogah=Button(sndFrame,image=aoogahImg,bg='#1888D3',activebackground='#186AD3')
eTrunkImg=PhotoImage(file='img/elephant-trunk.png')
eTrunk=Button(sndFrame,image=eTrunkImg,bg='#1888D3',activebackground='#186AD3')
fHornImg=PhotoImage(file='img/fog-horn.png')
fHorn=Button(sndFrame,image=fHornImg,bg='#1888D3',activebackground='#186AD3')
oSingerImg=PhotoImage(file='img/opera-singer.png')
oSinger=Button(sndFrame,image=oSingerImg,bg='#1888D3',activebackground='#186AD3')
#Throw
thrwFrame=Frame(gagFrame)
cCakeImg=PhotoImage(file='img/cupcake.png')
cCake=Button(thrwFrame,image=cCakeImg,bg='#1888D3',activebackground='#186AD3')
fPSliceImg=PhotoImage(file='img/fruit-pie-slice.png')
fPSlice=Button(thrwFrame,image=fPSliceImg,bg='#1888D3',activebackground='#186AD3')
cPSliceImg=PhotoImage(file='img/cream-pie-slice.png')
cPSlice=Button(thrwFrame,image=cPSliceImg,bg='#1888D3',activebackground='#186AD3')
wFPieImg=PhotoImage(file='img/whole-fruit-pie.png')
wFPie=Button(thrwFrame,image=wFPieImg,bg='#1888D3',activebackground='#186AD3')
wCPieImg=PhotoImage(file='img/whole-cream-pie.png')
wCPie=Button(thrwFrame,image=wCPieImg,bg='#1888D3',activebackground='#186AD3')
bCakeImg=PhotoImage(file='img/birthday-cake.png')
bCake=Button(thrwFrame,image=bCakeImg,bg='#1888D3',activebackground='#186AD3')
wCakeImg=PhotoImage(file='img/wedding-cake.png')
wCake=Button(thrwFrame,image=wCakeImg,bg='#1888D3',activebackground='#186AD3')
#Squirt
sqrtFrame=Frame(gagFrame)
sFlowerImg=PhotoImage(file='img/squirting-flower.png')
sFlower=Button(sqrtFrame,image=sFlowerImg,bg='#1888D3',activebackground='#186AD3')
gWaterImg=PhotoImage(file='img/glass-of-water.png')
gWater=Button(sqrtFrame,image=gWaterImg,bg='#1888D3',activebackground='#186AD3')
sGunImg=PhotoImage(file='img/squirt-gun.png')
sGun=Button(sqrtFrame,image=sGunImg,bg='#1888D3',activebackground='#186AD3')
sBottleImg=PhotoImage(file='img/seltzer-bottle.png')
sBottle=Button(sqrtFrame,image=sBottleImg,bg='#1888D3',activebackground='#186AD3')
fHoseImg=PhotoImage(file='img/fire-hose.png')
fHose=Button(sqrtFrame,image=fHoseImg,bg='#1888D3',activebackground='#186AD3')
sCloudImg=PhotoImage(file='img/storm-cloud.png')
sCloud=Button(sqrtFrame,image=sCloudImg,bg='#1888D3',activebackground='#186AD3')
geyserImg=PhotoImage(file='img/geyser.png')
geyser=Button(sqrtFrame,image=geyserImg,bg='#1888D3',activebackground='#186AD3')
#Drop
drpFrame=Frame(gagFrame)
fPotImg=PhotoImage(file='img/flower-pot.png')
fPot=Button(drpFrame,image=fPotImg,bg='#1888D3',activebackground='#186AD3')
sBagImg=PhotoImage(file='img/sandbag.png')
sBag=Button(drpFrame,image=sBagImg,bg='#1888D3',activebackground='#186AD3')
anvilImg=PhotoImage(file='img/anvil.png')
anvil=Button(drpFrame,image=anvilImg,bg='#1888D3',activebackground='#186AD3')
bWeightImg=PhotoImage(file='img/big-weight.png')
bWeight=Button(drpFrame,image=bWeightImg,bg='#1888D3',activebackground='#186AD3')
safeImg=PhotoImage(file='img/safe.png')
safe=Button(drpFrame,image=safeImg,bg='#1888D3',activebackground='#186AD3')
gPianoImg=PhotoImage(file='img/grand-piano.png')
gPiano=Button(drpFrame,image=gPianoImg,bg='#1888D3',activebackground='#186AD3')
tTanicImg=PhotoImage(file='img/toontanic.png')
tTanic=Button(drpFrame,image=tTanicImg,bg='#1888D3',activebackground='#186AD3')
#Trap!
trpFrame=Frame(gagFrame)
bPeelImg=PhotoImage(file='img/banana-peel.png')
bPeel=Button(trpFrame,image=bPeelImg,bg='#1888D3',activebackground='#186AD3')
rakeImg=PhotoImage(file='img/rake.png')
rake=Button(trpFrame,image=rakeImg,bg='#1888D3',activebackground='#186AD3')
marblesImg=PhotoImage(file='img/marbles.png')
marbles=Button(trpFrame,image=marblesImg,bg='#1888D3',activebackground='#186AD3')
qSandImg=PhotoImage(file='img/quicksand.png')
qSand=Button(trpFrame,image=qSandImg,bg='#1888D3',activebackground='#186AD3')
tDoorImg=PhotoImage(file='img/trapdoor.png')
tDoor=Button(trpFrame,image=tDoorImg,bg='#1888D3',activebackground='#186AD3')
tntImg=PhotoImage(file='img/tnt.png')
tnt=Button(trpFrame,image=tntImg,bg='#1888D3',activebackground='#186AD3')
rRoadImg=PhotoImage(file='img/railroad.png')
rRoad=Button(trpFrame,image=rRoadImg,bg='#1888D3',activebackground='#186AD3')

#Button list - used for mass configuring the gag buttons
gagBtns=(bHorn,whistle,bugle,aoogah,eTrunk,fHorn,oSinger,cCake,fPSlice,cPSlice,wFPie,wCPie,bCake,wCake,sFlower,gWater,sGun,sBottle,fHose,sCloud,geyser,fPot,sBag,anvil,bWeight,safe,gPiano,tTanic,bPeel,rake,marbles,qSand,tDoor,tnt,rRoad)

#Calculation history
hist=Frame(col2)
histLbl=Label(hist,text="History")
histBox=Text(hist,width=25,height=17,state=DISABLED,font=('Arial',10,'normal'),wrap=WORD)
pinBtn=Button(hist,text="Pin to top")
clrHistBtn=Button(hist,text="Clear History")
cogClc=Button(hist,text="Show Health")

#Calculation results
clcResults=Frame(col1)
dmgThsRnd=Label(clcResults,text="Damage this round:",font=('Arial',16,'normal'))
theDmg=Label(clcResults,text="0",font=('Arial',16,'bold'))
cHPInd=Label(clcResults,text="(level 0)",font=('Arial',8,'normal'))
orgOnOff=Label(clcResults,text="Organic = OFF",font=('Arial',10,'bold'))

#Cog HP
cogHPSheet=Frame(window)
cogHPImg=PhotoImage(file='img/coghp.png')
cogHPLbl=Label(cogHPSheet,image=cogHPImg)

#Toggle organic functions
def togOrgOff():
  global organic
  organic=0
  print("Gags in calculations will no longer be organic!")
  orgBtn.configure(command=togOrgOn)
  orgOnOff.configure(text="Organic = OFF")
  for i in gagBtns:
    i.configure(bg='#1888D3',activebackground='#186AD3')
def togOrgOn():
  global organic
  organic=1
  print("Gags in calculations will now be organic!")
  orgBtn.configure(command=togOrgOff)
  orgOnOff.configure(text="Organic = ON")
  for i in gagBtns:
    i.configure(bg='darkorange',activebackground='orange')
orgBtn.configure(command=togOrgOn)

#Clear inputs function
def clearInputs():
  print("Clearing gag inputs!")
  global lured
  global dmgDown
  global dlLock
  global sndUsed
  global trwUsed
  global sqtUsed
  global drpUsed
  global trpUsed
  localLure=0
  lurInfo='no'
  if lured.get()==1: #Find out if lure is enabled. If it is, save a local variable.
    localLure=1
    lurInfo='yes'
  histBox.configure(state=NORMAL)
  histBox.insert('1.0',"--------\nCalculation finished!\nDamage calculated was: "+theDmg.cget("text")+"\nDefense: "+dmgDown.get()+"\nLure: "+lurInfo+"\n")
  histBox.configure(state=DISABLED)
  if dlLock.get()=='No lock' or dlLock.get()=='Lock lure':
    dmgDown.set('0%')
  lured.set(0)
  sndUsed=list()
  trwUsed=list()
  sqtUsed=list()
  drpUsed=list()
  trpUsed=list()
  togOrgOff()
  clcDmg()
  if localLure==1 and dlLock.get()=='Lock lure' or dlLock.get()=='Lock both': #Use the local variable and dlLock to lock lure as active even after it is set to 0 by clearInputs()
    lured.set(1)
clrBtn.configure(command=clearInputs)

#Clear history function
def clearHistory():
  print("Clearing calculcation history!")
  histBox.configure(state=NORMAL)
  histBox.delete('1.0', END)
  histBox.configure(state=DISABLED)
clrHistBtn.configure(command=clearHistory)

#Clicking on the bike horn button - the first button to be configured, and the button that will be used as the guinea pig for most testing.
def bHornPrs():
  if organic==0:
    #bHorn.configure(bg='#104789',activebackground='#0D3A6D') #maybe a selection indicator?
    sndUsed.append(4)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Bike Horn (4)\n")
    histBox.configure(state=DISABLED)
  else:
    sndUsed.append(5)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Bike Horn (5)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
bHorn.configure(command=bHornPrs)
#Other sound buttons, who gives a fuck
def whistlePrs():
  if organic==0:
    sndUsed.append(7)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Whistle (7)\n")
    histBox.configure(state=DISABLED)
  else:
    sndUsed.append(8)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Whistle (8)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
whistle.configure(command=whistlePrs)
def buglePrs():
  if organic==0:
    sndUsed.append(11)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Bugle (4)\n")
    histBox.configure(state=DISABLED)
  else:
    sndUsed.append(12)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Bugle (12)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
bugle.configure(command=buglePrs)
def aoogahPrs():
  if organic==0:
    sndUsed.append(16)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Aoogah (16)\n")
    histBox.configure(state=DISABLED)
  else:
    sndUsed.append(17)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Aoogah (17)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
aoogah.configure(command=aoogahPrs)
def eTrunkPrs():
  if organic==0:
    sndUsed.append(21)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Elephant Trunk (21)\n")
    histBox.configure(state=DISABLED)
  else:
    sndUsed.append(23)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Elephant Trunk (23)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
eTrunk.configure(command=eTrunkPrs)
def fHornPrs():
  if organic==0:
    sndUsed.append(50)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Foghorn (50)\n")
    histBox.configure(state=DISABLED)
  else:
    sndUsed.append(55)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Foghorn (55)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
fHorn.configure(command=fHornPrs)
def oSingerPrs():
  if organic==0:
    sndUsed.append(90)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Opera Singer (90)\n")
    histBox.configure(state=DISABLED)
  else:
    sndUsed.append(99)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Opera Singer (99)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
oSinger.configure(command=oSingerPrs)

#Throw
def cCakePrs():
  if organic==0:
    trwUsed.append(6)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Cupcake (6)\n")
    histBox.configure(state=DISABLED)
  else:
    trwUsed.append(7)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Cupcake (7)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
cCake.configure(command=cCakePrs)
def fPSlicePrs():
  if organic==0:
    trwUsed.append(10)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Fruit Pie Slice (10)\n")
    histBox.configure(state=DISABLED)
  else:
    trwUsed.append(11)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Fruit Pie Slice (11)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
fPSlice.configure(command=fPSlicePrs)
def cPSlicePrs():
  if organic==0:
    trwUsed.append(18)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Cream Pie Slice (18)\n")
    histBox.configure(state=DISABLED)
  else:
    trwUsed.append(19)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Cream Pie Slice (19)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
cPSlice.configure(command=cPSlicePrs)
def wFPiePrs():
  if organic==0:
    trwUsed.append(27)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Whole Fruit Pie (27)\n")
    histBox.configure(state=DISABLED)
  else:
    trwUsed.append(29)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Whole Fruit Pie (29)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
wFPie.configure(command=wFPiePrs)
def wCPiePrs():
  if organic==0:
    trwUsed.append(40)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Whole Cream Pie (40)\n")
    histBox.configure(state=DISABLED)
  else:
    trwUsed.append(44)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Whole Cream Pie (44)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
wCPie.configure(command=wCPiePrs)
def bCakePrs():
  if organic==0:
    trwUsed.append(100)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Birthday Cake (100)\n")
    histBox.configure(state=DISABLED)
  else:
    trwUsed.append(110)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Birthday Cake (110)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
bCake.configure(command=bCakePrs)
def wCakePrs():
  if organic==0:
    trwUsed.append(120)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Wedding Cake (120)\n")
    histBox.configure(state=DISABLED)
  else:
    trwUsed.append(132)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Wedding Cake (132)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
wCake.configure(command=wCakePrs)

#Squirt
def sFlowerPrs():
  if organic==0:
    sqtUsed.append(4)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Squirting Flower (4)\n")
    histBox.configure(state=DISABLED)
  else:
    sqtUsed.append(5)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Squirting Flower (7)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
sFlower.configure(command=sFlowerPrs)
def gWaterPrs():
  if organic==0:
    sqtUsed.append(8)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Glass of Water (8)\n")
    histBox.configure(state=DISABLED)
  else:
    sqtUsed.append(9)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Glass of Water (9)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
gWater.configure(command=gWaterPrs)
def sGunPrs():
  if organic==0:
    sqtUsed.append(12)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Squirt Gun (12)\n")
    histBox.configure(state=DISABLED)
  else:
    sqtUsed.append(13)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Squirt Gun (13)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
sGun.configure(command=sGunPrs)
def sBottlePrs():
  if organic==0:
    sqtUsed.append(21)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Seltzer Bottle (21)\n")
    histBox.configure(state=DISABLED)
  else:
    sqtUsed.append(23)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Seltzer Bottle (23)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
sBottle.configure(command=sBottlePrs)
def fHosePrs():
  if organic==0:
    sqtUsed.append(30)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Fire Hose (30)\n")
    histBox.configure(state=DISABLED)
  else:
    sqtUsed.append(33)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Fire Hose (33)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
fHose.configure(command=fHosePrs)
def sCloudPrs():
  if organic==0:
    sqtUsed.append(80)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Storm Cloud (80)\n")
    histBox.configure(state=DISABLED)
  else:
    sqtUsed.append(88)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Storm Cloud (88)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
sCloud.configure(command=sCloudPrs)
def geyserPrs():
  if organic==0:
    sqtUsed.append(105)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Geyser (105)\n")
    histBox.configure(state=DISABLED)
  else:
    sqtUsed.append(115)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Geyser (115)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
geyser.configure(command=geyserPrs)

#Drop
def fPotPrs():
  if organic==0:
    drpUsed.append(10)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Flower Pot (10)\n")
    histBox.configure(state=DISABLED)
  else:
    drpUsed.append(11)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Flower Pot (11)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
fPot.configure(command=fPotPrs)
def sBagPrs():
  if organic==0:
    drpUsed.append(18)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Sandbag (18)\n")
    histBox.configure(state=DISABLED)
  else:
    drpUsed.append(19)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Sandbag (19)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
sBag.configure(command=sBagPrs)
def anvilPrs():
  if organic==0:
    drpUsed.append(30)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Anvil (30)\n")
    histBox.configure(state=DISABLED)
  else:
    drpUsed.append(33)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Anvil (33)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
anvil.configure(command=anvilPrs)
def bWeightPrs():
  if organic==0:
    drpUsed.append(45)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Big Weight (45)\n")
    histBox.configure(state=DISABLED)
  else:
    drpUsed.append(49)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Big Weight (49)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
bWeight.configure(command=bWeightPrs)
def safePrs():
  if organic==0:
    drpUsed.append(70)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Safe (70)\n")
    histBox.configure(state=DISABLED)
  else:
    drpUsed.append(77)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Safe (77)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
safe.configure(command=safePrs)
def gPianoPrs():
  if organic==0:
    drpUsed.append(170)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Grand Piano (170)\n")
    histBox.configure(state=DISABLED)
  else:
    drpUsed.append(187)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Grand Piano (187)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
gPiano.configure(command=gPianoPrs)
def tTanicPrs():
  if organic==0:
    drpUsed.append(180)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Toontanic (180)\n")
    histBox.configure(state=DISABLED)
  else:
    drpUsed.append(198)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Toontanic (198)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
tTanic.configure(command=tTanicPrs)

#Trap
def bPeelPrs():
  if organic==0:
    trpUsed.append(12)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Banana Peel (12)\n")
    histBox.configure(state=DISABLED)
  else:
    trpUsed.append(13)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Banana Peel (13)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
bPeel.configure(command=bPeelPrs)
def rakePrs():
  if organic==0:
    trpUsed.append(20)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Rake (20)\n")
    histBox.configure(state=DISABLED)
  else:
    trpUsed.append(22)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Rake (22)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
rake.configure(command=rakePrs)
def marblesPrs():
  if organic==0:
    trpUsed.append(35)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Marbles (35)\n")
    histBox.configure(state=DISABLED)
  else:
    trpUsed.append(38)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Marbles (38)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
marbles.configure(command=marblesPrs)
def qSandPrs():
  if organic==0:
    trpUsed.append(50)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Quicksand (50)\n")
    histBox.configure(state=DISABLED)
  else:
    trpUsed.append(55)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Quicksand (55)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
qSand.configure(command=qSandPrs)
def tDoorPrs():
  if organic==0:
    trpUsed.append(85)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Trapdoor (85)\n")
    histBox.configure(state=DISABLED)
  else:
    trpUsed.append(93)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Trapdoor (93)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
tDoor.configure(command=tDoorPrs)
def tntPrs():
  if organic==0:
    trpUsed.append(180)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: TNT (180)\n")
    histBox.configure(state=DISABLED)
  else:
    trpUsed.append(198)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic TNT (198)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
tnt.configure(command=tntPrs)
def rRoadPrs():
  if organic==0:
    trpUsed.append(200)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Railroad (200)\n")
    histBox.configure(state=DISABLED)
  else:
    trpUsed.append(220)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Railroad (220)\n")
    histBox.configure(state=DISABLED)
  clcDmg()
rRoad.configure(command=rRoadPrs)

#Sound damage calculation
def sndDmgClc():
  localDmg=list()
  if dmgDown.get()=='10%':
    for i in range(len(sndUsed)):
      localDmg.append(sndUsed[i]-math.ceil(sndUsed[i]*.1)) #Defense buff ceils
  elif dmgDown.get()=='15%':
    for i in range(len(sndUsed)):
      localDmg.append(sndUsed[i]-math.ceil(sndUsed[i]*.15))
  elif dmgDown.get()=='20%':
    for i in range(len(sndUsed)):
      localDmg.append(sndUsed[i]-math.ceil(sndUsed[i]*.2))
  else:
    for i in range(len(sndUsed)):
      localDmg.append(sndUsed[i])
  print("Damage of each individual sound gag: "+str(localDmg))
  global lured
  lured.set(0)
  print("If cogs were lured, they aren't anymore! Don't use sound on lured cogs!")
  totSndDmg=sum(localDmg,0)
  if len(sndUsed)>1:
    totSndDmg=totSndDmg+math.ceil((totSndDmg*0.2)) #Group damage bonus always rounds up. See: 3 fogs and 1 aoogah getting rid of level 12 cogs. This does 199.2 damage, but still works.
  print("Total sound damage: "+str(totSndDmg))
  global totDmg
  totDmg=totDmg+totSndDmg

#Throw damage calculation
def trwDmgClc():
  localDmg=list()
  if dmgDown.get()=='10%':
    for i in range(len(trwUsed)):
      localDmg.append(trwUsed[i]-math.ceil(trwUsed[i]*.1))
  elif dmgDown.get()=='15%':
    for i in range(len(trwUsed)):
      localDmg.append(trwUsed[i]-math.ceil(trwUsed[i]*.15))
  elif dmgDown.get()=='20%':
    for i in range(len(trwUsed)):
      localDmg.append(trwUsed[i]-math.ceil(trwUsed[i]*.2))
  else:
    for i in range(len(trwUsed)):
      localDmg.append(trwUsed[i])
  print("Damage of each individual throw gag:"+str(localDmg))
  totTrwDmg=sum(localDmg,0)
  global lured
  if lured.get()==0:
    print("The cogs are not lured, and there will be no 50% damage bonus.")
    if len(trwUsed)>1:
      totTrwDmg=totTrwDmg+math.ceil((totTrwDmg*0.2))
  else:
    print("The cogs are lured, and there will be a 50% damage bonus.") #Lure bonus used to not ceil but does now apparently (TTR V3.0.8).
    if len(trwUsed)>1:
      totTrwDmg=totTrwDmg+math.ceil(totTrwDmg/2)+math.ceil((totTrwDmg*0.2))
    else:
      totTrwDmg=totTrwDmg+math.ceil(totTrwDmg/2)
    lured.set(0)
  print("Total throw damage: "+str(totTrwDmg))
  global totDmg
  totDmg=totDmg+totTrwDmg

#Squirt damage calculation, luckily just throw 2. (Squirt is better than throw and I am tired of people pretending it isn't. It's the superior organic choice. Cowards.)
def sqtDmgClc():
  localDmg=list()
  if dmgDown.get()=='10%':
    for i in range(len(sqtUsed)):
      localDmg.append(sqtUsed[i]-math.ceil(sqtUsed[i]*.1))
  elif dmgDown.get()=='15%':
    for i in range(len(sqtUsed)):
      localDmg.append(sqtUsed[i]-math.ceil(sqtUsed[i]*.15))
  elif dmgDown.get()=='20%':
    for i in range(len(sqtUsed)):
      localDmg.append(sqtUsed[i]-math.ceil(sqtUsed[i]*.2))
  else:
    for i in range(len(sqtUsed)):
      localDmg.append(sqtUsed[i])
  print("Damage of each individual squirt gag:"+str(localDmg))
  totSqtDmg=sum(localDmg,0)
  global lured
  if lured.get()==0:
    print("The cogs are not lured, and there will be no 50% damage bonus.")
    if len(sqtUsed)>1:
      totSqtDmg=totSqtDmg+math.ceil((totSqtDmg*0.2))
  else:
    print("The cogs are lured, and there will be a 50% damage bonus.") #Lure bonus doesn't get rounded for some dumb reason.
    if len(sqtUsed)>1:
      totSqtDmg=totSqtDmg+math.ceil(totSqtDmg/2)+math.ceil((totSqtDmg*0.2))
    else:
      totSqtDmg=totSqtDmg+math.ceil(totSqtDmg/2)
    lured.set(0)
  print("Total squirt damage: "+str(totSqtDmg))
  global totDmg
  totDmg=totDmg+totSqtDmg

#Drop damage calculation
def drpDmgClc():
  localDmg=list()
  if dmgDown.get()=='10%':
    for i in range(len(drpUsed)):
      localDmg.append(drpUsed[i]-math.ceil(drpUsed[i]*.1))
  elif dmgDown.get()=='15%':
    for i in range(len(drpUsed)):
      localDmg.append(drpUsed[i]-math.ceil(drpUsed[i]*.15))
  elif dmgDown.get()=='20%':
    for i in range(len(drpUsed)):
      localDmg.append(drpUsed[i]-math.ceil(drpUsed[i]*.2))
  else:
    for i in range(len(drpUsed)):
      localDmg.append(drpUsed[i])
  print("Damage of each individual drop gag:"+str(localDmg))
  totDrpDmg=sum(localDmg,0)
  global lured
  if lured.get()==0:
    print("The cogs are not lured, so drop is able to hit!")
    if len(drpUsed)>1:
      totDrpDmg=totDrpDmg+math.ceil((totDrpDmg*0.2))
  else:
    print("The cogs are lured, and drop does not work on lured cogs! https://www.youtube.com/watch?v=NV-p_-OvUnA&t=4s")
    totDrpDmg=0
  print("Total drop damage: "+str(totDrpDmg))
  global totDmg
  totDmg=totDmg+totDrpDmg

#Trap damage calculation
def trpDmgClc():
  localDmg=list()
  if dmgDown.get()=='10%':
    for i in range(len(trpUsed)):
      localDmg.append(trpUsed[i]-math.ceil(trpUsed[i]*.1))
  if dmgDown.get()=='15%':
    for i in range(len(trpUsed)):
      localDmg.append(trpUsed[i]-math.ceil(trpUsed[i]*.15))
  if dmgDown.get()=='20%':
    for i in range(len(trpUsed)):
      localDmg.append(trpUsed[i]-math.ceil(trpUsed[i]*.2))
  else:
    for i in range(len(trpUsed)):
      localDmg.append(trpUsed[i])
  print("Damage of each individual trap gag:"+str(localDmg))
  global lured
  if lured.get()==0:
    print("You need to lure cogs if you want trap to work!")
    totTrpDmg=0
  else:
    if len(trpUsed)>1:
      print("The traps canceled out! Only one trap can be used on a cog at a time!")
      totTrpDmg=0
    else:
      print("The trap worked! This can mean only one thing: You used lure AND only one trap on the cog! Amazing! It did "+str(trpUsed[0])+" damage!")
      totTrpDmg=localDmg[0]
      lured.set(0)
  global totDmg
  totDmg=totDmg+totTrpDmg

#Cog HP Cheatsheet Function
def cHPClcDlt():
  cogHPSheet.grid_remove()
  window.geometry('')
  cogClc.configure(text='Show Health',command=cHPClc)
  
def cHPClc():
  cogHPSheet.grid(column=0,row=2,columnspan=2)
  cogHPLbl.grid(column=0,row=0)
  cogClc.configure(text='Hide Health',command=cHPClcDlt)
  window.geometry('')
cogClc.configure(command=cHPClc)

#Pin commands
def unpin():
  window.attributes('-topmost',False)
  pinBtn.configure(command=pin,text='Pin to top')
def pin():
  window.attributes('-topmost',True)
  pinBtn.configure(command=unpin,text='Unpin from top')
pinBtn.configure(command=pin)

#Cog HP Indicator Function
def cHPIndClc():
  global totDmg
  if totDmg<6:
    print("Cannot kill a level one.")
    cHPInd.configure(text="(level 0)")
  elif 5<totDmg<12:
    print("Can kill a level one.")
    cHPInd.configure(text="(level 1)")
  elif 11<totDmg<20:
    print("Can kill a level two.")
    cHPInd.configure(text="(level 2)")
  elif 19<totDmg<30:
    print("Can kill a level three.")
    cHPInd.configure(text="(level 3)")
  elif 29<totDmg<42:
    print("Can kill a level four.")
    cHPInd.configure(text="(level 4)")
  elif 41<totDmg<56:
    print("Can kill a level five.")
    cHPInd.configure(text="(level 5)")
  elif 55<totDmg<72:
    print("Can kill a level six.")
    cHPInd.configure(text="(level 6)")
  elif 71<totDmg<90:
    print("Can kill a level seven.")
    cHPInd.configure(text="(level 7)")
  elif 89<totDmg<110:
    print("Can kill a level eight.")
    cHPInd.configure(text="(level 8)")
  elif 109<totDmg<132:
    print("Can kill a level nine.")
    cHPInd.configure(text="(level 9)")
  elif 131<totDmg<156:
    print("Can kill a level ten.")
    cHPInd.configure(text="(level 10)")
  elif 155<totDmg<196:
    print("Can kill a level eleven.")
    cHPInd.configure(text="(level 11)")
  elif 195<totDmg<224:
    print("Can kill a level twelve.")
    cHPInd.configure(text="(level 12)")
  elif 223<totDmg<254:
    print("Can kill a level thirteen.")
    cHPInd.configure(text="(level 13)")
  elif 253<totDmg<286:
    print("Can kill a level fourteen.")
    cHPInd.configure(text="(level 14)")
  elif 285<totDmg<320:
    print("Can kill a level fifteen.")
    cHPInd.configure(text="(level 15)")
  elif 319<totDmg<356:
    print("Can kill a level sixteen.")
    cHPInd.configure(text="(level 16)")
  elif 355<totDmg<394:
    print("Can kill a level seventeen.")
    cHPInd.configure(text="(level 17)")
  elif 393<totDmg<434:
    print("Can kill a level eighteen.")
    cHPInd.configure(text="(level 18)")
  elif 433<totDmg<476:
    print("Can kill a level nineteen.")
    cHPInd.configure(text="(level 19)")
  elif 475<totDmg:
    print("Can kill a level twenty.")
    cHPInd.configure(text="(level 20)")
  else:
    print("what the fuck")
    cHPInd.configure(text="(???)")

#Geometry - Main Columns
col1.grid(column=0,row=0,padx=5) #In retrospect I should have used 0 for the column name too, but it doesn't matter *that* much.
col2.grid(column=1,row=0,padx=10)

#Geometry - Toggles
togBtns.grid(column=0,row=1,pady=5)
lurChk.grid(column=0,row=0,padx=5)
orgBtn.grid(column=1,row=0,padx=5)
defLbl.grid(column=2,row=0,padx=0)
defBtn.grid(column=3,row=0)
lockDwn.grid(column=0,row=1)
clrBtn.grid(column=2,row=1,columnspan=2,padx=5)

#Geometry - Gags
gagFrame.grid(column=0,row=2,pady=10)
#Sound
sndFrame.grid(column=0,row=1,)
bHorn.grid(column=0,row=0)
whistle.grid(column=1,row=0)
bugle.grid(column=2,row=0)
aoogah.grid(column=3,row=0)
eTrunk.grid(column=4,row=0)
fHorn.grid(column=5,row=0)
oSinger.grid(column=6,row=0)
#Throw
thrwFrame.grid(column=0,row=2)
cCake.grid(column=0,row=0)
fPSlice.grid(column=1,row=0)
cPSlice.grid(column=2,row=0)
wFPie.grid(column=3,row=0)
wCPie.grid(column=4,row=0)
bCake.grid(column=5,row=0)
wCake.grid(column=6,row=0)
#Squirt
sqrtFrame.grid(column=0,row=3)
sFlower.grid(column=0,row=0)
gWater.grid(column=1,row=0)
sGun.grid(column=2,row=0)
sBottle.grid(column=3,row=0)
fHose.grid(column=4,row=0)
sCloud.grid(column=5,row=0)
geyser.grid(column=6,row=0)
#Drop
drpFrame.grid(column=0,row=4)
fPot.grid(column=0,row=0)
sBag.grid(column=1,row=0)
anvil.grid(column=2,row=0)
bWeight.grid(column=3,row=0)
safe.grid(column=4,row=0)
gPiano.grid(column=5,row=0)
tTanic.grid(column=6,row=0)
#Trap
trpFrame.grid(column=0,row=0)
bPeel.grid(column=0,row=0)
rake.grid(column=1,row=0)
marbles.grid(column=2,row=0)
qSand.grid(column=3,row=0)
tDoor.grid(column=4,row=0)
tnt.grid(column=5,row=0)
rRoad.grid(column=6,row=0)

#Geometry - Calculation History
hist.grid(column=0,row=0)
histLbl.grid(column=0,row=0)
histBox.grid(column=0,row=1)
clrHistBtn.grid(column=0,row=2,pady=3)
pinBtn.grid(column=0,row=3,pady=3)
cogClc.grid(column=0,row=4,pady=3)

#Geometry - Calculation Results
clcResults.grid(column=0,row=0)
dmgThsRnd.grid(column=0,row=0)
theDmg.grid(column=1,row=0)
cHPInd.grid(column=2,row=0)
orgOnOff.grid(column=0,row=1,columnspan=3)

#Run
window.mainloop()