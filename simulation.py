import random
import numpy as np

global xx, yy
percs = ["%5 %95","%8 %92","%12 %88","%18 %82","%25 %75","%32 %68","%40 %60","%50 %50","%60 %40","%68 %32","%75 %25","%82 %18","%88 %12","%92 %8","%95 %5"]
xN="aaa"
xxx="425321" #0.Technique 1.Speed 2.Accuracy 3.Power 4.Intelligence 5.Experience 

yN="bbb"
yyy="534244"
END=9

simtype=1 #1:fast 2:every step 
xPrss,yPrss,xAtmp,yAtmp,xOppr,yOppr,xCnt,yCnt,xSc,ySc,xstrategy,ystrategy,xtactic,ytactic,x2pt,y2pt = (0,)*16 # = 0,0,0,0...

def string_to_array(s):
  return [int(c) + 1 if int(c) > 5 else int(c) for c in s]
def ovr_calc(arr):
    return np.sum(arr) * 5


xx=string_to_array(xxx)
yy=string_to_array(yyy)


def main():
  IntDex()
  print("%s ovr: %d"%(xx,ovr_calc(xx)))
  print("%s ovr: %d"%(yy,ovr_calc(yy)))
  counter=1
  print("%s %d - %d %s"%(xN,xSc,ySc,yN),end="  ")
  print("%s"%(percs[xx[0]-yy[0]+7]))
  while(counter < END or xSc == ySc):
    if counter < 6:
      side,chc,bn=decider(xx[0],yy[0],counter)
      wait(counter)
      if side != 0:
        combat(side,chc,bn)
    else:
      side,chc,bn=decider(xx[5],yy[5],counter)
      wait(counter)
      if side != 0:
        combat(side,chc,bn)


    print("%s %d - %d %s"%(xN,xSc,ySc,yN),end="  ")
    if counter < 5:
      print("%s"%(percs[xx[0]-yy[0]+7]))
    else:
      print("%s"%(percs[xx[5]-yy[5]+7]))
    wait(counter)



    print()
    if counter == 5:
      print("= = = = =")
    counter +=1

  print("= = = = =")
  pad = 20 - len(xN) 
  for i in range(pad):
      print ("",end=" ")
  print("%s %d - %d %s"%(xN,xSc,ySc,yN))
  print("Pressure             %d - %d "%(xPrss,yPrss))
  print("Pressure Rate        %d - %d "%(xPrss / (counter-1) * 100 if (counter-1) else 0, yPrss / (counter-1) * 100 if (counter-1) else 0))
  print("Conversion to Att.   %d - %d "%(xAtmp,yAtmp))
  print("Conversion Rate      %.2f - %.2f"%(xAtmp / xPrss * 100 if xPrss else 0, yAtmp / yPrss * 100 if yPrss else 0))
  print("Expected Damage      %.2f - %.2f "%(xOppr,yOppr))
  print("Critical Att. Made   %d - %d"%(x2pt,y2pt))
  print("Average Att. Made    %d - %d"%(xCnt-x2pt,yCnt-y2pt))
  print("True Striking        %.2f - %.2f" % (xSc / xAtmp * 100 if xAtmp else 0, ySc / yAtmp * 100 if yAtmp else 0))
  print("Striking Percentage  %.2f - %.2f "%(xCnt/xAtmp*100 if xAtmp else 0,yCnt / yAtmp * 100 if yAtmp else 0))
  print("Strategy             %d - %d "%(xtactic,ytactic))
  print("Round                %d "%(counter-1))
  print("= = = = =")



def wait(cnt):
  global simtype
  if simtype==2:
    input('...')
  elif simtype==1:
    if cnt == 5 or cnt>=8:
      input('->')

def combat(side,chc,bn):
  global xSc,ySc,xOppr,yOppr,xCnt,yCnt,xAtmp,yAtmp
  rnd=random.randrange(0, 10)
  if chc % 2 == 0:
    if side == 1:
      xOppr += (xx[2]+bn)*10/100
      xAtmp += 1
      sc=acc(xx[2]+bn,side)
      xSc +=sc
      if not sc == 0:
        xCnt +=1
    if side == 2:
      yOppr += (yy[2]+bn)*10/100
      yAtmp += 1
      sc=acc(yy[2]+bn,side)
      ySc +=sc
      if not sc == 0:
        yCnt +=1

  else:
    if side == 1:
      xOppr += (xx[3]+bn)*10/100
      xAtmp += 1
      sc=ofdef((xx[3]+bn)*2)
      xSc +=sc
      if not sc == 0:
        xCnt +=1
    if side == 2:
      yOppr += (yy[3]+bn)*10/100
      yAtmp += 1
      sc=ofdef((yy[3]+bn)*2)
      ySc +=sc
      if not sc == 0:
        yCnt +=1

def ofdef(num):
  gal = 21-num
  roll = random.randrange(1, 21)
  if roll >= gal:
    print("1 point!",end="  ")
    return 1
  else:
    print("nope",end="  ")
    return 0

def acc(num,side):
  global x2pt,y2pt
  gal = 21-num
  roll = random.randrange(1, 21)
  if roll >= gal:
    print("2 points!",end="  ")
    if side == 1:
      x2pt +=1
    else:
      y2pt +=1
    return 2
  else:
    print("nope",end="  ")
    return 0

def stat(side,bn):
  chance = 0
  if xstrategy != 0 and side == 1:
    rnd=random.randrange(1, 10)
    if rnd % 3 == 0:
      chance = (xstrategy + 1) % 2
    else:
      chance = xstrategy % 2
  elif ystrategy != 0 and side == 2:
    rnd=random.randrange(1, 10)
    if rnd % 3 == 0:
      chance = (ystrategy + 1) % 2
    else:
      chance = ystrategy % 2
  else:
    rnd=random.randrange(0, 10)
    chance = rnd % 2

  if side == 1:
    if chance == 0:
      print ("2 pt: %d percent"%((xx[2]+bn)*5))
      return 1,2,bn
    else:
      print ("1 pt: %d percent"%((xx[3]+bn)*10))
      return 1,1,bn
  if side == 2:
    if chance == 0:
      print ("2 pt: %d percent"%((yy[2]+bn)*5))
      return 2,2,bn
    else:
      print ("1 pt: %d percent"%((yy[3]+bn)*10))
      return 2,1,bn


def decider(x,y,cnt):
  global xPrss,yPrss
  print("%d."%(cnt),end=" ")
  x += random.randrange(0, 10)
  y += random.randrange(0, 10)
  if x>y:
    print("%s attacks"%(xN),end="  ")
    xPrss += 1
    dc2=deciderSlc(xx[1],yy[1])
    if dc2 % 2 != 0 or dc2 == 0:
      if dc2 == 3:
        print("dangerously",end=" ")
        return stat(1,1)
      else:
        return stat(1,0)
    else:
      print("slow")
      return 0,0,0

  elif x<y:
    print("%s attacks"%(yN),end="  ")
    yPrss += 1
    dc2=deciderSlc(xx[1],yy[1])
    if dc2 % 2 != 1:
      if dc2 == 4:
        print("dangerously",end=" ")
        return stat(2,1)
      else:
        return stat(2,0)
    else:
      print("slow")
      return 0,0,0
  elif x==y:
    dec=random.randrange(1, 3)
    if dec==1:
      print("%s attacks"%(xN),end="  ")
      xPrss += 1
      dc2=deciderSlc(xx[1],yy[1])
      if dc2 % 2 != 0 or dc2 == 0:
        if dc2 == 3:
          print("dangerously",end=" ")
          return stat(1,1)
        else:
          return stat(1,0)
      else:
        print("slow")
        return 0,0,0
    else:
      print("%s attacks"%(yN),end="  ")
      yPrss += 1
      dc2=deciderSlc(xx[1],yy[1])
      if dc2 % 2 != 1:
        if dc2 == 4:
          print("dangerously",end=" ")
          return stat(2,1)
        else:
          return stat(2,0)
      else:
        print("slow")
        return 0,0,0

def IntDex():
  global strategy, xstrategy, ystrategy, xtactic, ytactic
  intDec=deciderSlc(xx[4],yy[4])
  if intDec % 2 == 0 and intDec != 0:
    if xx[1]<xx[0]:
      temp = xx[0]
      xx[0]=xx[1]
      xx[1]=temp
    ytactic += 1
    if intDec == 4:
      if yy[1]>yy[0]:
        temp = yy[0]
        yy[0]=yy[1]
        yy[1]=temp
      if xx[2] > xx[3]:
        xstrategy=1
      else:
        xstrategy=2
      ytactic += 1
      print("dude!",end=" ")
    print("y outsmarts")
    if yy[2] <= yy[3]:
      ystrategy=1
    else:
      ystrategy=2
    print()
  elif intDec % 2 == 1:
    if yy[1]<yy[0]:
      temp = yy[0]
      yy[0]=yy[1]
      yy[1]=temp
    xtactic += 1
    if intDec == 3:
      if xx[1]>xx[0]:
        temp = xx[0]
        xx[0]=xx[1]
        xx[1]=temp
      if yy[2] > yy[3]:
        ystrategy=1
      else:
        ystrategy=2
      xtactic += 1
      print("dude!",end=" ")
    print("x outsmarts")
    if xx[2] <= xx[3]:
      xstrategy=1
    else:
      xstrategy=2
    print()
  else:
    print("hmm")
    print()

def deciderSlc(x,y):
  x += random.randrange(0, 10)
  y += random.randrange(0, 10)
  if x>y+4:
    return 3
  elif x>y+1:
    return 1
  elif x+4<y:
    return 4
  elif x+1<y:
    return 2
  else:
    return 0

if __name__ == "__main__":
  main()