import random


modif = ["","'","2"]
def scramble_fm(s,len,mods=modif):
  cb = ""
  a = ""
  res = ""
  for _ in range(len):
    while a == cb:  
      a = random.choice(s)
      
    res +=  a + random.choice(mods) + " "
    cb = a
  return res


_s3 = ["R","L","U","D","F","B"]
scramble_3x3 = lambda l=20: scramble_fm(_s3,l)
_s2 = ["R","U","F"]
scramble_2x2 = lambda l=9: scramble_fm(_s2,l)

_s4 = ["R","L","U","D","F","B","Fw","Rw","Uw"]
scramble_4x4 = lambda l=45: scramble_fm(_s4,l)

scramble_5x5 = lambda l=60: scramble_fm(_s4,l)

_rcn = lambda: random.randrange(0,6)
_rcs = lambda: random.choice(["+","-"])
def _rpn(pins= ["UR","UL","DR","DL"],mods=['']):
  np = random.randrange(0,len(pins)+1)
  po = ""
  for _ in range(np):
    
    p = random.choice(pins)
    po += p + random.choice(mods) +" "
    ind = pins.index(p)
    del pins[ind]
  return po



def scramble_clock():
  pins = ["UR","DR","DL","UL","U","R","D","L","ALL","y2","U","R","D","L","ALL"]
  res = ""
  for pin in pins:
    if pin == "y2":
      res += pin + " "
      continue
    res += pin + str(_rcn()) + _rcs() + " "
  return res + _rpn()
  


scramble_pyraminx = lambda l=9: scramble_fm(["R","L","U","B"],l,["","'"]) + _rpn(["r","b",'u','l'],["","\'"])

scramble_skewb = lambda l=9: scramble_fm(["R","L","U","B"],l,["","'"])


scramble_3bld = lambda l=20: scramble_fm(_s3,l,["","'"]) + _rpn(["R",'U','F'],["w","w\'","w2"])


scrambled = {"3x3":scramble_3x3,\
						 "2x2":scramble_2x2,\
						 "4x4":scramble_4x4,\
						 "5x5":scramble_5x5,\
						 "pyraminx":scramble_pyraminx,\
						 "skewb":scramble_skewb,\
						 "clock":scramble_clock,\
						 "3bld": scramble_3bld}
