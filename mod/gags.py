#This module is to stop gag press functions from completely cluttering the main file. If I can make this properly, like 500 lines will be eliminated forever and sent to the void. Exciting! Update: after finishing everything, it looks like I reduced the file size by 509 lines and 16KB! Wow!
import math

class Gag:
  def __init__(self,type=str,name=str,track=str,dmg=int):
    self.type=type #Gag or SOS Card
    self.name=name #Name of the gag
    self.track=track #Track of the gag
    self.dmg=dmg #Base damage of the gag
  def make_org(self): #Make the gag organic
    if self.dmg*.1<1: return self.dmg+1 
    else: return self.dmg+math.floor(self.dmg*.1)

#Sound gags and SOS cards
bike_horn=Gag(type="Gag",name="Bike Horn",track="Sound",dmg=4)
whistle=Gag(type="Gag",name="Whistle",track="Sound",dmg=7)
bugle=Gag(type="Gag",name="Bugle",track="Sound",dmg=11)
aoogah=Gag(type="Gag",name="Aoogah",track="Sound",dmg=16)
elephant_trunk=Gag(type="Gag",name="Elephant Trunk",track="Sound",dmg=21)
foghorn=Gag(type="Gag",name="Foghorn",track="Sound",dmg=50)
opera_singer=Gag(type="Gag",name="Opera Singer",track="Sound",dmg=90)
barb=Gag(type="SOS",name="Barbara Seville",track="Sound",dmg=35)
sid=Gag(type="SOS",name="Sid Sonata",track="Sound",dmg=55)
moe=Gag(type="SOS",name="Moe Zart",track="Sound",dmg=75)

#Throw gags and SOS cards
cupcake=Gag(type="Gag",name="Cupcake",track="Throw",dmg=6)
fruit_pie_slice=Gag(type="Gag",name="Fruit Pie Slice",track="Throw",dmg=10)
cream_pie_slice=Gag(type="Gag",name="Cream Pie Slice",track="Throw",dmg=17)
whole_fruit_pie=Gag(type="Gag",name="Whole Fruit Pie",track="Throw",dmg=27)
whole_cream_pie=Gag(type="Gag",name="Whole Cream Pie",track="Throw",dmg=40)
birthday_cake=Gag(type="Gag",name="Birthday Cake",track="Throw",dmg=100)
wedding_cake=Gag(type="Gag",name="Wedding Cake",track="Throw",dmg=132)
rocky=Gag(type="SOS",name="Rocky",track="Throw",dmg=120)

#Squirt gags and SOS cards
squirting_flower=Gag(type="Gag",name="Squirting Flower",track="Squirt",dmg=4)
water_glass=Gag(type="Gag",name="Glass of Water",track="Squirt",dmg=8)
squirt_gun=Gag(type="Gag",name="Squirt Gun",track="Squirt",dmg=12)
seltzer_bottle=Gag(type="Gag",name="Seltzer Bottle",track="Squirt",dmg=21)
fire_hose=Gag(type="Gag",name="Fire Hose",track="Squirt",dmg=30)
storm_cloud=Gag(type="Gag",name="Storm Cloud",track="Squirt",dmg=80)
geyser=Gag(type="Gag",name="Geyser",track="Squirt",dmg=105)
loopy=Gag(type="SOS",name="Loopy Loopenloop",track="Squirt",dmg=115)

#Drop gags and SOS cards
flower_pot=Gag(type="Gag",name="Flower Pot",track="Drop",dmg=10)
sandbag=Gag(type="Gag",name="Sandbag",track="Drop",dmg=18)
anvil=Gag(type="Gag",name="Anvil",track="Drop",dmg=30)
big_weight=Gag(type="Gag",name="Big Weight",track="Drop",dmg=45)
safe=Gag(type="Gag",name="Safe",track="Drop",dmg=70)
piano=Gag(type="Gag",name="Grand Piano",track="Drop",dmg=170)
oceanliner=Gag(type="Gag",name="Toontanic",track="Drop",dmg=180)
ned=Gag(type="SOS",name="Clumsy Ned",track="Drop",dmg=60)
franz=Gag(type="SOS",name="Franz Neckvein",track="Drop",dmg=100)
bess=Gag(type="SOS",name="Barnacle Bessie",track="Drop",dmg=170)

#Trap gags and SOS cards
banana_peel=Gag(type="Gag",name="Banana Peel",track="Drop",dmg=12)
rake=Gag(type="Gag",name="Rake",track="Drop",dmg=20)
marbles=Gag(type="Gag",name="Marbles",track="Drop",dmg=35)
quicksand=Gag(type="Gag",name="Quicksand",track="Drop",dmg=50)
trapdoor=Gag(type="Gag",name="Trap Door",track="Drop",dmg=85)
tnt=Gag(type="Gag",name="TNT",track="Drop",dmg=180)
railroad=Gag(type="Gag",name="Railroad",track="Drop",dmg=200)
will=Gag(type="SOS",name="Clerk Will",track="Drop",dmg=60)
penny=Gag(type="SOS",name="Clerk Penny",track="Drop",dmg=120)
clara=Gag(type="SOS",name="Clerk Clara",track="Drop",dmg=180)