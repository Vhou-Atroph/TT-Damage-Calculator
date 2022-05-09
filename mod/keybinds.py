import toml

class Bind:
  def __init__(self,key_id):
    self.key_id=key_id
    settingsfile=toml.loads(open("mod/settings.toml","r").read())
    self.key=settingsfile['keybinds'][key_id]

organic=Bind('organic')
reset=Bind('reset')
lure=Bind('lure')
defense=Bind('defense')
v2=Bind('v2')
pin=Bind('pin')