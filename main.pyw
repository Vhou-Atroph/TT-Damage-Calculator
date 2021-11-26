from tkinter import *
import math
import os

'''VERSION 1.1.1

CONTRIBUTORS:
- Vhou-Atroph
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
global organic
global sndUsed
global trwUsed
global sqtUsed
global drpUsed
global trpUsed
global totDmg
lured=IntVar()
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

#Toggles
togBtns=Frame(col1)
orgBtn=Button(togBtns,text='Toggle Organic')
lurChk=Checkbutton(togBtns,text='Cog lured',variable=lured,onvalue=1,offvalue=0)
clrBtn=Button(togBtns,text='Clear Inputs')
clcBtn=Button(togBtns,text='Calculate',font=('Arial',10,'bold'))
emptLbl=Label(togBtns)

#The Gags
gagFrame=Frame(col1)
#Sound
sndFrame=Frame(gagFrame)
bHornImg=PhotoImage(file='img/bike-horn.png')
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
#Throw
thrwFrame=Frame(gagFrame)
cCakeImg=PhotoImage(file='img/cupcake.png')
cCake=Button(thrwFrame,image=cCakeImg)
fPSliceImg=PhotoImage(file='img/fruit-pie-slice.png')
fPSlice=Button(thrwFrame,image=fPSliceImg)
cPSliceImg=PhotoImage(file='img/cream-pie-slice.png')
cPSlice=Button(thrwFrame,image=cPSliceImg)
wFPieImg=PhotoImage(file='img/whole-fruit-pie.png')
wFPie=Button(thrwFrame,image=wFPieImg)
wCPieImg=PhotoImage(file='img/whole-cream-pie.png')
wCPie=Button(thrwFrame,image=wCPieImg)
bCakeImg=PhotoImage(file='img/birthday-cake.png')
bCake=Button(thrwFrame,image=bCakeImg)
wCakeImg=PhotoImage(file='img/wedding-cake.png')
wCake=Button(thrwFrame,image=wCakeImg)
#Squirt
sqrtFrame=Frame(gagFrame)
sFlowerImg=PhotoImage(file='img/squirting-flower.png')
sFlower=Button(sqrtFrame,image=sFlowerImg)
gWaterImg=PhotoImage(file='img/glass-of-water.png')
gWater=Button(sqrtFrame,image=gWaterImg)
sGunImg=PhotoImage(file='img/squirt-gun.png')
sGun=Button(sqrtFrame,image=sGunImg)
sBottleImg=PhotoImage(file='img/seltzer-bottle.png')
sBottle=Button(sqrtFrame,image=sBottleImg)
fHoseImg=PhotoImage(file='img/fire-hose.png')
fHose=Button(sqrtFrame,image=fHoseImg)
sCloudImg=PhotoImage(file='img/storm-cloud.png')
sCloud=Button(sqrtFrame,image=sCloudImg)
geyserImg=PhotoImage(file='img/geyser.png')
geyser=Button(sqrtFrame,image=geyserImg)
#Drop
drpFrame=Frame(gagFrame)
fPotImg=PhotoImage(file='img/flower-pot.png')
fPot=Button(drpFrame,image=fPotImg)
sBagImg=PhotoImage(file='img/sandbag.png')
sBag=Button(drpFrame,image=sBagImg)
anvilImg=PhotoImage(file='img/anvil.png')
anvil=Button(drpFrame,image=anvilImg)
bWeightImg=PhotoImage(file='img/big-weight.png')
bWeight=Button(drpFrame,image=bWeightImg)
safeImg=PhotoImage(file='img/safe.png')
safe=Button(drpFrame,image=safeImg)
gPianoImg=PhotoImage(file='img/grand-piano.png')
gPiano=Button(drpFrame,image=gPianoImg)
tTanicImg=PhotoImage(file='img/toontanic.png')
tTanic=Button(drpFrame,image=tTanicImg)
#Trap!
trpFrame=Frame(gagFrame)
bPeelImg=PhotoImage(file='img/banana-peel.png')
bPeel=Button(trpFrame,image=bPeelImg)
rakeImg=PhotoImage(file='img/rake.png')
rake=Button(trpFrame,image=rakeImg)
marblesImg=PhotoImage(file='img/marbles.png')
marbles=Button(trpFrame,image=marblesImg)
qSandImg=PhotoImage(file='img/quicksand.png')
qSand=Button(trpFrame,image=qSandImg)
tDoorImg=PhotoImage(file='img/trapdoor.png')
tDoor=Button(trpFrame,image=tDoorImg)
tntImg=PhotoImage(file='img/tnt.png')
tnt=Button(trpFrame,image=tntImg)
rRoadImg=PhotoImage(file='img/railroad.png')
rRoad=Button(trpFrame,image=rRoadImg)

#Button list - used for mass configuring the gag buttons
gagBtns=(bHorn,whistle,bugle,aoogah,eTrunk,fHorn,oSinger,cCake,fPSlice,cPSlice,wFPie,wCPie,bCake,wCake,sFlower,gWater,sGun,sBottle,fHose,sCloud,geyser,fPot,sBag,anvil,bWeight,safe,gPiano,tTanic,bPeel,rake,marbles,qSand,tDoor,tnt,rRoad)

#Calculation history
hist=Frame(col2)
histLbl=Label(hist,text="History")
histBox=Text(hist,width=25,height=18,state=DISABLED,font=('Arial',10,'normal'),wrap=WORD)
clrHistBtn=Button(hist,text="Clear History")
cogClc=Button(hist,text="Cog Health Info")

#Calculation results
clcResults=Frame(col1)
dmgThsRnd=Label(clcResults,text="Damage this round:",font=('Arial',16,'normal'))
theDmg=Label(clcResults,text="0",font=('Arial',16,'bold'))

#Toggle organic functions
def togOrgOff():
  global organic
  organic=0
  print("Gags in calculations will no longer be organic!")
  orgBtn.configure(command=togOrgOn)
  for i in gagBtns:
    i.configure(bg='SystemButtonFace',activebackground='SystemButtonFace')
def togOrgOn():
  global organic
  organic=1
  print("Gags in calculations will now be organic!")
  orgBtn.configure(command=togOrgOff)
  for i in gagBtns:
    i.configure(bg='darkorange',activebackground='orange')
orgBtn.configure(command=togOrgOn)

#Clear inputs function
def clearInputs():
  print("Clearing gag inputs!")
  global lured
  global sndUsed
  global trwUsed
  global sqtUsed
  global drpUsed
  global trpUsed
  lured.set(0)
  sndUsed=list()
  trwUsed=list()
  sqtUsed=list()
  drpUsed=list()
  trpUsed=list()
  togOrgOff()
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
    sndUsed.append(4)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Bike Horn (4)\n")
    histBox.configure(state=DISABLED)
  else:
    sndUsed.append(5)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Bike Horn (5)\n")
    histBox.configure(state=DISABLED)
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
    histBox.insert('1.0',"Gag used: Organic Bugle (5)\n")
    histBox.configure(state=DISABLED)
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
eTrunk.configure(command=eTrunkPrs)
def fHornPrs():
  if organic==0:
    sndUsed.append(50)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Foghorn (50)\n")
    histBox.configure(state=DISABLED)
  else:
    sndUsed.append(5)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Foghorn (55)\n")
    histBox.configure(state=DISABLED)
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
bWeight.configure(command=bWeightPrs)
def safePrs():
  if organic==0:
    drpUsed.append(60)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Safe (60)\n")
    histBox.configure(state=DISABLED)
  else:
    drpUsed.append(66)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Safe (66)\n")
    histBox.configure(state=DISABLED)
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
rake.configure(command=rakePrs)
def marblesPrs():
  if organic==0:
    trpUsed.append(30)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Marbles (30)\n")
    histBox.configure(state=DISABLED)
  else:
    trpUsed.append(22)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Marbles (33)\n")
    histBox.configure(state=DISABLED)
marbles.configure(command=marblesPrs)
def qSandPrs():
  if organic==0:
    trpUsed.append(50)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Quicksand (50)\n")
    histBox.configure(state=DISABLED)
  else:
    trpUsed.append(22)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Quicksand (55)\n")
    histBox.configure(state=DISABLED)
qSand.configure(command=qSandPrs)
def tDoorPrs():
  if organic==0:
    trpUsed.append(70)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Trapdoor (70)\n")
    histBox.configure(state=DISABLED)
  else:
    trpUsed.append(77)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Trapdoor (77)\n")
    histBox.configure(state=DISABLED)
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
tnt.configure(command=tntPrs)
def rRoadPrs():
  if organic==0:
    trpUsed.append(195)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Railroad (195)\n")
    histBox.configure(state=DISABLED)
  else:
    trpUsed.append(214)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Railroad (214)\n")
    histBox.configure(state=DISABLED)
rRoad.configure(command=rRoadPrs)

#Sound damage calculation
def sndDmgClc():
  print("Damage of each individual sound gag: "+str(sndUsed))
  global lured
  lured.set(0)
  print("If cogs were lured, they aren't anymore! Don't use sound on lured cogs!")
  if len(sndUsed)>1:
    totSndDmg=sum(sndUsed,0)
    totSndDmg=totSndDmg+math.ceil((totSndDmg*0.2)) #Group damage bonus always rounds up. See: 3 fogs and 1 aoogah getting rid of level 12 cogs. This does 199.2 damage, but still works.
  else:
    totSndDmg=sndUsed[0]
  print("Total sound damage: "+str(totSndDmg))
  global totDmg
  totDmg=totDmg+totSndDmg

#Throw damage calculation
def trwDmgClc():
  print("Damage of each individual throw gag:"+str(trwUsed))
  global lured
  if lured.get()==0:
    print("The cogs are not lured, and there will be no 50% damage bonus.")
    if len(trwUsed)>1:
      totTrwDmg=sum(trwUsed,0)
      totTrwDmg=totTrwDmg+math.ceil((totTrwDmg*0.2))
    else:
      totTrwDmg=trwUsed[0]
  else:
    print("The cogs are lured, and there will be a 50% damage bonus.") #Lure bonus doesn't get rounded for some dumb reason.
    if len(trwUsed)>1:
      totTrwDmg=sum(trwUsed,0)
      totTrwDmg=totTrwDmg+(totTrwDmg/2)+math.ceil((totTrwDmg*0.2))
    else:
      totTrwDmg=trwUsed[0]+(trwUsed[0]/2)
    lured.set(0)
  print("Total throw damage: "+str(totTrwDmg))
  global totDmg
  totDmg=totDmg+totTrwDmg

#Squirt damage calculation, luckily just throw 2. (Squirt is better than throw and I am tired of people pretending it isn't. It's the superior organic choice. Cowards.)
def sqtDmgClc():
  print("Damage of each individual squirt gag:"+str(sqtUsed))
  global lured
  if lured.get()==0:
    print("The cogs are not lured, and there will be no 50% damage bonus.")
    if len(sqtUsed)>1:
      totSqtDmg=sum(sqtUsed,0)
      totSqtDmg=totSqtDmg+math.ceil((totSqtDmg*0.2))
    else:
      totSqtDmg=sqtUsed[0]
  else:
    print("The cogs are lured, and there will be a 50% damage bonus.")
    if len(sqtUsed)>1:
      totSqtDmg=sum(sqtUsed,0)
      totSqtDmg=totSqtDmg+(totSqtDmg/2)+math.ceil((totSqtDmg*0.2))
    else:
      totSqtDmg=sqtUsed[0]+(sqtUsed[0]/2)
    lured.set(0)
  print("Total squirt damage: "+str(totSqtDmg))
  global totDmg
  totDmg=totDmg+totSqtDmg

#Drop damage calculation
def drpDmgClc():
  print("Damage of each individual drop gag:"+str(drpUsed))
  global lured
  if lured.get()==0:
    print("The cogs are not lured, so drop is able to hit!")
    if len(drpUsed)>1:
      totDrpDmg=sum(drpUsed,0)
      totDrpDmg=totDrpDmg+math.ceil((totDrpDmg*0.2))
    else:
      totDrpDmg=drpUsed[0]
  else:
    print("The cogs are lured, and drop does not work on lured cogs! https://www.youtube.com/watch?v=NV-p_-OvUnA&t=4s")
    totDrpDmg=0
  print("Total drop damage: "+str(totDrpDmg))
  global totDmg
  totDmg=totDmg+totDrpDmg

#Trap damage calculation
def trpDmgClc():
  print("Damage of each individual trap gag:"+str(trpUsed))
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
      totTrpDmg=trpUsed[0]
      lured.set(0)
  global totDmg
  totDmg=totDmg+totTrpDmg

#Total damage calculation
def clcDmg():
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
  histBox.configure(state=NORMAL)
  histBox.insert('1.0',"--------\nDamage calculated: "+str(totDmg)+"\n--------\n")
  histBox.configure(state=DISABLED)
  totDmg=0
  clearInputs()
  
clcBtn.configure(command=clcDmg)

#Geometry - Main Columns
col1.grid(column=0,row=0,padx=5) #In retrospect I should have used 0 for the column name too, but it doesn't matter *that* much.
col2.grid(column=1,row=0,padx=10)

#Geometry - Toggles
togBtns.grid(column=0,row=1,pady=10)
lurChk.grid(column=0,row=0,padx=5)
orgBtn.grid(column=1,row=0,padx=5)
clrBtn.grid(column=2,row=0,padx=5)
clcBtn.grid(column=4,row=0,padx=5)
emptLbl.grid(column=3,row=0,padx=15)

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
clrHistBtn.grid(column=0,row=2,pady=5)
cogClc.grid(column=0,row=3)

#Geometry - Calculation Results
clcResults.grid(column=0,row=0)
dmgThsRnd.grid(column=0,row=0)
theDmg.grid(column=1,row=0)

#Cog HP Calculator
def cHPClc():
  os.startfile(os.getcwd()+"/docs/coghp.html")
cogClc.configure(command=cHPClc)
#Run
window.mainloop()