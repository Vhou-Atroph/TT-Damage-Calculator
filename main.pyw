from tkinter import *
import math
import os

'''VERSION you figure it out, vhou

CONTRIBUTORS:
- Vhou-Atroph
- BoggoTV
- SkylimeTime
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
#Virtually everything involving v2 Cogs was initially implemented by Sky, not Vhou!
#If something goes wrong or looks really dumb, blame them instead please thank you .,. - Sky
global v2Snd
global v2Trw
global v2Sqt
global v2Drp
global v2Trp
global v2Dmg
v2Snd=list()
v2Trw=list()
v2Sqt=list()
v2Drp=list()
v2Trp=list()
v2Dmg=0
global isV2
isV2 = False
lvlKilled=0
v2Killed=0
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
  global v2Dmg
  global isV2
  if localLure==1:
    lured.set(1)
  if isV2:
    #print("V2: "+str(v2Dmg))
    v2TheDmg.configure(text=str(v2Dmg))
    v2CHPIndClc()
    v2Dmg=0
  else:
    #print("Total damage this round: "+str(totDmg))
    theDmg.configure(text=str(totDmg))
    cHPIndClc()
    totDmg=0

#Prepare damage calculation for V2.0 Cogs
#This function loops itself several times, so that way you don't have to click a button to check individual 2.0 levels!
#But in return this makes damage dealt to 2.0 Cogs display a little strangly at times. Sorry! The level it can beat can be trusted, though. I hope.
#Currently built off of the in development BBHQ changes TTR had announced on 3/11/2022. This is subject to change at any time, and as of 3/14/2022 is unknown when it will release.
def v2Clc(level):
  global v2Dmg
  global isV2
  global v2Snd
  global v2Trw
  global v2Sqt
  global v2Drp
  global v2Trp
  v2Snd = list()
  v2Trw = list()
  v2Sqt = list()
  v2Drp = list()
  v2Trp = list()
  defense = level*2
  for index in range(0, len(sndUsed)):
    newDam = sndUsed[index] - defense
    if newDam < 0:
      newDam = 0
    v2Snd.append(newDam)
  for index in range(0, len(trwUsed)):
    newDam = trwUsed[index] - defense
    if newDam < 0:
      newDam = 0
    v2Trw.append(newDam)
  for index in range(0, len(sqtUsed)):
    newDam = sqtUsed[index] - defense
    if newDam < 0:
      newDam = 0
    v2Sqt.append(newDam)
  for index in range(0, len(drpUsed)):
    newDam = drpUsed[index] - defense
    if newDam < 0:
      newDam = 0
    v2Drp.append(newDam)
  for index in range(0, len(trpUsed)):
    newDam = trpUsed[index] - defense
    if newDam < 0:
      newDam = 0
    v2Trp.append(newDam)
  isV2 = True
  v2Dmg = 0
  clcDmg()
  isV2 = False

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
bHorn=Button(sndFrame,image=bHornImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
whistleImg=PhotoImage(file='img/whistle.png')
whistle=Button(sndFrame,image=whistleImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
bugleImg=PhotoImage(file='img/bugle.png')
bugle=Button(sndFrame,image=bugleImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
aoogahImg=PhotoImage(file='img/aoogah.png')
aoogah=Button(sndFrame,image=aoogahImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
eTrunkImg=PhotoImage(file='img/elephant-trunk.png')
eTrunk=Button(sndFrame,image=eTrunkImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
fHornImg=PhotoImage(file='img/fog-horn.png')
fHorn=Button(sndFrame,image=fHornImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
oSingerImg=PhotoImage(file='img/opera-singer.png')
oSinger=Button(sndFrame,image=oSingerImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
#Throw
thrwFrame=Frame(gagFrame)
cCakeImg=PhotoImage(file='img/cupcake.png')
cCake=Button(thrwFrame,image=cCakeImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
fPSliceImg=PhotoImage(file='img/fruit-pie-slice.png')
fPSlice=Button(thrwFrame,image=fPSliceImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
cPSliceImg=PhotoImage(file='img/cream-pie-slice.png')
cPSlice=Button(thrwFrame,image=cPSliceImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
wFPieImg=PhotoImage(file='img/whole-fruit-pie.png')
wFPie=Button(thrwFrame,image=wFPieImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
wCPieImg=PhotoImage(file='img/whole-cream-pie.png')
wCPie=Button(thrwFrame,image=wCPieImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
bCakeImg=PhotoImage(file='img/birthday-cake.png')
bCake=Button(thrwFrame,image=bCakeImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
wCakeImg=PhotoImage(file='img/wedding-cake.png')
wCake=Button(thrwFrame,image=wCakeImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
#Squirt
sqrtFrame=Frame(gagFrame)
sFlowerImg=PhotoImage(file='img/squirting-flower.png')
sFlower=Button(sqrtFrame,image=sFlowerImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
gWaterImg=PhotoImage(file='img/glass-of-water.png')
gWater=Button(sqrtFrame,image=gWaterImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
sGunImg=PhotoImage(file='img/squirt-gun.png')
sGun=Button(sqrtFrame,image=sGunImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
sBottleImg=PhotoImage(file='img/seltzer-bottle.png')
sBottle=Button(sqrtFrame,image=sBottleImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
fHoseImg=PhotoImage(file='img/fire-hose.png')
fHose=Button(sqrtFrame,image=fHoseImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
sCloudImg=PhotoImage(file='img/storm-cloud.png')
sCloud=Button(sqrtFrame,image=sCloudImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
geyserImg=PhotoImage(file='img/geyser.png')
geyser=Button(sqrtFrame,image=geyserImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
#Drop
drpFrame=Frame(gagFrame)
fPotImg=PhotoImage(file='img/flower-pot.png')
fPot=Button(drpFrame,image=fPotImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
sBagImg=PhotoImage(file='img/sandbag.png')
sBag=Button(drpFrame,image=sBagImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
anvilImg=PhotoImage(file='img/anvil.png')
anvil=Button(drpFrame,image=anvilImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
bWeightImg=PhotoImage(file='img/big-weight.png')
bWeight=Button(drpFrame,image=bWeightImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
safeImg=PhotoImage(file='img/safe.png')
safe=Button(drpFrame,image=safeImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
gPianoImg=PhotoImage(file='img/grand-piano.png')
gPiano=Button(drpFrame,image=gPianoImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
tTanicImg=PhotoImage(file='img/toontanic.png')
tTanic=Button(drpFrame,image=tTanicImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
#Trap!
trpFrame=Frame(gagFrame)
bPeelImg=PhotoImage(file='img/banana-peel.png')
bPeel=Button(trpFrame,image=bPeelImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
rakeImg=PhotoImage(file='img/rake.png')
rake=Button(trpFrame,image=rakeImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
marblesImg=PhotoImage(file='img/marbles.png')
marbles=Button(trpFrame,image=marblesImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
qSandImg=PhotoImage(file='img/quicksand.png')
qSand=Button(trpFrame,image=qSandImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
tDoorImg=PhotoImage(file='img/trapdoor.png')
tDoor=Button(trpFrame,image=tDoorImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
tntImg=PhotoImage(file='img/tnt.png')
tnt=Button(trpFrame,image=tntImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
rRoadImg=PhotoImage(file='img/railroad.png')
rRoad=Button(trpFrame,image=rRoadImg,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')

#Button list - used for mass configuring the gag buttons
gagBtns=(bHorn,whistle,bugle,aoogah,eTrunk,fHorn,oSinger,cCake,fPSlice,cPSlice,wFPie,wCPie,bCake,wCake,sFlower,gWater,sGun,sBottle,fHose,sCloud,geyser,fPot,sBag,anvil,bWeight,safe,gPiano,tTanic,bPeel,rake,marbles,qSand,tDoor,tnt,rRoad)

#Calculation history
hist=Frame(col2)
histLbl=Label(hist,text="History")
histBox=Text(hist,width=25,height=22,state=DISABLED,font=('Arial',10,'normal'),wrap=WORD)
pinBtn=Button(hist,text="Pin to top")
clrHistBtn=Button(hist,text="Clear History")
cogClc=Button(hist,text="Show Health and\n SOS Cards")

#Calculation results
clcResults=Frame(col1)
dmgThsRnd=Label(clcResults,text="Damage this round:",font=('Arial',16,'normal'))
theDmg=Label(clcResults,text="0",font=('Arial',16,'bold'))
cHPInd=Label(clcResults,text="(level 0)",font=('Arial',8,'normal'))
orgOnOff=Label(clcResults,text="Organic = OFF",font=('Arial',10,'bold'))
v2Results=Frame(col1) #hope i got this right!
#if not, sorry vhou, this part's beyond me. please take it from here!
v2DmgThsRnd=Label(v2Results,text="V2 damage*:",font=('Arial',16,'normal'))
v2TheDmg=Label(v2Results,text="0",font=('Arial',16,'bold'))
v2CHPInd=Label(v2Results,text="(level 0)",font=('Arial',8,'normal'))

#Cog HP
cogHPSheet=Frame(window)
cogHPImg=PhotoImage(file='img/coghp.png')
cogHPLbl=Label(cogHPSheet,image=cogHPImg)

#SOS Cards
sosCards=Frame(window)
sosTrp=Frame(sosCards)
clrkWillImg=PhotoImage(file='img/clerkwill.png')
clrkWill=Button(sosTrp,image=clrkWillImg)
clrkPennyImg=PhotoImage(file='img/clerkpenny.png')
clrkPenny=Button(sosTrp,image=clrkPennyImg)
clrkClaraImg=PhotoImage(file='img/clerkclara.png')
clrkClara=Button(sosTrp,image=clrkClaraImg)
sosSnd=Frame(sosCards)
barbImg=PhotoImage(file='img/barbaraseville.png')
barb=Button(sosSnd,image=barbImg)
sidImg=PhotoImage(file='img/sidsonata.png')
sid=Button(sosSnd,image=sidImg)
moeImg=PhotoImage(file='img/moezart.png')
moe=Button(sosSnd,image=moeImg)
sosDrp=Frame(sosCards)
nedImg=PhotoImage(file='img/clumsyned.png')
ned=Button(sosDrp,image=nedImg)
franzImg=PhotoImage(file='img/franzneckvein.png')
franz=Button(sosDrp,image=franzImg)
bessImg=PhotoImage(file='img/barnaclebessie.png')
bess=Button(sosDrp,image=bessImg)

#Toggle organic functions
def togOrgOff(opt=""):
  global organic
  organic=0
  #print("Gags in calculations will no longer be organic!")
  orgBtn.configure(command=togOrgOn)
  orgOnOff.configure(text="Organic = OFF")
  for i in gagBtns:
    i.configure(bg='#1888D3',activebackground='#186AD3')
  window.bind('<Shift_L>',togOrgOn)
def togOrgOn(opt=""):
  global organic
  organic=1
  #print("Gags in calculations will now be organic!")
  orgBtn.configure(command=togOrgOff)
  orgOnOff.configure(text="Organic = ON")
  for i in gagBtns:
    i.configure(bg='darkorange',activebackground='orange')
  window.bind('<Shift_L>',togOrgOff)
orgBtn.configure(command=togOrgOn)
window.bind('<Shift_L>',togOrgOn)

#Def Keybind
def defSwap(opt=""):
  global dmgDown
  if dmgDown.get()=='0%':
    dmgDown.set('10%')
    clcDmg()
  elif dmgDown.get()=='10%':
    dmgDown.set('15%')
    clcDmg()
  elif dmgDown.get()=='15%':
    dmgDown.set('20%')
    clcDmg()
  else:
    dmgDown.set('0%')
    clcDmg()
window.bind('<Control-d>',defSwap)

#Lure Keybind
def lureSwap(opt=""):
  if lured.get()==0:
    lured.set(1)
    clcDmg()
  else:
    lured.set(0)
    clcDmg()
window.bind('<Control-l>',lureSwap)

#Clear inputs function
def clearInputs(opt=""):
  #print("Clearing gag inputs!")
  global lured
  global dmgDown
  global dlLock
  global sndUsed
  global trwUsed
  global sqtUsed
  global drpUsed
  global trpUsed
  global v2Snd
  global v2Trw
  global v2Sqt
  global v2Drp
  global v2Trp
  global isV2
  localLure=0
  lurInfo='no'
  if lured.get()==1: #Find out if lure is enabled. If it is, save a local variable.
    localLure=1
    lurInfo='yes'
  histBox.configure(state=NORMAL)
  histBox.insert('1.0',"--------\nCalculation finished!\nDamage calculated was: "+theDmg.cget("text")+"\n2.0 "+ v2CHPInd.cget("text") +" damage*: "+v2TheDmg.cget("text")+"\nDefense: "+dmgDown.get()+"\nLure: "+lurInfo+"\n\n")
  histBox.configure(state=DISABLED)
  if dlLock.get()=='No lock' or dlLock.get()=='Lock lure':
    dmgDown.set('0%')
  lured.set(0)
  sndUsed=list()
  trwUsed=list()
  sqtUsed=list()
  drpUsed=list()
  trpUsed=list()
  v2Snd=list()
  v2Trw=list()
  v2Sqt=list()
  v2Drp=list()
  v2Trp=list()
  togOrgOff()
  clcDmg()
  isV2 = True
  clcDmg() 
  isV2 = False
  for i in gagBtns:
    i.configure(text='0')
  if localLure==1 and dlLock.get()=='Lock lure' or dlLock.get()=='Lock both': #Use the local variable and dlLock to lock lure as active even after it is set to 0 by clearInputs()
    lured.set(1)
clrBtn.configure(command=clearInputs)
window.bind('<Control-r>',clearInputs)

#Clear history function
def clearHistory():
  #print("Clearing calculcation history!")
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
  bHorn.configure(text=int(bHorn.cget("text"))+1)
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
  whistle.configure(text=int(whistle.cget("text"))+1)
  clcDmg()
whistle.configure(command=whistlePrs)
def buglePrs():
  if organic==0:
    sndUsed.append(11)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Bugle (11)\n")
    histBox.configure(state=DISABLED)
  else:
    sndUsed.append(12)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Bugle (12)\n")
    histBox.configure(state=DISABLED)
  bugle.configure(text=int(bugle.cget("text"))+1)
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
  aoogah.configure(text=int(aoogah.cget("text"))+1)
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
  eTrunk.configure(text=int(eTrunk.cget("text"))+1)
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
  fHorn.configure(text=int(fHorn.cget("text"))+1)
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
  oSinger.configure(text=int(oSinger.cget("text"))+1)
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
  cCake.configure(text=int(cCake.cget("text"))+1)
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
  fPSlice.configure(text=int(fPSlice.cget("text"))+1)
  clcDmg()
fPSlice.configure(command=fPSlicePrs)
def cPSlicePrs():
  if organic==0:
    trwUsed.append(17)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Cream Pie Slice (17)\n")
    histBox.configure(state=DISABLED)
  else:
    trwUsed.append(18)
    histBox.configure(state=NORMAL)
    histBox.insert('1.0',"Gag used: Organic Cream Pie Slice (18)\n")
    histBox.configure(state=DISABLED)
  cPSlice.configure(text=int(cPSlice.cget("text"))+1)
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
  wFPie.configure(text=int(wFPie.cget("text"))+1)
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
  wCPie.configure(text=int(wCPie.cget("text"))+1)
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
  bCake.configure(text=int(bCake.cget("text"))+1)
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
  wCake.configure(text=int(wCake.cget("text"))+1)
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
    histBox.insert('1.0',"Gag used: Organic Squirting Flower (5)\n")
    histBox.configure(state=DISABLED)
  sFlower.configure(text=int(sFlower.cget("text"))+1)
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
  gWater.configure(text=int(gWater.cget("text"))+1)
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
  sGun.configure(text=int(sGun.cget("text"))+1)
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
  sBottle.configure(text=int(sBottle.cget("text"))+1)
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
  fHose.configure(text=int(fHose.cget("text"))+1)
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
    #print("Hey did you know an organic storm cloud can kill a lured level 10? Organic squirt is cooler than organic throw but most people keep lying to themselves about the true superior organic track.")
  sCloud.configure(text=int(sCloud.cget("text"))+1)
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
  geyser.configure(text=int(geyser.cget("text"))+1)
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
  fPot.configure(text=int(fPot.cget("text"))+1)
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
  sBag.configure(text=int(sBag.cget("text"))+1)
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
  anvil.configure(text=int(anvil.cget("text"))+1)
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
  bWeight.configure(text=int(bWeight.cget("text"))+1)
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
  safe.configure(text=int(safe.cget("text"))+1)
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
  gPiano.configure(text=int(gPiano.cget("text"))+1)
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
  tTanic.configure(text=int(tTanic.cget("text"))+1)
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
  bPeel.configure(text=int(bPeel.cget("text"))+1)
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
  rake.configure(text=int(rake.cget("text"))+1)
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
  marbles.configure(text=int(marbles.cget("text"))+1)
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
  qSand.configure(text=int(qSand.cget("text"))+1)
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
  tDoor.configure(text=int(tDoor.cget("text"))+1)
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
  tnt.configure(text=int(tnt.cget("text"))+1)
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
  rRoad.configure(text=int(rRoad.cget("text"))+1)
  clcDmg()
rRoad.configure(command=rRoadPrs)

#SOS Cards
def claraPrs():
  trpUsed.append(180)
  histBox.configure(state=NORMAL)
  histBox.insert('1.0',"Gag used: Clerk Clara (180)\n")
  histBox.configure(state=DISABLED)
  clcDmg()
clrkClara.configure(command=claraPrs)
def pennyPrs():
  trpUsed.append(120)
  histBox.configure(state=NORMAL)
  histBox.insert('1.0',"Gag used: Clerk Penny (120)\n")
  histBox.configure(state=DISABLED)
  clcDmg()
clrkPenny.configure(command=pennyPrs)
def willPrs():
  trpUsed.append(60)
  histBox.configure(state=NORMAL)
  histBox.insert('1.0',"Gag used: Clerk Will (60)\n")
  histBox.configure(state=DISABLED)
  clcDmg()
clrkWill.configure(command=willPrs)
def moePrs():
  sndUsed.append(75)
  histBox.configure(state=NORMAL)
  histBox.insert('1.0',"Gag used: Moe Zart (75)\n")
  histBox.configure(state=DISABLED)
  clcDmg()
moe.configure(command=moePrs)
def sidPrs():
  sndUsed.append(55)
  histBox.configure(state=NORMAL)
  histBox.insert('1.0',"Gag used: Sid Sonata (55)\n")
  histBox.configure(state=DISABLED)
  clcDmg()
sid.configure(command=sidPrs)
def barbPrs():
  sndUsed.append(35)
  histBox.configure(state=NORMAL)
  histBox.insert('1.0',"Gag used: Barbara Seville (35)\n")
  histBox.configure(state=DISABLED)
  clcDmg()
barb.configure(command=barbPrs)
def bessPrs():
  drpUsed.append(170)
  histBox.configure(state=NORMAL)
  histBox.insert('1.0',"Gag used: Barnacle Bessie (170)\n")
  histBox.configure(state=DISABLED)
  clcDmg()
bess.configure(command=bessPrs)
def franzPrs():
  drpUsed.append(100)
  histBox.configure(state=NORMAL)
  histBox.insert('1.0',"Gag used: Franz Neckvein (100)\n")
  histBox.configure(state=DISABLED)
  clcDmg()
franz.configure(command=franzPrs)
def nedPrs():
  drpUsed.append(60)
  histBox.configure(state=NORMAL)
  histBox.insert('1.0',"Gag used: Clumsy Ned (60)\n")
  histBox.configure(state=DISABLED)
  clcDmg()
ned.configure(command=nedPrs)

#Sound damage calculation
def sndDmgClc():
  global isV2
  localDmg=list()
  if isV2:
    localSndUsed=v2Snd
  else:
    localSndUsed=sndUsed
  if dmgDown.get()=='10%':
    for i in range(len(localSndUsed)):
      localDmg.append(localSndUsed[i]-math.ceil(localSndUsed[i]*.1)) #Defense buff ceils
  elif dmgDown.get()=='15%':
    for i in range(len(localSndUsed)):
      localDmg.append(localSndUsed[i]-math.ceil(localSndUsed[i]*.15))
  elif dmgDown.get()=='20%':
    for i in range(len(localSndUsed)):
      localDmg.append(localSndUsed[i]-math.ceil(localSndUsed[i]*.2))
  else:
    for i in range(len(localSndUsed)):
      localDmg.append(localSndUsed[i])
  #print("Damage of each individual sound gag: "+str(localDmg))
  global lured
  lured.set(0)
  #print("If cogs were lured, they aren't anymore! Don't use sound on lured cogs!")
  totSndDmg=sum(localDmg,0)
  if len(localSndUsed)>1:
    totSndDmg=totSndDmg+math.ceil((totSndDmg*0.2)) #Group damage bonus always rounds up. See: 3 fogs and 1 aoogah getting rid of level 12 cogs. This does 199.2 damage, but still works.
  #print("Total sound damage: "+str(totSndDmg))
  if isV2:
    global v2Dmg
    v2Dmg=v2Dmg+totSndDmg
  else:
    global totDmg
    totDmg=totDmg+totSndDmg

#Throw damage calculation
def trwDmgClc():
  global isV2
  localDmg=list()
  if isV2:
    localTrwUsed=v2Trw
  else:
    localTrwUsed=trwUsed
  if dmgDown.get()=='10%':
    for i in range(len(localTrwUsed)):
      localDmg.append(localTrwUsed[i]-math.ceil(localTrwUsed[i]*.1))
  elif dmgDown.get()=='15%':
    for i in range(len(localTrwUsed)):
      localDmg.append(localTrwUsed[i]-math.ceil(localTrwUsed[i]*.15))
  elif dmgDown.get()=='20%':
    for i in range(len(localTrwUsed)):
      localDmg.append(localTrwUsed[i]-math.ceil(localTrwUsed[i]*.2))
  else:
    for i in range(len(localTrwUsed)):
      localDmg.append(localTrwUsed[i])
  #print("Damage of each individual throw gag:"+str(localDmg))
  totTrwDmg=sum(localDmg,0)
  global lured
  if lured.get()==0:
    #print("The cogs are not lured, and there will be no 50% damage bonus.")
    if len(localTrwUsed)>1:
      totTrwDmg=totTrwDmg+math.ceil((totTrwDmg*0.2))
  else:
    #print("The cogs are lured, and there will be a 50% damage bonus.") #Lure bonus used to not ceil but does now apparently (TTR V3.0.8).
    if len(localTrwUsed)>1:
      totTrwDmg=totTrwDmg+math.ceil(totTrwDmg/2)+math.ceil((totTrwDmg*0.2))
    else:
      totTrwDmg=totTrwDmg+math.ceil(totTrwDmg/2)
    lured.set(0)
  #print("Total throw damage: "+str(totTrwDmg))
  if isV2:
    global v2Dmg
    v2Dmg=v2Dmg+totTrwDmg
  else:
    global totDmg
    totDmg=totDmg+totTrwDmg

#Squirt damage calculation, luckily just throw 2. (Squirt is better than throw and I am tired of people pretending it isn't. It's the superior organic choice. Cowards.)
def sqtDmgClc():
  global isV2
  localDmg=list()
  if isV2:
    localSqtUsed=v2Sqt
  else:
    localSqtUsed=sqtUsed
  if dmgDown.get()=='10%':
    for i in range(len(localSqtUsed)):
      localDmg.append(localSqtUsed[i]-math.ceil(localSqtUsed[i]*.1))
  elif dmgDown.get()=='15%':
    for i in range(len(localSqtUsed)):
      localDmg.append(localSqtUsed[i]-math.ceil(localSqtUsed[i]*.15))
  elif dmgDown.get()=='20%':
    for i in range(len(localSqtUsed)):
      localDmg.append(localSqtUsed[i]-math.ceil(localSqtUsed[i]*.2))
  else:
    for i in range(len(localSqtUsed)):
      localDmg.append(localSqtUsed[i])
  #print("Damage of each individual squirt gag:"+str(localDmg))
  totSqtDmg=sum(localDmg,0)
  global lured
  if lured.get()==0:
    #print("The cogs are not lured, and there will be no 50% damage bonus.")
    if len(localSqtUsed)>1:
      totSqtDmg=totSqtDmg+math.ceil((totSqtDmg*0.2))
  else:
    #print("The cogs are lured, and there will be a 50% damage bonus.") #Lure bonus doesn't get rounded for some dumb reason.
    if len(localSqtUsed)>1:
      totSqtDmg=totSqtDmg+math.ceil(totSqtDmg/2)+math.ceil((totSqtDmg*0.2))
    else:
      totSqtDmg=totSqtDmg+math.ceil(totSqtDmg/2)
    lured.set(0)
  #print("Total squirt damage: "+str(totSqtDmg))
  if isV2:
    global v2Dmg
    v2Dmg=v2Dmg+totSqtDmg
  else:
    global totDmg
    totDmg=totDmg+totSqtDmg

#Drop damage calculation
def drpDmgClc():
  global isV2
  localDmg=list()
  if isV2:
    localDrpUsed=v2Drp
  else:
    localDrpUsed=drpUsed
  if dmgDown.get()=='10%':
    for i in range(len(localDrpUsed)):
      localDmg.append(localDrpUsed[i]-math.ceil(localDrpUsed[i]*.1))
  elif dmgDown.get()=='15%':
    for i in range(len(localDrpUsed)):
      localDmg.append(localDrpUsed[i]-math.ceil(localDrpUsed[i]*.15))
  elif dmgDown.get()=='20%':
    for i in range(len(localDrpUsed)):
      localDmg.append(localDrpUsed[i]-math.ceil(localDrpUsed[i]*.2))
  else:
    for i in range(len(localDrpUsed)):
      localDmg.append(localDrpUsed[i])
  #print("Damage of each individual drop gag:"+str(localDmg))
  totDrpDmg=sum(localDmg,0)
  global lured
  if lured.get()==0:
    #print("The cogs are not lured, so drop is able to hit!")
    if len(localDrpUsed)>1:
      totDrpDmg=totDrpDmg+math.ceil((totDrpDmg*0.2))
  else:
    #print("The cogs are lured, and drop does not work on lured cogs! https://www.youtube.com/watch?v=NV-p_-OvUnA&t=4s")
    totDrpDmg=0
  #print("Total drop damage: "+str(totDrpDmg))
  if isV2:
    global v2Dmg
    v2Dmg=v2Dmg+totDrpDmg
  else:
    global totDmg
    totDmg=totDmg+totDrpDmg

#Trap damage calculation
def trpDmgClc():
  global isV2
  localDmg=list()
  if isV2:
    localTrpUsed=v2Trp
  else:
    localTrpUsed=trpUsed
  if dmgDown.get()=='10%':
    for i in range(len(localTrpUsed)):
      localDmg.append(localTrpUsed[i]-math.ceil(localTrpUsed[i]*.1))
  if dmgDown.get()=='15%':
    for i in range(len(localTrpUsed)):
      localDmg.append(localTrpUsed[i]-math.ceil(localTrpUsed[i]*.15))
  if dmgDown.get()=='20%':
    for i in range(len(localTrpUsed)):
      localDmg.append(localTrpUsed[i]-math.ceil(localTrpUsed[i]*.2))
  else:
    for i in range(len(localTrpUsed)):
      localDmg.append(localTrpUsed[i])
  #print("Damage of each individual trap gag:"+str(localDmg))
  global lured
  if lured.get()==0:
    #print("You need to lure cogs if you want trap to work!")
    totTrpDmg=0
  else:
    if len(localTrpUsed)>1:
      #print("The traps canceled out! Only one trap can be used on a cog at a time!")
      totTrpDmg=0
    else:
      #print("The trap worked! This can mean only one thing: You used lure AND only one trap on the cog! Amazing! It did "+str(trpUsed[0])+" damage!")
      totTrpDmg=localDmg[0]
      lured.set(0)
  if isV2:
    global v2Dmg
    v2Dmg=v2Dmg+totTrpDmg
  else:
    global totDmg
    totDmg=totDmg+totTrpDmg

#Cog HP Cheatsheet Function
def cHPClcDlt():
  cogHPSheet.grid_remove()
  sosCards.grid_remove()
  window.geometry('')
  cogClc.configure(text='Show Health and\n SOS Cards',command=cHPClc)

def cHPClc():
  cogHPSheet.grid(column=0,row=3)
  cogHPLbl.grid(column=0,row=0)
  sosCards.grid(column=1,row=3)
  sosTrp.grid(column=0,row=0)
  clrkWill.grid(column=0,row=0)
  clrkPenny.grid(column=1,row=0)
  clrkClara.grid(column=2,row=0)
  sosSnd.grid(column=0,row=1)
  barb.grid(column=0,row=0)
  sid.grid(column=1,row=0)
  moe.grid(column=2,row=0)
  sosDrp.grid(column=0,row=2)
  ned.grid(column=0,row=0)
  franz.grid(column=1,row=0)
  bess.grid(column=2,row=0)
  cogClc.configure(text='Hide Health and\n SOS Cards',command=cHPClcDlt)
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
  global levelKilled
  if totDmg<6:
    #print("Cannot kill a level one.")
    levelKilled=0
  elif 5<totDmg<12:
    #print("Can kill a level one.")
    levelKilled=1
  elif 11<totDmg<20:
    #print("Can kill a level two.")
    levelKilled=2
  elif 19<totDmg<30:
    #print("Can kill a level three.")
    levelKilled=3
  elif 29<totDmg<42:
    #print("Can kill a level four.")
    levelKilled=4
  elif 41<totDmg<56:
    #print("Can kill a level five.")
    levelKilled=5
  elif 55<totDmg<72:
    #print("Can kill a level six.")
    levelKilled=6
  elif 71<totDmg<90:
    #print("Can kill a level seven.")
    levelKilled=7
  elif 89<totDmg<110:
    #print("Can kill a level eight.")
    levelKilled=8
  elif 109<totDmg<132:
    #print("Can kill a level nine.")
    levelKilled=9
  elif 131<totDmg<156:
    #print("Can kill a level ten.")
    levelKilled=10
  elif 155<totDmg<196:
    #print("Can kill a level eleven.")
    levelKilled=11
  elif 195<totDmg<224:
    #print("Can kill a level twelve.")
    levelKilled=12
  elif 223<totDmg<254:
    #print("Can kill a level thirteen.")
    levelKilled=13
  elif 253<totDmg<286:
    #print("Can kill a level fourteen.")
    levelKilled=14
  elif 285<totDmg<320:
    #print("Can kill a level fifteen.")
    levelKilled=15
  elif 319<totDmg<356:
    #print("Can kill a level sixteen.")
    levelKilled=16
  elif 355<totDmg<394:
    #print("Can kill a level seventeen.")
    levelKilled=17
  elif 393<totDmg<434:
    #print("Can kill a level eighteen.")
    levelKilled=18
  elif 433<totDmg<476:
    #print("Can kill a level nineteen.")
    levelKilled=19
  elif 475<totDmg:
    #print("Can kill a level twenty.")
    levelKilled=20
  else:
    #print("what the fuck")
    levelKilled=-1
  #needed to make a new variable, and it introduced the chance to optimize
  #hoping I didn't break the code
  #shit i broke the code im sorry
  #think it's fixed but who knows what lingering damage this caused
  if levelKilled == 0:
    cHPInd.configure(text="(level 0)")
    v2Clc(levelKilled)
  elif levelKilled == -1:
    cHPInd.configure(text="(???)")
    v2CHPInd.configure(text="something went wrong! try getting gud later")
  else:
    cHPInd.configure(text="(level " + str(levelKilled) + ")")
    v2Clc(levelKilled)

#V2 HP Indicator Function
def v2CHPIndClc():
  global v2Dmg
  global levelKilled
  global v2Killed
  if v2Dmg<6:
    #print("Cannot kill a v2 level one.")
    v2Killed = 0
  elif 5<v2Dmg<12:
    #print("Can kill a v2 level one.")
    v2Killed = 1
  elif 11<v2Dmg<20:
    #print("Can kill a v2 level two.")
    v2Killed = 2
  elif 19<v2Dmg<30:
    #print("Can kill a v2 level three.")
    v2Killed = 3
  elif 29<v2Dmg<42:
    #print("Can kill a v2 level four.")
    v2Killed = 4
  elif 41<v2Dmg<56:
    #print("Can kill a v2 level five.")
    v2Killed = 5
  elif 55<v2Dmg<72:
    #print("Can kill a v2 level six.")
    v2Killed = 6
  elif 71<v2Dmg<90:
    #print("Can kill a v2 level seven.")
    v2Killed = 7
  elif 89<v2Dmg<110:
    #print("Can kill a v2 level eight.")
    v2Killed = 8
  elif 109<v2Dmg<132:
    #print("Can kill a v2 level nine.")
    v2Killed = 9
  elif 131<v2Dmg<156:
    #print("Can kill a v2 level ten.")
    v2Killed = 10
  elif 155<v2Dmg<196:
    #print("Can kill a v2 level eleven.")
    v2Killed = 11
  elif 195<v2Dmg<224:
    #print("Can kill a v2 level twelve.")
    v2Killed = 12
  elif 223<v2Dmg<254:
    #print("Can kill a v2 level thirteen.")
    v2Killed = 13
  elif 253<v2Dmg<286:
    #print("Can kill a v2 level fourteen.")
    v2Killed = 14
  elif 285<v2Dmg<320:
    #print("Can kill a v2 level fifteen.")
    v2Killed = 15
  elif 319<v2Dmg<356:
    #print("Can kill a v2 level sixteen.")
    v2Killed = 16
  elif 355<v2Dmg<394:
    #print("Can kill a v2 level seventeen.")
    v2Killed = 17
  elif 393<v2Dmg<434:
    #print("Can kill a v2 level eighteen.")
    v2Killed = 18
  elif 433<v2Dmg<476:
    #print("Can kill a v2 level nineteen.")
    v2Killed = 19
  elif 475<v2Dmg:
    #print("Can kill a v2 level twenty.")
    v2Killed = 20
  else:
    #print("what the fuck")
    v2Killed = -1
  if v2Killed == 0 and levelKilled <= 1:
    v2CHPInd.configure(text="(level 0)")
  elif v2Killed == -1:
    v2CHPInd.configure(text="i probably negative'd 2.0s wrong LMAO")
  elif v2Killed == levelKilled or v2Killed == levelKilled - 1:
    #This may not be the most user friendly way of displaying the levels used for calculation, but it helps reduce processing time by trimming how many loops are needed to find a level that can be beaten
    v2CHPInd.configure(text="(level " + str(v2Killed) + ", calc based on level " +str(levelKilled) + ")")
  elif v2Killed > levelKilled:
    #this doesn't happen often but when it does, hoo boy
    v2CHPInd.configure(text="(level " + str(levelKilled) + ", calc based on level " +str(levelKilled) + ")")
  else:
    levelKilled -= 1
    v2Clc(levelKilled)
    levelKilled += 1

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
#brb crying myself to sleep ,., please fix this vhou sorry thank you
v2Results.grid(column=0,row=1)
v2DmgThsRnd.grid(column=0,row=1)
v2TheDmg.grid(column=1,row=1)
v2CHPInd.grid(column=2,row=1)

#Run
window.mainloop()
