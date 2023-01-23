def Zellers(a,b,c):
  if a==11 or a==12:
    c=c-1
  c = c%100
  d = c//100
  w = (13*a-1)//5
  x = c//4
  y = d//4
  z = w+x+y+b+c-2*d
  r = z%7
  if r==0:
    print("Sunday")
  elif r==1:
    print("Monday")
  elif r==2:
    print("Tuesday")
  elif r==3:
    print("Wednesday")
  elif r==4:
    print("Thursday")
  elif r==5:
    print("Friday")
  else:
    print("Saturday")
