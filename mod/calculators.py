#This file stores math functions for the calculator to reduce overall file size. It's been getting excessively painful navigating a 1000+ line file recently.
import math

def cog_health(level):
  if 0<level<12:
    return (level+1)*(level+2)
  elif 11<level<21:
    return (level+1)*(level+2)+14
  else:
    raise ValueError("Cog levels cannot exceed 20 or be lower than 1.")

def cog_defense(gaglist,strength=0):
  new_gaglist=[]
  for gag in range(len(gaglist)):
    new_gaglist.append(gaglist[gag]-math.ceil(gaglist[gag]*strength))
  return new_gaglist

def reinforced_plating(gaglist,level=0):
  new_gaglist=[]
  for gag in range(len(gaglist)):
    damage=(gaglist[gag]-math.floor(level*1.5))
    if damage>0:
      new_gaglist.append(damage)
  return new_gaglist

def lureless_gagclc(gaglist):
  raw=sum(gaglist,0)
  if len(gaglist)>1:
    return raw+math.ceil(raw*.2)
  else:
    return raw

def lured_gagclc(gaglist):
  raw=sum(gaglist,0)
  if len(gaglist)>1:
    return raw+math.ceil(raw*.2)+math.ceil(raw*.5)
  else:
    return raw+math.ceil(raw*.5)

def gag_calculator(gaglist,lured=0,defense=None,plating=None):
  if defense:
    gaglist=cog_defense(gaglist,defense)
  elif plating:
    gaglist=reinforced_plating(gaglist,plating)
  if lured==1:
    return lured_gagclc(gaglist)
  else:
    return lureless_gagclc(gaglist)