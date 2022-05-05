from tkinter import *

from mod import calculators
from mod import update_checker

'''
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
global dmg_down
global def_lur_lock
global organic
global snd_used
global trw_used
global sqt_used
global drp_used
global trp_used
global tot_dmg
global v2
lured=IntVar()
def_values=['0%','10%','15%','20%']
dmg_down=StringVar()
dmg_down.set('0%')
def_lur_options=['No lock','Lock lure','Lock defense','Lock both']
def_lur_lock=StringVar()
def_lur_lock.set('No lock')
organic=0
snd_used=list()
trw_used=list()
sqt_used=list()
drp_used=list()
trp_used=list()
tot_dmg=0
v2=IntVar()

#Columns
col0=Frame(window) #Main content of the calculator
col1=Frame(window) #Will be used for calculation history

#Total damage calculation
def calc_dmg(opt=""):
  global tot_dmg
  global lured
  local_lure=0
  if lured.get()==1: #Find out if lure is enabled. If it is, save a local variable.
    local_lure=1
  global v2
  if v2.get()==0:
    if len(trp_used)==1 and lured.get()==1:
      tot_dmg=tot_dmg+calculators.gag_calculator(trp_used,defense=trans_def(dmg_down.get()))
      lured.set(0)
    if len(snd_used)>0:
      tot_dmg=tot_dmg+calculators.gag_calculator(snd_used,defense=trans_def(dmg_down.get()))
      lured.set(0)
    if len(trw_used)>0:
      tot_dmg=tot_dmg+calculators.gag_calculator(trw_used,lured=lured.get(),defense=trans_def(dmg_down.get()))
      lured.set(0)
    if len(sqt_used)>0:
      tot_dmg=tot_dmg+calculators.gag_calculator(sqt_used,lured=lured.get(),defense=trans_def(dmg_down.get()))
      lured.set(0)
    if len(drp_used)>0 and lured.get()==0:
      tot_dmg=tot_dmg+calculators.gag_calculator(drp_used,defense=trans_def(dmg_down.get()))
    #print("Total damage this round: "+str(tot_dmg))
    dmg_indicator.configure(text=str(tot_dmg))
    cog_health_ind_calc()
    tot_dmg=0
    def_btn.configure(state="normal")
  else:
    v2_calc()
    def_btn.configure(state="disabled")
  if local_lure==1:
    lured.set(1)

#Defense str -> int
def trans_def(mod):
  if mod=="0%":
    return None
  if mod=="10%":
    return 0.1
  if mod=="15%":
    return 0.15
  if mod=="20%":
    return 0.2

#Toggles
tog_btns=Frame(col0)
org_btn=Button(tog_btns,text='Toggle Organic',font=('Arial',11,'normal'))
lur_check=Checkbutton(tog_btns,text='Cog lured',variable=lured,onvalue=1,offvalue=0,font=('Arial',11,'normal'),command=calc_dmg)
clear_btn=Button(tog_btns,text='Reset damage',font=('Arial',11,'normal'))
def_lbl=Label(tog_btns,text='Defense:',font=('Arial',11,'normal'))
def_btn=OptionMenu(tog_btns,dmg_down,*def_values,command=calc_dmg)
def_btn.configure(width=4,font=('Arial',11,'normal'))
def_lur_dropdown=OptionMenu(tog_btns,def_lur_lock,*def_lur_options)
def_lur_dropdown.configure(width=12,font=('Arial',11,'normal'))
v2_check=Checkbutton(tog_btns,text='V2 Cog',variable=v2,onvalue=1,offvalue=0,font=('Arial',11,'normal'),command=calc_dmg)

#The Gags
gag_frame=Frame(col0)
#Sound
snd_frame=Frame(gag_frame)
bike_horn_img=PhotoImage(file='img/bike-horn.png')
bike_horn=Button(snd_frame,image=bike_horn_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
whistle_img=PhotoImage(file='img/whistle.png')
whistle=Button(snd_frame,image=whistle_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
bugle_img=PhotoImage(file='img/bugle.png')
bugle=Button(snd_frame,image=bugle_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
aoogah_img=PhotoImage(file='img/aoogah.png')
aoogah=Button(snd_frame,image=aoogah_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
elephant_trunk_img=PhotoImage(file='img/elephant-trunk.png')
elephant_trunk=Button(snd_frame,image=elephant_trunk_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
fog_horn_img=PhotoImage(file='img/fog-horn.png')
fog_horn=Button(snd_frame,image=fog_horn_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
opera_singer_img=PhotoImage(file='img/opera-singer.png')
opera_singer=Button(snd_frame,image=opera_singer_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
#Throw
trw_frame=Frame(gag_frame)
cupcake_img=PhotoImage(file='img/cupcake.png')
cupcake=Button(trw_frame,image=cupcake_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
fruit_pie_slice_img=PhotoImage(file='img/fruit-pie-slice.png')
fruit_pie_slice=Button(trw_frame,image=fruit_pie_slice_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
cream_pie_slice_img=PhotoImage(file='img/cream-pie-slice.png')
cream_pie_slice=Button(trw_frame,image=cream_pie_slice_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
whole_fruit_pie_img=PhotoImage(file='img/whole-fruit-pie.png')
whole_fruit_pie=Button(trw_frame,image=whole_fruit_pie_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
whole_cream_pie_img=PhotoImage(file='img/whole-cream-pie.png')
whole_cream_pie=Button(trw_frame,image=whole_cream_pie_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
birthday_cake_img=PhotoImage(file='img/birthday-cake.png')
birthday_cake=Button(trw_frame,image=birthday_cake_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
wedding_cake_img=PhotoImage(file='img/wedding-cake.png')
wedding_cake=Button(trw_frame,image=wedding_cake_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
#Squirt
sqt_frame=Frame(gag_frame)
squirting_flower_img=PhotoImage(file='img/squirting-flower.png')
squirting_flower=Button(sqt_frame,image=squirting_flower_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
water_glass_img=PhotoImage(file='img/glass-of-water.png')
water_glass=Button(sqt_frame,image=water_glass_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
squirt_gun_img=PhotoImage(file='img/squirt-gun.png')
squirt_gun=Button(sqt_frame,image=squirt_gun_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
seltzer_bottle_img=PhotoImage(file='img/seltzer-bottle.png')
seltzer_bottle=Button(sqt_frame,image=seltzer_bottle_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
fire_hose_img=PhotoImage(file='img/fire-hose.png')
fire_hose=Button(sqt_frame,image=fire_hose_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
storm_cloud_img=PhotoImage(file='img/storm-cloud.png')
storm_cloud=Button(sqt_frame,image=storm_cloud_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
geyser_img=PhotoImage(file='img/geyser.png')
geyser=Button(sqt_frame,image=geyser_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
#Drop
drp_frame=Frame(gag_frame)
flower_pot_img=PhotoImage(file='img/flower-pot.png')
flower_pot=Button(drp_frame,image=flower_pot_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
sandbag_img=PhotoImage(file='img/sandbag.png')
sandbag=Button(drp_frame,image=sandbag_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
anvil_img=PhotoImage(file='img/anvil.png')
anvil=Button(drp_frame,image=anvil_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
big_weight_img=PhotoImage(file='img/big-weight.png')
big_weight=Button(drp_frame,image=big_weight_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
safe_img=PhotoImage(file='img/safe.png')
safe=Button(drp_frame,image=safe_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
grand_piano_img=PhotoImage(file='img/grand-piano.png')
grand_piano=Button(drp_frame,image=grand_piano_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
toontanic_img=PhotoImage(file='img/toontanic.png')
toontanic=Button(drp_frame,image=toontanic_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
#Trap!
trpFrame=Frame(gag_frame)
banana_peel_img=PhotoImage(file='img/banana-peel.png')
banana_peel=Button(trpFrame,image=banana_peel_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
rake_img=PhotoImage(file='img/rake.png')
rake=Button(trpFrame,image=rake_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
marbles_img=PhotoImage(file='img/marbles.png')
marbles=Button(trpFrame,image=marbles_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
quicksand_img=PhotoImage(file='img/quicksand.png')
quicksand=Button(trpFrame,image=quicksand_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
trapdoor_img=PhotoImage(file='img/trapdoor.png')
trapdoor=Button(trpFrame,image=trapdoor_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
tnt_img=PhotoImage(file='img/tnt.png')
tnt=Button(trpFrame,image=tnt_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')
railroad_img=PhotoImage(file='img/railroad.png')
railroad=Button(trpFrame,image=railroad_img,bg='#1888D3',activebackground='#186AD3',text='0',font=('Impress BT',8,'bold'),compound='top',fg='white')

#Button list - used for mass configuring the gag buttons
gag_btns=(bike_horn,whistle,bugle,aoogah,elephant_trunk,fog_horn,opera_singer,cupcake,fruit_pie_slice,cream_pie_slice,whole_fruit_pie,whole_cream_pie,birthday_cake,wedding_cake,squirting_flower,water_glass,squirt_gun,seltzer_bottle,fire_hose,storm_cloud,geyser,flower_pot,sandbag,anvil,big_weight,safe,grand_piano,toontanic,banana_peel,rake,marbles,quicksand,trapdoor,tnt,railroad)

#Calculation history
hist=Frame(col1)
hist_lbl=Label(hist,text="History")
hist_box=Text(hist,width=25,height=22,state=DISABLED,font=('Arial',10,'normal'),wrap=WORD)
pin_btn=Button(hist,text="Pin to top")
clear_hist_btn=Button(hist,text="Clear History")
cog_calc=Button(hist,text="Show Health and\n SOS Cards")

#Calculation results
calc_results=Frame(col0)
dmg_this_round=Label(calc_results,text="Damage this round:",font=('Arial',16,'normal'))
dmg_indicator=Label(calc_results,text="0",font=('Arial',16,'bold'))
cog_level_indicator=Label(calc_results,text="(level 0)",font=('Arial',8,'normal'))
org_indicator=Label(calc_results,text="Organic = OFF",font=('Arial',10,'bold'))

#Cog HP
cog_health_sheet=Frame(window)
cog_health_img=PhotoImage(file='img/coghp.png')
cog_health_lbl=Label(cog_health_sheet,image=cog_health_img)

#SOS Cards
sos_cards=Frame(window)
sos_trp=Frame(sos_cards)
clerk_will_img=PhotoImage(file='img/clerkwill.png')
clerk_will=Button(sos_trp,image=clerk_will_img)
clerk_penny_img=PhotoImage(file='img/clerkpenny.png')
clerk_penny=Button(sos_trp,image=clerk_penny_img)
clerk_clara_img=PhotoImage(file='img/clerkclara.png')
clerk_clara=Button(sos_trp,image=clerk_clara_img)
sos_snd=Frame(sos_cards)
barb_img=PhotoImage(file='img/barbaraseville.png')
barb=Button(sos_snd,image=barb_img)
sid_img=PhotoImage(file='img/sidsonata.png')
sid=Button(sos_snd,image=sid_img)
moe_img=PhotoImage(file='img/moezart.png')
moe=Button(sos_snd,image=moe_img)
sos_drp=Frame(sos_cards)
ned_img=PhotoImage(file='img/clumsyned.png')
ned=Button(sos_drp,image=ned_img)
franz_img=PhotoImage(file='img/franzneckvein.png')
franz=Button(sos_drp,image=franz_img)
bess_img=PhotoImage(file='img/barnaclebessie.png')
bess=Button(sos_drp,image=bess_img)

#Toggle organic functions
def tog_org_off(opt=""):
  global organic
  organic=0
  #print("Gags in calculations will no longer be organic!")
  org_btn.configure(command=tog_org_on)
  org_indicator.configure(text="Organic = OFF")
  for i in gag_btns:
    i.configure(bg='#1888D3',activebackground='#186AD3')
  window.bind('<Shift_L>',tog_org_on)
def tog_org_on(opt=""):
  global organic
  organic=1
  #print("Gags in calculations will now be organic!")
  org_btn.configure(command=tog_org_off)
  org_indicator.configure(text="Organic = ON")
  for i in gag_btns:
    i.configure(bg='darkorange',activebackground='orange')
  window.bind('<Shift_L>',tog_org_off)
org_btn.configure(command=tog_org_on)
window.bind('<Shift_L>',tog_org_on)

#Def Keybind
def defSwap(opt=""):
  global dmg_down
  if dmg_down.get()=='0%':
    dmg_down.set('10%')
    calc_dmg()
  elif dmg_down.get()=='10%':
    dmg_down.set('15%')
    calc_dmg()
  elif dmg_down.get()=='15%':
    dmg_down.set('20%')
    calc_dmg()
  else:
    dmg_down.set('0%')
    calc_dmg()
window.bind('<Control-d>',defSwap)

#Lure Keybind
def lureSwap(opt=""):
  if lured.get()==0:
    lured.set(1)
    calc_dmg()
  else:
    lured.set(0)
    calc_dmg()
window.bind('<Control-l>',lureSwap)

#V2 Keybind
def v2Swap(opt=""):
  if v2.get()==0:
    v2.set(1)
    calc_dmg()
  else:
    v2.set(0)
    calc_dmg()
window.bind('<Control-v>',v2Swap)

#Clear inputs function
def clear_inputs(opt=""):
  #print("Clearing gag inputs!")
  global lured
  global dmg_down
  global def_lur_lock
  global snd_used
  global trw_used
  global sqt_used
  global drp_used
  global trp_used
  global v2
  local_lure=0
  lur_info='no'
  if lured.get()==1: #Find out if lure is enabled. If it is, save a local variable.
    local_lure=1
    lur_info='yes'
  hist_box.configure(state=NORMAL)
  if v2.get()==1:
    hist_box.insert('1.0',"--------\nCalculation finished!\nDamage calculated was: "+dmg_indicator.cget("text")+"\nDefense: V2.0"+"\nLure: "+lur_info+"\nWill kill: "+cog_level_indicator.cget("text")+"\n\n")
  else:
    hist_box.insert('1.0',"--------\nCalculation finished!\nDamage calculated was: "+dmg_indicator.cget("text")+"\nDefense: "+dmg_down.get()+"\nLure: "+lur_info+"\nWill kill: "+cog_level_indicator.cget("text")+"\n\n")
  hist_box.configure(state=DISABLED)
  if def_lur_lock.get()=='No lock' or def_lur_lock.get()=='Lock lure':
    dmg_down.set('0%')
  lured.set(0)
  v2.set(0)
  snd_used=list()
  trw_used=list()
  sqt_used=list()
  drp_used=list()
  trp_used=list()
  tog_org_off()
  calc_dmg()
  for i in gag_btns:
    i.configure(text='0')
  if local_lure==1 and def_lur_lock.get()=='Lock lure' or def_lur_lock.get()=='Lock both': #Use the local variable and def_lur_lock to lock lure as active even after it is set to 0 by clear_inputs()
    lured.set(1)
clear_btn.configure(command=clear_inputs)
window.bind('<Control-r>',clear_inputs)

#Clear history function
def clear_history():
  #print("Clearing calculcation history!")
  hist_box.configure(state=NORMAL)
  hist_box.delete('1.0', END)
  hist_box.configure(state=DISABLED)
clear_hist_btn.configure(command=clear_history)

#Clicking on the bike horn button - the first button to be configured, and the button that will be used as the guinea pig for most testing.
def bike_horn_prs():
  if organic==0:
    #bike_horn.configure(bg='#104789',activebackground='#0D3A6D') #maybe a selection indicator?
    snd_used.append(4)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Bike Horn (4)\n")
    hist_box.configure(state=DISABLED)
  else:
    snd_used.append(5)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Bike Horn (5)\n")
    hist_box.configure(state=DISABLED)
  bike_horn.configure(text=int(bike_horn.cget("text"))+1)
  calc_dmg()
bike_horn.configure(command=bike_horn_prs)
#Other sound buttons, who gives a fuck
def whistle_prs():
  if organic==0:
    snd_used.append(7)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Whistle (7)\n")
    hist_box.configure(state=DISABLED)
  else:
    snd_used.append(8)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Whistle (8)\n")
    hist_box.configure(state=DISABLED)
  whistle.configure(text=int(whistle.cget("text"))+1)
  calc_dmg()
whistle.configure(command=whistle_prs)
def bugle_prs():
  if organic==0:
    snd_used.append(11)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Bugle (11)\n")
    hist_box.configure(state=DISABLED)
  else:
    snd_used.append(12)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Bugle (12)\n")
    hist_box.configure(state=DISABLED)
  bugle.configure(text=int(bugle.cget("text"))+1)
  calc_dmg()
bugle.configure(command=bugle_prs)
def aoogah_prs():
  if organic==0:
    snd_used.append(16)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Aoogah (16)\n")
    hist_box.configure(state=DISABLED)
  else:
    snd_used.append(17)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Aoogah (17)\n")
    hist_box.configure(state=DISABLED)
  aoogah.configure(text=int(aoogah.cget("text"))+1)
  calc_dmg()
aoogah.configure(command=aoogah_prs)
def elephant_trunk_prs():
  if organic==0:
    snd_used.append(21)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Elephant Trunk (21)\n")
    hist_box.configure(state=DISABLED)
  else:
    snd_used.append(23)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Elephant Trunk (23)\n")
    hist_box.configure(state=DISABLED)
  elephant_trunk.configure(text=int(elephant_trunk.cget("text"))+1)
  calc_dmg()
elephant_trunk.configure(command=elephant_trunk_prs)
def fog_horn_prs():
  if organic==0:
    snd_used.append(50)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Foghorn (50)\n")
    hist_box.configure(state=DISABLED)
  else:
    snd_used.append(55)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Foghorn (55)\n")
    hist_box.configure(state=DISABLED)
  fog_horn.configure(text=int(fog_horn.cget("text"))+1)
  calc_dmg()
fog_horn.configure(command=fog_horn_prs)
def opera_singer_prs():
  if organic==0:
    snd_used.append(90)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Opera Singer (90)\n")
    hist_box.configure(state=DISABLED)
  else:
    snd_used.append(99)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Opera Singer (99)\n")
    hist_box.configure(state=DISABLED)
  opera_singer.configure(text=int(opera_singer.cget("text"))+1)
  calc_dmg()
opera_singer.configure(command=opera_singer_prs)

#Throw
def cupcake_prs():
  if organic==0:
    trw_used.append(6)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Cupcake (6)\n")
    hist_box.configure(state=DISABLED)
  else:
    trw_used.append(7)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Cupcake (7)\n")
    hist_box.configure(state=DISABLED)
  cupcake.configure(text=int(cupcake.cget("text"))+1)
  calc_dmg()
cupcake.configure(command=cupcake_prs)
def fruit_pie_slice_prs():
  if organic==0:
    trw_used.append(10)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Fruit Pie Slice (10)\n")
    hist_box.configure(state=DISABLED)
  else:
    trw_used.append(11)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Fruit Pie Slice (11)\n")
    hist_box.configure(state=DISABLED)
  fruit_pie_slice.configure(text=int(fruit_pie_slice.cget("text"))+1)
  calc_dmg()
fruit_pie_slice.configure(command=fruit_pie_slice_prs)
def cream_pie_slice_prs():
  if organic==0:
    trw_used.append(17)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Cream Pie Slice (17)\n")
    hist_box.configure(state=DISABLED)
  else:
    trw_used.append(18)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Cream Pie Slice (18)\n")
    hist_box.configure(state=DISABLED)
  cream_pie_slice.configure(text=int(cream_pie_slice.cget("text"))+1)
  calc_dmg()
cream_pie_slice.configure(command=cream_pie_slice_prs)
def whole_fruit_pie_prs():
  if organic==0:
    trw_used.append(27)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Whole Fruit Pie (27)\n")
    hist_box.configure(state=DISABLED)
  else:
    trw_used.append(29)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Whole Fruit Pie (29)\n")
    hist_box.configure(state=DISABLED)
  whole_fruit_pie.configure(text=int(whole_fruit_pie.cget("text"))+1)
  calc_dmg()
whole_fruit_pie.configure(command=whole_fruit_pie_prs)
def whole_cream_pie_prs():
  if organic==0:
    trw_used.append(40)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Whole Cream Pie (40)\n")
    hist_box.configure(state=DISABLED)
  else:
    trw_used.append(44)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Whole Cream Pie (44)\n")
    hist_box.configure(state=DISABLED)
  whole_cream_pie.configure(text=int(whole_cream_pie.cget("text"))+1)
  calc_dmg()
whole_cream_pie.configure(command=whole_cream_pie_prs)
def birthday_cake_prs():
  if organic==0:
    trw_used.append(100)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Birthday Cake (100)\n")
    hist_box.configure(state=DISABLED)
  else:
    trw_used.append(110)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Birthday Cake (110)\n")
    hist_box.configure(state=DISABLED)
  birthday_cake.configure(text=int(birthday_cake.cget("text"))+1)
  calc_dmg()
birthday_cake.configure(command=birthday_cake_prs)
def wedding_cake_prs():
  if organic==0:
    trw_used.append(120)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Wedding Cake (120)\n")
    hist_box.configure(state=DISABLED)
  else:
    trw_used.append(132)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Wedding Cake (132)\n")
    hist_box.configure(state=DISABLED)
  wedding_cake.configure(text=int(wedding_cake.cget("text"))+1)
  calc_dmg()
wedding_cake.configure(command=wedding_cake_prs)

#Squirt
def squirting_flower_prs():
  if organic==0:
    sqt_used.append(4)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Squirting Flower (4)\n")
    hist_box.configure(state=DISABLED)
  else:
    sqt_used.append(5)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Squirting Flower (5)\n")
    hist_box.configure(state=DISABLED)
  squirting_flower.configure(text=int(squirting_flower.cget("text"))+1)
  calc_dmg()
squirting_flower.configure(command=squirting_flower_prs)
def water_glass_prs():
  if organic==0:
    sqt_used.append(8)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Glass of Water (8)\n")
    hist_box.configure(state=DISABLED)
  else:
    sqt_used.append(9)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Glass of Water (9)\n")
    hist_box.configure(state=DISABLED)
  water_glass.configure(text=int(water_glass.cget("text"))+1)
  calc_dmg()
water_glass.configure(command=water_glass_prs)
def squirt_gun_prs():
  if organic==0:
    sqt_used.append(12)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Squirt Gun (12)\n")
    hist_box.configure(state=DISABLED)
  else:
    sqt_used.append(13)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Squirt Gun (13)\n")
    hist_box.configure(state=DISABLED)
  squirt_gun.configure(text=int(squirt_gun.cget("text"))+1)
  calc_dmg()
squirt_gun.configure(command=squirt_gun_prs)
def seltzer_bottle_prs():
  if organic==0:
    sqt_used.append(21)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Seltzer Bottle (21)\n")
    hist_box.configure(state=DISABLED)
  else:
    sqt_used.append(23)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Seltzer Bottle (23)\n")
    hist_box.configure(state=DISABLED)
  seltzer_bottle.configure(text=int(seltzer_bottle.cget("text"))+1)
  calc_dmg()
seltzer_bottle.configure(command=seltzer_bottle_prs)
def fire_hose_prs():
  if organic==0:
    sqt_used.append(30)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Fire Hose (30)\n")
    hist_box.configure(state=DISABLED)
  else:
    sqt_used.append(33)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Fire Hose (33)\n")
    hist_box.configure(state=DISABLED)
  fire_hose.configure(text=int(fire_hose.cget("text"))+1)
  calc_dmg()
fire_hose.configure(command=fire_hose_prs)
def storm_cloud_prs():
  if organic==0:
    sqt_used.append(80)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Storm Cloud (80)\n")
    hist_box.configure(state=DISABLED)
  else:
    sqt_used.append(88)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Storm Cloud (88)\n")
    hist_box.configure(state=DISABLED)
    #print("Hey did you know an organic storm cloud can kill a lured level 10? Organic squirt is cooler than organic throw but most people keep lying to themselves about the true superior organic track.")
  storm_cloud.configure(text=int(storm_cloud.cget("text"))+1)
  calc_dmg()
storm_cloud.configure(command=storm_cloud_prs)
def geyser_prs():
  if organic==0:
    sqt_used.append(105)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Geyser (105)\n")
    hist_box.configure(state=DISABLED)
  else:
    sqt_used.append(115)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Geyser (115)\n")
    hist_box.configure(state=DISABLED)
  geyser.configure(text=int(geyser.cget("text"))+1)
  calc_dmg()
geyser.configure(command=geyser_prs)

#Drop
def flower_pot_prs():
  if organic==0:
    drp_used.append(10)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Flower Pot (10)\n")
    hist_box.configure(state=DISABLED)
  else:
    drp_used.append(11)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Flower Pot (11)\n")
    hist_box.configure(state=DISABLED)
  flower_pot.configure(text=int(flower_pot.cget("text"))+1)
  calc_dmg()
flower_pot.configure(command=flower_pot_prs)
def sandbag_prs():
  if organic==0:
    drp_used.append(18)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Sandbag (18)\n")
    hist_box.configure(state=DISABLED)
  else:
    drp_used.append(19)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Sandbag (19)\n")
    hist_box.configure(state=DISABLED)
  sandbag.configure(text=int(sandbag.cget("text"))+1)
  calc_dmg()
sandbag.configure(command=sandbag_prs)
def anvil_prs():
  if organic==0:
    drp_used.append(30)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Anvil (30)\n")
    hist_box.configure(state=DISABLED)
  else:
    drp_used.append(33)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Anvil (33)\n")
    hist_box.configure(state=DISABLED)
  anvil.configure(text=int(anvil.cget("text"))+1)
  calc_dmg()
anvil.configure(command=anvil_prs)
def big_weight_prs():
  if organic==0:
    drp_used.append(45)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Big Weight (45)\n")
    hist_box.configure(state=DISABLED)
  else:
    drp_used.append(49)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Big Weight (49)\n")
    hist_box.configure(state=DISABLED)
  big_weight.configure(text=int(big_weight.cget("text"))+1)
  calc_dmg()
big_weight.configure(command=big_weight_prs)
def safe_prs():
  if organic==0:
    drp_used.append(70)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Safe (70)\n")
    hist_box.configure(state=DISABLED)
  else:
    drp_used.append(77)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Safe (77)\n")
    hist_box.configure(state=DISABLED)
  safe.configure(text=int(safe.cget("text"))+1)
  calc_dmg()
safe.configure(command=safe_prs)
def grand_piano_prs():
  if organic==0:
    drp_used.append(170)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Grand Piano (170)\n")
    hist_box.configure(state=DISABLED)
  else:
    drp_used.append(187)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Grand Piano (187)\n")
    hist_box.configure(state=DISABLED)
  grand_piano.configure(text=int(grand_piano.cget("text"))+1)
  calc_dmg()
grand_piano.configure(command=grand_piano_prs)
def toontanic_prs():
  if organic==0:
    drp_used.append(180)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Toontanic (180)\n")
    hist_box.configure(state=DISABLED)
  else:
    drp_used.append(198)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Toontanic (198)\n")
    hist_box.configure(state=DISABLED)
  toontanic.configure(text=int(toontanic.cget("text"))+1)
  calc_dmg()
toontanic.configure(command=toontanic_prs)

#Trap
def banana_peel_prs():
  if organic==0:
    trp_used.append(12)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Banana Peel (12)\n")
    hist_box.configure(state=DISABLED)
  else:
    trp_used.append(13)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Banana Peel (13)\n")
    hist_box.configure(state=DISABLED)
  banana_peel.configure(text=int(banana_peel.cget("text"))+1)
  calc_dmg()
banana_peel.configure(command=banana_peel_prs)
def rake_prs():
  if organic==0:
    trp_used.append(20)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Rake (20)\n")
    hist_box.configure(state=DISABLED)
  else:
    trp_used.append(22)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Rake (22)\n")
    hist_box.configure(state=DISABLED)
  rake.configure(text=int(rake.cget("text"))+1)
  calc_dmg()
rake.configure(command=rake_prs)
def marbles_prs():
  if organic==0:
    trp_used.append(35)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Marbles (35)\n")
    hist_box.configure(state=DISABLED)
  else:
    trp_used.append(38)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Marbles (38)\n")
    hist_box.configure(state=DISABLED)
  marbles.configure(text=int(marbles.cget("text"))+1)
  calc_dmg()
marbles.configure(command=marbles_prs)
def quicksand_prs():
  if organic==0:
    trp_used.append(50)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Quicksand (50)\n")
    hist_box.configure(state=DISABLED)
  else:
    trp_used.append(55)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Quicksand (55)\n")
    hist_box.configure(state=DISABLED)
  quicksand.configure(text=int(quicksand.cget("text"))+1)
  calc_dmg()
quicksand.configure(command=quicksand_prs)
def trapdoor_prs():
  if organic==0:
    trp_used.append(85)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Trapdoor (85)\n")
    hist_box.configure(state=DISABLED)
  else:
    trp_used.append(93)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Trapdoor (93)\n")
    hist_box.configure(state=DISABLED)
  trapdoor.configure(text=int(trapdoor.cget("text"))+1)
  calc_dmg()
trapdoor.configure(command=trapdoor_prs)
def tnt_prs():
  if organic==0:
    trp_used.append(180)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: TNT (180)\n")
    hist_box.configure(state=DISABLED)
  else:
    trp_used.append(198)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic TNT (198)\n")
    hist_box.configure(state=DISABLED)
  tnt.configure(text=int(tnt.cget("text"))+1)
  calc_dmg()
tnt.configure(command=tnt_prs)
def railroad_prs():
  if organic==0:
    trp_used.append(200)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Railroad (200)\n")
    hist_box.configure(state=DISABLED)
  else:
    trp_used.append(220)
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: Organic Railroad (220)\n")
    hist_box.configure(state=DISABLED)
  railroad.configure(text=int(railroad.cget("text"))+1)
  calc_dmg()
railroad.configure(command=railroad_prs)

#SOS Cards
def clara_prs():
  trp_used.append(180)
  hist_box.configure(state=NORMAL)
  hist_box.insert('1.0',"Gag used: Clerk Clara (180)\n")
  hist_box.configure(state=DISABLED)
  calc_dmg()
clerk_clara.configure(command=clara_prs)
def penny_prs():
  trp_used.append(120)
  hist_box.configure(state=NORMAL)
  hist_box.insert('1.0',"Gag used: Clerk Penny (120)\n")
  hist_box.configure(state=DISABLED)
  calc_dmg()
clerk_penny.configure(command=penny_prs)
def will_prs():
  trp_used.append(60)
  hist_box.configure(state=NORMAL)
  hist_box.insert('1.0',"Gag used: Clerk Will (60)\n")
  hist_box.configure(state=DISABLED)
  calc_dmg()
clerk_will.configure(command=will_prs)
def moe_prs():
  snd_used.append(75)
  hist_box.configure(state=NORMAL)
  hist_box.insert('1.0',"Gag used: Moe Zart (75)\n")
  hist_box.configure(state=DISABLED)
  calc_dmg()
moe.configure(command=moe_prs)
def sid_prs():
  snd_used.append(55)
  hist_box.configure(state=NORMAL)
  hist_box.insert('1.0',"Gag used: Sid Sonata (55)\n")
  hist_box.configure(state=DISABLED)
  calc_dmg()
sid.configure(command=sid_prs)
def barb_prs():
  snd_used.append(35)
  hist_box.configure(state=NORMAL)
  hist_box.insert('1.0',"Gag used: Barbara Seville (35)\n")
  hist_box.configure(state=DISABLED)
  calc_dmg()
barb.configure(command=barb_prs)
def bess_prs():
  drp_used.append(170)
  hist_box.configure(state=NORMAL)
  hist_box.insert('1.0',"Gag used: Barnacle Bessie (170)\n")
  hist_box.configure(state=DISABLED)
  calc_dmg()
bess.configure(command=bess_prs)
def franz_prs():
  drp_used.append(100)
  hist_box.configure(state=NORMAL)
  hist_box.insert('1.0',"Gag used: Franz Neckvein (100)\n")
  hist_box.configure(state=DISABLED)
  calc_dmg()
franz.configure(command=franz_prs)
def ned_prs():
  drp_used.append(60)
  hist_box.configure(state=NORMAL)
  hist_box.insert('1.0',"Gag used: Clumsy Ned (60)\n")
  hist_box.configure(state=DISABLED)
  calc_dmg()
ned.configure(command=ned_prs)

#Cog HP Cheatsheet Function
def cog_health_calc_hide():
  cog_health_sheet.grid_remove()
  sos_cards.grid_remove()
  window.geometry('')
  cog_calc.configure(text='Show Health and\n SOS Cards',command=cog_health_calc_show)

def cog_health_calc_show():
  cog_health_sheet.grid(column=0,row=3)
  cog_health_lbl.grid(column=0,row=0)
  sos_cards.grid(column=1,row=3)
  sos_trp.grid(column=0,row=0)
  clerk_will.grid(column=0,row=0)
  clerk_penny.grid(column=1,row=0)
  clerk_clara.grid(column=2,row=0)
  sos_snd.grid(column=0,row=1)
  barb.grid(column=0,row=0)
  sid.grid(column=1,row=0)
  moe.grid(column=2,row=0)
  sos_drp.grid(column=0,row=2)
  ned.grid(column=0,row=0)
  franz.grid(column=1,row=0)
  bess.grid(column=2,row=0)
  cog_calc.configure(text='Hide Health and\n SOS Cards',command=cog_health_calc_hide)
  window.geometry('')
cog_calc.configure(command=cog_health_calc_show)

#Pin commands
def unpin():
  window.attributes('-topmost',False)
  pin_btn.configure(command=pin,text='Pin to top')
def pin():
  window.attributes('-topmost',True)
  pin_btn.configure(command=unpin,text='Unpin from top')
pin_btn.configure(command=pin)

#Cog HP Indicator Function
def cog_health_ind_calc():
  lvl=0
  while lvl<20:
    lvl=lvl+1
    #print("Evaluating level: "+str(lvl))
    global tot_dmg
    #print("The current total damage is "+str(tot_dmg))
    if tot_dmg==calculators.cog_health(lvl):
      #print("Wow! We found the level!")
      #print("The level is: "+str(lvl))
      cog_level_indicator.configure(text="(level "+str(lvl)+")")
      break
    elif tot_dmg<calculators.cog_health(lvl):
      #print("Wow! We found the level!")
      lvl=lvl-1
      #print("The level is: "+str(lvl))
      cog_level_indicator.configure(text="(level "+str(lvl)+")")
      break
    elif lvl==20 and tot_dmg>calculators.cog_health(lvl):
      #print("Wow! We found the level!")
      #print("The level is: "+str(lvl))
      cog_level_indicator.configure(text="(level "+str(lvl)+")")

#Cog V2 Calculation
global v2_dmg
v2_dmg=0

def v2_calc():
  lvl=0
  while lvl<20:
    global lured
    local_lure=0
    if lured.get()==1:
      local_lure=1
    lvl=lvl+1
    global v2_dmg
    v2_dmg=0
    #print("Evaluating lvl: "+str(lvl))
    
    if len(trp_used)==1 and lured.get()==1:
      v2_dmg=v2_dmg+calculators.gag_calculator(trp_used,plating=lvl)
      lured.set(0)
    if len(snd_used)>0:
      v2_dmg=v2_dmg+calculators.gag_calculator(snd_used,plating=lvl)
      lured.set(0)
    if len(trw_used)>0:
      v2_dmg=v2_dmg+calculators.gag_calculator(trw_used,lured=lured.get(),plating=lvl)
      lured.set(0)
    if len(sqt_used)>0:
      v2_dmg=v2_dmg+calculators.gag_calculator(sqt_used,lured=lured.get(),plating=lvl)
      lured.set(0)
    if len(drp_used)>0 and lured.get()==0:
      v2_dmg=v2_dmg+calculators.gag_calculator(drp_used,plating=lvl)
    
    if local_lure==1:
      lured.set(1)
    
    if v2_dmg==calculators.cog_health(lvl):
      #print("Wow! We found the level!")
      #print("The level is: "+str(lvl))
      cog_level_indicator.configure(text="(v2.0 level "+str(lvl)+")")
      dmg_indicator.configure(text=str(v2_dmg))
      break
    elif v2_dmg<calculators.cog_health(lvl):
      #print("Wow! We found the level!")
      lvl=lvl-1
      #print("The level is: "+str(lvl))
      v2_dmg=0
      if len(trp_used)==1 and lured.get()==1:
        v2_dmg=v2_dmg+calculators.gag_calculator(trp_used,plating=lvl)
        lured.set(0)
      if len(snd_used)>0:
        v2_dmg=v2_dmg+calculators.gag_calculator(snd_used,plating=lvl)
        lured.set(0)
      if len(trw_used)>0:
        v2_dmg=v2_dmg+calculators.gag_calculator(trw_used,lured=lured.get(),plating=lvl)
        lured.set(0)
      if len(sqt_used)>0:
        v2_dmg=v2_dmg+calculators.gag_calculator(sqt_used,lured=lured.get(),plating=lvl)
        lured.set(0)
      if len(drp_used)>0 and lured.get()==0:
        v2_dmg=v2_dmg+calculators.gag_calculator(drp_used,plating=lvl)
      cog_level_indicator.configure(text="(v2.0 level "+str(lvl)+")")
      dmg_indicator.configure(text=str(v2_dmg))
      break
    elif lvl==20 and v2_dmg>calculators.cog_health(lvl):
      #print("Wow! We found the level!")
      #print("The level is: "+str(lvl))
      cog_level_indicator.configure(text="(v2.0 level "+str(lvl)+")")
      dmg_indicator.configure(text=str(v2_dmg))
    if local_lure==1:
      lured.set(1)

#Toolbar
toolbar=Menu(window)
#Program
program_menu=Menu(toolbar,tearoff=0)
program_menu.add_command(label="Update Checker",command=lambda:update_checker.compare_versions(local_file="mod/version.txt",git_file="https://raw.githubusercontent.com/Vhou-Atroph/TT-Damage-Calculator/main/mod/version.txt"))
program_menu.add_separator()
program_menu.add_command(label="Exit",command=lambda:window.destroy())
toolbar.add_cascade(label="Program",menu=program_menu)
window.configure(menu=toolbar)

#Geometry - Main Columns
col0.grid(column=0,row=0,padx=5)
col1.grid(column=1,row=0,padx=10)

#Geometry - Toggles
tog_btns.grid(column=0,row=1,pady=5)
lur_check.grid(column=0,row=0,padx=5)
org_btn.grid(column=1,row=0,padx=5)
def_lbl.grid(column=2,row=0,padx=0)
def_btn.grid(column=3,row=0)
def_lur_dropdown.grid(column=1,row=1)
clear_btn.grid(column=2,row=1,columnspan=2,padx=5)
v2_check.grid(column=0,row=1)

#Geometry - Gags
gag_frame.grid(column=0,row=2,pady=10)
#Sound
snd_frame.grid(column=0,row=1,)
bike_horn.grid(column=0,row=0)
whistle.grid(column=1,row=0)
bugle.grid(column=2,row=0)
aoogah.grid(column=3,row=0)
elephant_trunk.grid(column=4,row=0)
fog_horn.grid(column=5,row=0)
opera_singer.grid(column=6,row=0)
#Throw
trw_frame.grid(column=0,row=2)
cupcake.grid(column=0,row=0)
fruit_pie_slice.grid(column=1,row=0)
cream_pie_slice.grid(column=2,row=0)
whole_fruit_pie.grid(column=3,row=0)
whole_cream_pie.grid(column=4,row=0)
birthday_cake.grid(column=5,row=0)
wedding_cake.grid(column=6,row=0)
#Squirt
sqt_frame.grid(column=0,row=3)
squirting_flower.grid(column=0,row=0)
water_glass.grid(column=1,row=0)
squirt_gun.grid(column=2,row=0)
seltzer_bottle.grid(column=3,row=0)
fire_hose.grid(column=4,row=0)
storm_cloud.grid(column=5,row=0)
geyser.grid(column=6,row=0)
#Drop
drp_frame.grid(column=0,row=4)
flower_pot.grid(column=0,row=0)
sandbag.grid(column=1,row=0)
anvil.grid(column=2,row=0)
big_weight.grid(column=3,row=0)
safe.grid(column=4,row=0)
grand_piano.grid(column=5,row=0)
toontanic.grid(column=6,row=0)
#Trap
trpFrame.grid(column=0,row=0)
banana_peel.grid(column=0,row=0)
rake.grid(column=1,row=0)
marbles.grid(column=2,row=0)
quicksand.grid(column=3,row=0)
trapdoor.grid(column=4,row=0)
tnt.grid(column=5,row=0)
railroad.grid(column=6,row=0)

#Geometry - Calculation History
hist.grid(column=0,row=0)
hist_lbl.grid(column=0,row=0)
hist_box.grid(column=0,row=1)
clear_hist_btn.grid(column=0,row=2,pady=3)
pin_btn.grid(column=0,row=3,pady=3)
cog_calc.grid(column=0,row=4,pady=3)

#Geometry - Calculation Results
calc_results.grid(column=0,row=0)
dmg_this_round.grid(column=0,row=0)
dmg_indicator.grid(column=1,row=0)
cog_level_indicator.grid(column=2,row=0)
org_indicator.grid(column=0,row=1,columnspan=3)

#Run
window.mainloop()