from tkinter import *

from mod import calculators
from mod import gags
from mod import keybinds
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
global snd_used
global trw_used
global sqt_used
global drp_used
global trp_used
global tot_dmg
snd_used=list()
trw_used=list()
sqt_used=list()
drp_used=list()
trp_used=list()
tot_dmg=0

organic=IntVar()
lured=IntVar()
v2=IntVar()
pin_val=IntVar()
dmg_down=StringVar()
dmg_down.set('0%')
def_values=['0%','10%','15%','20%','25%']
def_lur_lock=StringVar()
def_lur_lock.set('No lock')
def_lur_options=['No lock','Lock lure','Lock defense','Lock both']

#Columns
col0=Frame(window) #Main content of the calculator
col1=Frame(window) #Will be used for calculation history

#Total damage calculation
def calc_dmg(opt=""):
  global tot_dmg
  local_lure=0
  if lured.get()==1: #Find out if lure is enabled. If it is, save a local variable.
    local_lure=1
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
  elif mod=="10%":
    return 0.1
  elif mod=="15%":
    return 0.15
  elif mod=="20%":
    return 0.2
  elif mod=="25%":
    return 0.25

#Gag Buttons
def gag_btn(gag,list,btn=None):
  if organic.get()==1 and gag.type=="Gag":
    name="Organic "+gag.name
    dmg=gag.make_org()
  else:
    dmg=gag.dmg
    name=gag.name
  if btn:
    btn.configure(text=int(btn.cget("text"))+1)
  list.append(dmg)
  hist_box.configure(state=NORMAL)
  hist_box.insert('1.0',"Gag used: "+name+" ("+str(dmg)+")\n")
  hist_box.configure(state=DISABLED)
  calc_dmg()

#Pin window to top
def pin():
  if pin_val.get()==1:
    return window.attributes('-topmost',True)
  window.attributes('-topmost',False)

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
bike_horn.configure(command=lambda:gag_btn(gags.bike_horn,snd_used,bike_horn))
whistle.configure(command=lambda:gag_btn(gags.whistle,snd_used,whistle))
bugle.configure(command=lambda:gag_btn(gags.bugle,snd_used,bugle))
aoogah.configure(command=lambda:gag_btn(gags.aoogah,snd_used,aoogah))
elephant_trunk.configure(command=lambda:gag_btn(gags.elephant_trunk,snd_used,elephant_trunk))
fog_horn.configure(command=lambda:gag_btn(gags.foghorn,snd_used,fog_horn))
opera_singer.configure(command=lambda:gag_btn(gags.opera_singer,snd_used,opera_singer))
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
cupcake.configure(command=lambda:gag_btn(gags.cupcake,trw_used,cupcake))
fruit_pie_slice.configure(command=lambda:gag_btn(gags.fruit_pie_slice,trw_used,fruit_pie_slice))
cream_pie_slice.configure(command=lambda:gag_btn(gags.cream_pie_slice,trw_used,cream_pie_slice))
whole_fruit_pie.configure(command=lambda:gag_btn(gags.whole_fruit_pie,trw_used,whole_fruit_pie))
whole_cream_pie.configure(command=lambda:gag_btn(gags.whole_cream_pie,trw_used,whole_cream_pie))
birthday_cake.configure(command=lambda:gag_btn(gags.birthday_cake,trw_used,birthday_cake))
wedding_cake.configure(command=lambda:gag_btn(gags.wedding_cake,trw_used,wedding_cake))
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
squirting_flower.configure(command=lambda:gag_btn(gags.squirting_flower,sqt_used,squirting_flower))
water_glass.configure(command=lambda:gag_btn(gags.water_glass,sqt_used,water_glass))
squirt_gun.configure(command=lambda:gag_btn(gags.squirt_gun,sqt_used,squirt_gun))
seltzer_bottle.configure(command=lambda:gag_btn(gags.seltzer_bottle,sqt_used,seltzer_bottle))
fire_hose.configure(command=lambda:gag_btn(gags.fire_hose,sqt_used,fire_hose))
storm_cloud.configure(command=lambda:gag_btn(gags.storm_cloud,sqt_used,storm_cloud))
geyser.configure(command=lambda:gag_btn(gags.geyser,sqt_used,geyser))
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
flower_pot.configure(command=lambda:gag_btn(gags.flower_pot,drp_used,flower_pot))
sandbag.configure(command=lambda:gag_btn(gags.sandbag,drp_used,sandbag))
anvil.configure(command=lambda:gag_btn(gags.anvil,drp_used,anvil))
big_weight.configure(command=lambda:gag_btn(gags.big_weight,drp_used,big_weight))
safe.configure(command=lambda:gag_btn(gags.safe,drp_used,safe))
grand_piano.configure(command=lambda:gag_btn(gags.piano,drp_used,grand_piano))
toontanic.configure(command=lambda:gag_btn(gags.oceanliner,drp_used,toontanic))
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
banana_peel.configure(command=lambda:gag_btn(gags.banana_peel,trp_used,banana_peel))
rake.configure(command=lambda:gag_btn(gags.rake,trp_used,rake))
marbles.configure(command=lambda:gag_btn(gags.marbles,trp_used,marbles))
quicksand.configure(command=lambda:gag_btn(gags.quicksand,trp_used,quicksand))
trapdoor.configure(command=lambda:gag_btn(gags.trapdoor,trp_used,trapdoor))
tnt.configure(command=lambda:gag_btn(gags.tnt,trp_used,tnt))
railroad.configure(command=lambda:gag_btn(gags.railroad,trp_used,railroad))

#Button list - used for mass configuring the gag buttons
gag_btns=(bike_horn,whistle,bugle,aoogah,elephant_trunk,fog_horn,opera_singer,cupcake,fruit_pie_slice,cream_pie_slice,whole_fruit_pie,whole_cream_pie,birthday_cake,wedding_cake,squirting_flower,water_glass,squirt_gun,seltzer_bottle,fire_hose,storm_cloud,geyser,flower_pot,sandbag,anvil,big_weight,safe,grand_piano,toontanic,banana_peel,rake,marbles,quicksand,trapdoor,tnt,railroad)

#Calculation history
hist=Frame(col1)
hist_lbl=Label(hist,text="History")
hist_box=Text(hist,width=25,height=25,state=DISABLED,font=('Arial',10,'normal'),wrap=WORD)
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
clerk_will.configure(command=lambda:gag_btn(gags.will,trp_used))
clerk_penny.configure(command=lambda:gag_btn(gags.penny,trp_used))
clerk_clara.configure(command=lambda:gag_btn(gags.clara,trp_used))
sos_snd=Frame(sos_cards)
barb_img=PhotoImage(file='img/barbaraseville.png')
barb=Button(sos_snd,image=barb_img)
sid_img=PhotoImage(file='img/sidsonata.png')
sid=Button(sos_snd,image=sid_img)
moe_img=PhotoImage(file='img/moezart.png')
moe=Button(sos_snd,image=moe_img)
barb.configure(command=lambda:gag_btn(gags.barb,snd_used))
sid.configure(command=lambda:gag_btn(gags.sid,snd_used))
moe.configure(command=lambda:gag_btn(gags.moe,snd_used))
sos_drp=Frame(sos_cards)
ned_img=PhotoImage(file='img/clumsyned.png')
ned=Button(sos_drp,image=ned_img)
franz_img=PhotoImage(file='img/franzneckvein.png')
franz=Button(sos_drp,image=franz_img)
bess_img=PhotoImage(file='img/barnaclebessie.png')
bess=Button(sos_drp,image=bess_img)
ned.configure(command=lambda:gag_btn(gags.ned,drp_used))
franz.configure(command=lambda:gag_btn(gags.franz,drp_used))
bess.configure(command=lambda:gag_btn(gags.bess,drp_used))

###Keybinds

#Toggle organic functions
def tog_org_off(opt=""):
  organic.set(0)
  #print("Gags in calculations will no longer be organic!")
  org_btn.configure(command=tog_org_on)
  org_indicator.configure(text="Organic = OFF")
  for i in gag_btns:
    i.configure(bg='#1888D3',activebackground='#186AD3')
  window.bind('<'+keybinds.organic.key+'>',tog_org_on)
def tog_org_on(opt=""):
  organic.set(1)
  #print("Gags in calculations will now be organic!")
  org_btn.configure(command=tog_org_off)
  org_indicator.configure(text="Organic = ON")
  for i in gag_btns:
    i.configure(bg='darkorange',activebackground='orange')
  window.bind('<'+keybinds.organic.key+'>',tog_org_off)
org_btn.configure(command=tog_org_on)
window.bind('<'+keybinds.organic.key+'>',tog_org_on)

#Def Keybind
def def_swap(opt=""):
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
window.bind('<'+keybinds.defense.key+'>',def_swap)

#Swap a toggle
def tog_swap(par,tog):
  if tog.get()==0:
    tog.set(1)
  else:
    tog.set(0)
  calc_dmg()
  pin()
window.bind('<'+keybinds.lure.key+'>',lambda par: tog_swap(par,lured))
window.bind('<'+keybinds.v2.key+'>',lambda par: tog_swap(par,v2))
window.bind('<'+keybinds.pin.key+'>',lambda par: tog_swap(par,pin_val))

#Clear inputs function
def clear_inputs(opt=""):
  #print("Clearing gag inputs!")
  global def_lur_lock
  global snd_used
  global trw_used
  global sqt_used
  global drp_used
  global trp_used
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
window.bind('<'+keybinds.reset.key+'>',clear_inputs)

#Clear history function
def clear_history():
  #print("Clearing calculcation history!")
  hist_box.configure(state=NORMAL)
  hist_box.delete('1.0', END)
  hist_box.configure(state=DISABLED)
clear_hist_btn.configure(command=clear_history)

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
program_menu.add_checkbutton(label="Pin window",command=pin,variable=pin_val,onvalue=1,offvalue=0,accelerator="Alt+Up")
program_menu.add_separator()
program_menu.add_command(label="Check for update",command=lambda:update_checker.compare_versions(local_file="mod/version.txt",git_file="https://raw.githubusercontent.com/Vhou-Atroph/TT-Damage-Calculator/main/mod/version.txt"))
program_menu.add_command(label="Exit",command=lambda:window.destroy(),accelerator="Alt+F4")
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
cog_calc.grid(column=0,row=4,pady=3)

#Geometry - Calculation Results
calc_results.grid(column=0,row=0)
dmg_this_round.grid(column=0,row=0)
dmg_indicator.grid(column=1,row=0)
cog_level_indicator.grid(column=2,row=0)
org_indicator.grid(column=0,row=1,columnspan=3)

#Run
window.mainloop()