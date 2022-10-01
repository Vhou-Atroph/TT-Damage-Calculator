"""
TT-Damage-Calculator
Copyright (C) 2022 Vhou-Atroph

TT-Damage-Calculator is a gag damage calculator for Toontown Rewritten. It has an interface built with Python's tkinter library, and is supplemented with modules written in Rust.

CONTRIBUTORS:
- Vhou-Atroph
- BoggoTV
"""

from tkinter import *

from mod import tt_calc
from mod import tt_gags
from mod import tt_settings
from mod import update_checker

#Window
global window
window=Tk()
window.title("Toontown Damage Calculator")
whole_cream_pie_img=PhotoImage(file="img/whole-cream-pie.png")
window.iconphoto(True, whole_cream_pie_img)
window.resizable(0,0)

#Variables
global snd_used
global trw_used
global sqt_used
global drp_used
global trp_used
snd_used=[]
trw_used=[]
sqt_used=[]
drp_used=[]
trp_used=[]

organic=BooleanVar()
lured=BooleanVar()
pin_val=BooleanVar()
dmg_down=DoubleVar()
plating_lvl=IntVar()
status_lock=BooleanVar()
dmg_down.set(0.0)
plating_lvl.set(0)

settings = tt_settings.Settings("mod/settings.toml")

#Columns
col0=Frame(window) #Main content of the calculator
col1=Frame(window) #Will be used for calculation history

#Total damage calculation
def calc_dmg(*args):
  tot_dmg=tt_calc.full_calc(trp_used,snd_used,trw_used,sqt_used,drp_used,lured.get(),dmg_down.get(),plating_lvl.get())
  cog_level_indicator.configure(text=tt_calc.lvl_ind_string(tt_calc.lvl_ind(tot_dmg),int(dmg_down.get()*100),plating_lvl.get()))
  dmg_indicator.configure(text=str(tot_dmg))

#Pin window to top
def pin():
  if pin_val.get():
    return window.attributes('-topmost',True)
  window.attributes('-topmost',False)

#Toggles
tog_btns=Frame(col0)
org_btn=Button(tog_btns,text='Toggle Organic',font=('Arial',11,'normal'))
lur_check=Checkbutton(tog_btns,text='Cog lured',variable=lured,onvalue=1,offvalue=0,font=('Arial',11,'normal'),command=calc_dmg)
clear_btn=Button(tog_btns,text='Reset damage',font=('Arial',11,'normal'))

#The Gags
class GagButton(Button):
  def __init__(self,parent,image,gag):
    self.gag = gag
    Button.__init__(self,parent)
    self['image'] = image
    if self.gag.gtype == "Gag":
      self['bg'] = '#1888D3'
      self['activebackground'] = '#186AD3'
      self['text'] = '0'
      self['font'] = ('Impress BT',8,'bold')
      self['compound'] = 'top'
      self['fg'] = 'white'
    self['command'] = self.press
    self.grid(row=0,column=self.gag.level)
  def list(self):
    global trp_used
    global snd_used
    global trw_used
    global sqt_used
    global drp_used
    match self.gag.track:
      case "Trap":
        return trp_used
      case "Sound":
        return snd_used
      case "Throw":
        return trw_used
      case "Squirt":
        return sqt_used
      case "Drop":
        return drp_used
  def press(self):
    data = self.gag.button_press(organic.get())
    self.list().append(data[0])
    hist_box.configure(state=NORMAL)
    hist_box.insert('1.0',"Gag used: "+data[1]+" ("+str(data[0])+")\n")
    hist_box.configure(state=DISABLED)
    if self.gag.gtype == "Gag":
      self.configure(text=int(self.cget("text"))+1)
    calc_dmg()

gag_frame=Frame(col0)
#Sound
snd_frame=Frame(gag_frame)
bike_horn_img=PhotoImage(file='img/bike-horn.png')
bike_horn=GagButton(snd_frame,image=bike_horn_img,gag=tt_gags.Gag("Gag","Bike Horn","Sound",0,4))
whistle_img=PhotoImage(file='img/whistle.png')
whistle=GagButton(snd_frame,image=whistle_img,gag=tt_gags.Gag("Gag","Whistle","Sound",1,7))
bugle_img=PhotoImage(file='img/bugle.png')
bugle=GagButton(snd_frame,image=bugle_img,gag=tt_gags.Gag("Gag","Bugle","Sound",2,11))
aoogah_img=PhotoImage(file='img/aoogah.png')
aoogah=GagButton(snd_frame,image=aoogah_img,gag=tt_gags.Gag("Gag","Aoogah","Sound",3,16))
elephant_trunk_img=PhotoImage(file='img/elephant-trunk.png')
elephant_trunk=GagButton(snd_frame,image=elephant_trunk_img,gag=tt_gags.Gag("Gag","Elephant Trunk","Sound",4,21))
fog_horn_img=PhotoImage(file='img/fog-horn.png')
fog_horn=GagButton(snd_frame,image=fog_horn_img,gag=tt_gags.Gag("Gag","Fog Horn","Sound",5,50))
opera_singer_img=PhotoImage(file='img/opera-singer.png')
opera_singer=GagButton(snd_frame,image=opera_singer_img,gag=tt_gags.Gag("Gag","Opera Singer","Sound",6,90))
#Throw
trw_frame=Frame(gag_frame)
cupcake_img=PhotoImage(file='img/cupcake.png')
cupcake=GagButton(trw_frame,image=cupcake_img,gag=tt_gags.Gag("Gag","Cupcake","Throw",0,6))
fruit_pie_slice_img=PhotoImage(file='img/fruit-pie-slice.png')
fruit_pie_slice=GagButton(trw_frame,image=fruit_pie_slice_img,gag=tt_gags.Gag("Gag","Fruit Pie Slice","Throw",1,10))
cream_pie_slice_img=PhotoImage(file='img/cream-pie-slice.png')
cream_pie_slice=GagButton(trw_frame,image=cream_pie_slice_img,gag=tt_gags.Gag("Gag","Cream Pie Slice","Throw",2,17))
whole_fruit_pie_img=PhotoImage(file='img/whole-fruit-pie.png')
whole_fruit_pie=GagButton(trw_frame,image=whole_fruit_pie_img,gag=tt_gags.Gag("Gag","Whole Fruit Pie","Throw",3,27))
whole_cream_pie=GagButton(trw_frame,image=whole_cream_pie_img,gag=tt_gags.Gag("Gag","Whole Cream Pie","Throw",4,40))
birthday_cake_img=PhotoImage(file='img/birthday-cake.png')
birthday_cake=GagButton(trw_frame,image=birthday_cake_img,gag=tt_gags.Gag("Gag","Birthday Cake","Throw",5,100))
wedding_cake_img=PhotoImage(file='img/wedding-cake.png')
wedding_cake=GagButton(trw_frame,image=wedding_cake_img,gag=tt_gags.Gag("Gag","Wedding Cake","Throw",6,120))
#Squirt
sqt_frame=Frame(gag_frame)
squirting_flower_img=PhotoImage(file='img/squirting-flower.png')
squirting_flower=GagButton(sqt_frame,image=squirting_flower_img,gag=tt_gags.Gag("Gag","Squirting Flower","Squirt",0,4))
water_glass_img=PhotoImage(file='img/glass-of-water.png')
water_glass=GagButton(sqt_frame,image=water_glass_img,gag=tt_gags.Gag("Gag","Glass of Water","Squirt",1,8))
squirt_gun_img=PhotoImage(file='img/squirt-gun.png')
squirt_gun=GagButton(sqt_frame,image=squirt_gun_img,gag=tt_gags.Gag("Gag","Squirt Gun","Squirt",2,12))
seltzer_bottle_img=PhotoImage(file='img/seltzer-bottle.png')
seltzer_bottle=GagButton(sqt_frame,image=seltzer_bottle_img,gag=tt_gags.Gag("Gag","Seltzer Bottle","Squirt",3,21))
fire_hose_img=PhotoImage(file='img/fire-hose.png')
fire_hose=GagButton(sqt_frame,image=fire_hose_img,gag=tt_gags.Gag("Gag","Fire Hose","Squirt",4,30))
storm_cloud_img=PhotoImage(file='img/storm-cloud.png')
storm_cloud=GagButton(sqt_frame,image=storm_cloud_img,gag=tt_gags.Gag("Gag","Storm Cloud","Squirt",5,80))
geyser_img=PhotoImage(file='img/geyser.png')
geyser=GagButton(sqt_frame,image=geyser_img,gag=tt_gags.Gag("Gag","Geyser","Squirt",6,105))
#Drop
drp_frame=Frame(gag_frame)
flower_pot_img=PhotoImage(file='img/flower-pot.png')
flower_pot=GagButton(drp_frame,image=flower_pot_img,gag=tt_gags.Gag("Gag","Flower Pot","Drop",0,10))
sandbag_img=PhotoImage(file='img/sandbag.png')
sandbag=GagButton(drp_frame,image=sandbag_img,gag=tt_gags.Gag("Gag","Sandbag","Drop",1,18))
anvil_img=PhotoImage(file='img/anvil.png')
anvil=GagButton(drp_frame,image=anvil_img,gag=tt_gags.Gag("Gag","Anvil","Drop",2,30))
big_weight_img=PhotoImage(file='img/big-weight.png')
big_weight=GagButton(drp_frame,image=big_weight_img,gag=tt_gags.Gag("Gag","Big Weight","Drop",3,45))
safe_img=PhotoImage(file='img/safe.png')
safe=GagButton(drp_frame,image=safe_img,gag=tt_gags.Gag("Gag","Safe","Drop",4,70))
grand_piano_img=PhotoImage(file='img/grand-piano.png')
grand_piano=GagButton(drp_frame,image=grand_piano_img,gag=tt_gags.Gag("Gag","Grand Piano","Drop",5,170))
toontanic_img=PhotoImage(file='img/toontanic.png')
toontanic=GagButton(drp_frame,image=toontanic_img,gag=tt_gags.Gag("Gag","Toontanic","Drop",6,180))
#Trap!
trpFrame=Frame(gag_frame)
banana_peel_img=PhotoImage(file='img/banana-peel.png')
banana_peel=GagButton(trpFrame,image=banana_peel_img,gag=tt_gags.Gag("Gag","Banana Peel","Trap",0,12))
rake_img=PhotoImage(file='img/rake.png')
rake=GagButton(trpFrame,image=rake_img,gag=tt_gags.Gag("Gag","Rake","Trap",1,18))
marbles_img=PhotoImage(file='img/marbles.png')
marbles=GagButton(trpFrame,image=marbles_img,gag=tt_gags.Gag("Gag","Marbles","Trap",2,35))
quicksand_img=PhotoImage(file='img/quicksand.png')
quicksand=GagButton(trpFrame,image=quicksand_img,gag=tt_gags.Gag("Gag","Quicksand","Trap",3,50))
trapdoor_img=PhotoImage(file='img/trapdoor.png')
trapdoor=GagButton(trpFrame,image=trapdoor_img,gag=tt_gags.Gag("Gag","Trapdoor","Trap",4,85))
tnt_img=PhotoImage(file='img/tnt.png')
tnt=GagButton(trpFrame,image=tnt_img,gag=tt_gags.Gag("Gag","TNT","Trap",5,180))
railroad_img=PhotoImage(file='img/railroad.png')
railroad=GagButton(trpFrame,image=railroad_img,gag=tt_gags.Gag("Gag","Railroad","Trap",6,200))

gag_btns=[bike_horn,whistle,bugle,aoogah,elephant_trunk,fog_horn,opera_singer,cupcake,fruit_pie_slice,cream_pie_slice,whole_fruit_pie,whole_cream_pie,birthday_cake,wedding_cake,squirting_flower,water_glass,squirt_gun,seltzer_bottle,fire_hose,storm_cloud,geyser,flower_pot,sandbag,anvil,big_weight,safe,grand_piano,toontanic,banana_peel,rake,marbles,quicksand,trapdoor,tnt,railroad]

#Calculation history
hist=Frame(col1)
hist_lbl=Label(hist,text="History")
hist_box=Text(hist,width=25,height=22,state=DISABLED,font=('Arial',10,'normal'),wrap=WORD)
clear_hist_btn=Button(hist,text="Clear History")
cog_calc=Button(hist,text="Show Health and\n SOS Cards")

#Calculation results
calc_results=Frame(col0)
dmg_this_round=Label(calc_results,text="Damage this round:",font=('Arial',16,'normal'))
dmg_indicator=Label(calc_results,text="0",font=('Arial',16,'bold'))
cog_level_indicator=Label(calc_results,text="Level 0",font=('Arial',8,'normal'))
org_indicator=Label(calc_results,text="Organic = OFF",font=('Arial',10,'bold'))

#Cog HP
cog_health_sheet=Frame(window)
cog_health_img=PhotoImage(file='img/coghp.png')
cog_health_lbl=Label(cog_health_sheet,image=cog_health_img)

#SOS Cards
sos_cards=Frame(window)
sos_trp=Frame(sos_cards)
clerk_will_img=PhotoImage(file='img/clerkwill.png')
clerk_will=GagButton(sos_trp,image=clerk_will_img,gag=tt_gags.Gag("Sos","Clerk Will","Trap",0,60))
clerk_penny_img=PhotoImage(file='img/clerkpenny.png')
clerk_penny=GagButton(sos_trp,image=clerk_penny_img,gag=tt_gags.Gag("Sos","Clerk Penny","Trap",1,120))
clerk_clara_img=PhotoImage(file='img/clerkclara.png')
clerk_clara=GagButton(sos_trp,image=clerk_clara_img,gag=tt_gags.Gag("Sos","Clerk Clara","Trap",2,180))
sos_snd=Frame(sos_cards)
barb_img=PhotoImage(file='img/barbaraseville.png')
barb=GagButton(sos_snd,image=barb_img,gag=tt_gags.Gag("Sos","Barbara Seville","Sound",0,35))
sid_img=PhotoImage(file='img/sidsonata.png')
sid=GagButton(sos_snd,image=sid_img,gag=tt_gags.Gag("Sos","Sid Sonata","Sound",1,55))
moe_img=PhotoImage(file='img/moezart.png')
moe=GagButton(sos_snd,image=moe_img,gag=tt_gags.Gag("Sos","Moe Zart","Sound",2,75))
sos_drp=Frame(sos_cards)
ned_img=PhotoImage(file='img/clumsyned.png')
ned=GagButton(sos_drp,image=ned_img,gag=tt_gags.Gag("Sos","Clumsy Ned","Drop",0,60))
franz_img=PhotoImage(file='img/franzneckvein.png')
franz=GagButton(sos_drp,image=franz_img,gag=tt_gags.Gag("Sos","Franz Neckvein","Drop",1,100))
bess_img=PhotoImage(file='img/barnaclebessie.png')
bess=GagButton(sos_drp,image=bess_img,gag=tt_gags.Gag("Sos","Barnacle Bessie","Drop",2,170))

###Keybinds
window.bind('<'+settings.keybinds.v2+'>',lambda par: [plating_lvl.set(tt_calc.advance_int([0,9,10,11,12],plating_lvl.get())),calc_dmg()])
window.bind('<'+settings.keybinds.defense+'>',lambda par: [dmg_down.set(tt_calc.advance_float([0.0,0.1,0.15,0.2,0.25],dmg_down.get())),calc_dmg()])


#Organic gag toggle
def organic_toggle(*arg):
  if organic.get():
    organic.set(False)
    org_indicator.configure(text="Organic = OFF")
    for i in gag_btns:
      i.configure(bg='#1888D3',activebackground='#186AD3')
  else:
    organic.set(True)
    org_indicator.configure(text="Organic = ON")
    for i in gag_btns:
      i.configure(bg='darkorange',activebackground='orange')
org_btn.configure(command=organic_toggle)
window.bind('<'+settings.keybinds.organic+'>',organic_toggle)

#Swap a toggle
def tog_swap(tog):
  if tog.get():
    return tog.set(False)
  tog.set(True)
  calc_dmg()
  pin()
window.bind('<'+settings.keybinds.lure+'>',lambda par: tog_swap(lured))
window.bind('<'+settings.keybinds.lock+'>',lambda par: tog_swap(status_lock))
window.bind('<'+settings.keybinds.pin+'>',lambda par: tog_swap(pin_val))

#Clear inputs function
def clear_inputs(*arg):
  global snd_used
  global trw_used
  global sqt_used
  global drp_used
  global trp_used
  hist_box.configure(state=NORMAL)
  hist_box.insert('1.0',tt_calc.calc_fin_string(int(dmg_indicator.cget("text")),tt_calc.lvl_ind(int(dmg_indicator.cget("text"))),lured.get(),int(dmg_down.get()*100),plating_lvl.get()))
  hist_box.configure(state=DISABLED)
  if organic.get():
    organic_toggle()
  snd_used=[]
  trw_used=[]
  sqt_used=[]
  drp_used=[]
  trp_used=[]
  for i in gag_btns:
    i.configure(text='0')
  if not status_lock.get():
    plating_lvl.set(0)
    dmg_down.set(0.0)
    lured.set(0)
  calc_dmg()
clear_btn.configure(command=clear_inputs)
window.bind('<'+settings.keybinds.reset+'>',clear_inputs)

#Clear history function
def clear_history():
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
  cog_calc.configure(text='Hide Health and\n SOS Cards',command=cog_health_calc_hide)
  window.geometry('')
cog_calc.configure(command=cog_health_calc_show)

#Toolbar
toolbar=Menu(window)
#Program
program_menu=Menu(toolbar,tearoff=0)
program_menu.add_checkbutton(label="Pin window",command=pin,variable=pin_val,onvalue=True,offvalue=False,accelerator="Alt+Up")
program_menu.add_separator()
program_menu.add_command(label="Check for update",command=lambda:update_checker.compare_versions(local_file="mod/version.txt",git_file="https://raw.githubusercontent.com/Vhou-Atroph/TT-Damage-Calculator/main/mod/version.txt"))
program_menu.add_command(label="Exit",command=lambda:window.destroy(),accelerator="Alt+F4")
toolbar.add_cascade(label="Program",menu=program_menu)
calculations_menu=Menu(toolbar,tearoff=0)
def_menu=Menu(calculations_menu,tearoff=0)
def_menu.add_radiobutton(label="None",value=0.0,variable=dmg_down,command=calc_dmg)
def_menu.add_radiobutton(label="10% (1⭐)",value=0.1,variable=dmg_down,command=calc_dmg)
def_menu.add_radiobutton(label="15% (2⭐)",value=0.15,variable=dmg_down,command=calc_dmg)
def_menu.add_radiobutton(label="20% (3⭐)",value=0.2,variable=dmg_down,command=calc_dmg)
def_menu.add_radiobutton(label="25% (4⭐)",value=0.25,variable=dmg_down,command=calc_dmg)
calculations_menu.add_cascade(label="Cog Defense",menu=def_menu)
v2_menu=Menu(calculations_menu,tearoff=0)
v2_menu.add_radiobutton(label="None",value=0,variable=plating_lvl,command=calc_dmg)
v2_menu.add_radiobutton(label="Level 9",value=9,variable=plating_lvl,command=calc_dmg)
v2_menu.add_radiobutton(label="Level 10",value=10,variable=plating_lvl,command=calc_dmg)
v2_menu.add_radiobutton(label="Level 11",value=11,variable=plating_lvl,command=calc_dmg)
v2_menu.add_radiobutton(label="Level 12",value=12,variable=plating_lvl,command=calc_dmg)
calculations_menu.add_cascade(label="V2.0 Cogs",menu=v2_menu)
calculations_menu.add_separator()
calculations_menu.add_checkbutton(label="Lock Status",variable=status_lock,onvalue=True,offvalue=False)
toolbar.add_cascade(label="Calculations",menu=calculations_menu)
window.configure(menu=toolbar)

#Geometry - Main Columns
col0.grid(column=0,row=0,padx=5)
col1.grid(column=1,row=0,padx=10)

#Geometry - Toggles
tog_btns.grid(column=0,row=1,pady=5)
lur_check.grid(column=0,row=0,padx=5)
org_btn.grid(column=1,row=0,padx=5)
clear_btn.grid(column=2,row=0,columnspan=2,padx=5)

#Geometry - Gags
gag_frame.grid(column=0,row=2,pady=10)
snd_frame.grid(column=0,row=1,)
trw_frame.grid(column=0,row=2)
sqt_frame.grid(column=0,row=3)
drp_frame.grid(column=0,row=4)
trpFrame.grid(column=0,row=0)
sos_trp.grid(column=0,row=0)
sos_snd.grid(column=0,row=1)
sos_drp.grid(column=0,row=2)

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